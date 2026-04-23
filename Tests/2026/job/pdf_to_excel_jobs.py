"""
╔══════════════════════════════════════════════════════════════════════════════╗
║          QA JOB LISTINGS PDF → EXCEL EXTRACTOR                             ║
║          Author  : Senior Python Automation Engineer                        ║
║          Usage   : python pdf_to_excel_jobs.py [path/to/jobs.pdf]           ║
║          Requires: pip install pdfplumber pandas openpyxl                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT THIS SCRIPT DOES (beginner-friendly overview):
────────────────────────────────────────────────────
1. Opens the PDF and reads every page as plain text.
2. Strips all noise (headers, footers, ads, page numbers).
3. Splits the cleaned text into individual job blocks using "Company:" as the boundary.
4. For every block, extracts 6 fields using regex + string matching.
5. Deduplicates rows (same company + same job title).
6. Writes a professionally styled Excel file with:
      • Sheet 1 – Full job data table (freeze panes, auto-filter, alt row shading)
      • Sheet 2 – Summary statistics
"""

import sys
import re
import os
import logging
import argparse
from datetime import datetime

import pdfplumber
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ─────────────────────────────────────────────────────────────────────────────
# LOGGING SETUP
# ─────────────────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# STEP 1 – Extract full text from PDF
# WHY pdfplumber? It preserves text layout better than PyPDF2 for complex PDFs.
# ─────────────────────────────────────────────────────────────────────────────
def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Open the PDF page by page and return one big text string.
    Handles missing CropBox warnings gracefully.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    log.info(f"Reading PDF → {pdf_path}")
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text() or ""
            full_text += page_text + "\n"
            log.info(f"  Page {i:03d}: {len(page_text):,} chars extracted")

    log.info(f"Total characters: {len(full_text):,}")
    return full_text


# ─────────────────────────────────────────────────────────────────────────────
# STEP 2a – Remove header/footer/promotional noise
# WHY? These recurring lines would corrupt field extraction if left in.
# ─────────────────────────────────────────────────────────────────────────────
NOISE_PATTERNS = [
    r"LATEST QA JOBS.*?(\n|$)",
    r"SHAMMI JHA.*?(\n|$)",
    r"Click to Join.*?(\n|$)",
    r"Join our.*?(\n|$)",
    r"Curated by.*?(\n|$)",
    r"Training & Updates.*?(\n|$)",
    r"✔.*?(\n|$)",
    r"India & Abroad.*?(\n|$)",
    r"India QA Jobs:.*?(\n|$)",
    r"Abroad QA Jobs:.*?(\n|$)",
    r"\d+ QA Opportunities.*?(\n|$)",
    r"Page No\..*?(\n|$)",
    r"DISCLAIMER.*",        # remove everything after disclaimer
]

def clean_text(text: str) -> str:
    """Strip headers, footers, and ads. Collapse excessive blank lines."""
    for pattern in NOISE_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ─────────────────────────────────────────────────────────────────────────────
# STEP 2b – Split cleaned text into individual job blocks
# LOGIC: Every job posting starts with "Company:" – use lookahead split.
# ─────────────────────────────────────────────────────────────────────────────
def split_jobs(text: str) -> list[str]:
    """
    Split on 'Company:' boundaries using a regex lookahead so the delimiter
    is included at the start of each chunk (not discarded).
    """
    parts = re.split(r"(?=Company\s*:)", text, flags=re.IGNORECASE)
    blocks = [p.strip() for p in parts if re.search(r"Company\s*:", p, re.IGNORECASE)]
    log.info(f"Total job blocks found: {len(blocks)}")
    return blocks


# ─────────────────────────────────────────────────────────────────────────────
# STEP 3 – Email extractor (pure regex)
# WHY regex? Emails follow a reliable pattern; no NLP needed.
# ─────────────────────────────────────────────────────────────────────────────
def extract_email(text: str) -> str:
    """Return the first valid email found in text, or empty string."""
    match = re.search(
        r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
        text
    )
    return match.group(0).strip() if match else ""


# ─────────────────────────────────────────────────────────────────────────────
# STEP 4 – Parse a single job block → dict
# DESIGN: Each field has a primary regex and a fallback.
#         Using non-greedy patterns + lookahead keeps fields from bleeding
#         into each other across multi-line values.
# ─────────────────────────────────────────────────────────────────────────────

# Field patterns: capture value between label and next known label (or end)
FIELD_PATTERNS = {
    "company":    r"Company\s*:\s*(.+?)(?=\n|Location\s*:|$)",
    "location":   r"Location\s*:\s*(.+?)(?=\n|Job Title\s*:|$)",
    "job_title":  r"Job Title\s*:\s*(.+?)(?=\n|Experience Required\s*:|$)",
    "experience": r"Experience Required\s*:\s*(.+?)(?=\n|Skills Required\s*:|$)",
    # Skills can be multi-line → stop at "Job Description:" or the resume line
    "skills":     r"Skills Required\s*:\s*([\s\S]+?)(?=\n\s*Job Description\s*:|Interested candidates|$)",
}

def _get_field(pattern: str, text: str) -> str:
    """Run a regex pattern, collapse internal whitespace, return clean value."""
    m = re.search(pattern, text, re.IGNORECASE)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip().rstrip(",;.")
    return ""

def parse_job_block(block: str, index: int) -> dict:
    """
    Extract all 6 fields from a single job block string.
    Falls back gracefully when a field is absent.

    Args:
        block (str): Raw text for one job posting.
        index (int): Job sequence number for logging.

    Returns:
        dict: {Company Name, Location, Job Title, Experience, Skills, HR Email}
    """
    result = {
        "Company Name": _get_field(FIELD_PATTERNS["company"],    block),
        "Location":     _get_field(FIELD_PATTERNS["location"],   block),
        "Job Title":    _get_field(FIELD_PATTERNS["job_title"],  block),
        "Experience":   _get_field(FIELD_PATTERNS["experience"], block),
        "Skills":       _get_field(FIELD_PATTERNS["skills"],     block),
        "HR Email":     extract_email(block),
    }

    # Fallback: if skills multi-line pattern missed, try single-line grab
    if not result["Skills"]:
        m = re.search(r"Skills Required\s*:\s*(.+)", block, re.IGNORECASE)
        if m:
            result["Skills"] = re.sub(r"\s+", " ", m.group(1)).strip()

    log.info(
        f"  Job {index:02d} | {result['Company Name'][:30]:<30} | "
        f"{result['Job Title'][:35]:<35} | Email: {'✓' if result['HR Email'] else '✗'}"
    )
    return result


# ─────────────────────────────────────────────────────────────────────────────
# STEP 5 – Write styled Excel output
# DESIGN: First dump with pandas (handles CSV → sheet), then re-open with
#         openpyxl for rich formatting. Keeps code clean and avoids
#         manually writing every cell.
# ─────────────────────────────────────────────────────────────────────────────

# Colors & shared styles
HEADER_BG  = "1F3864"   # deep navy
HEADER_FG  = "FFFFFF"
ALT_ROW_BG = "EAF2FB"   # light blue
ACCENT     = "2E75B6"   # steel blue (emails)
BORDER_CLR = "BFBFBF"

HDR_FONT   = Font(name="Calibri", bold=True, color=HEADER_FG, size=11)
HDR_FILL   = PatternFill("solid", fgColor=HEADER_BG)
HDR_ALIGN  = Alignment(horizontal="center", vertical="center", wrap_text=True)
BODY_FONT  = Font(name="Calibri", size=10)
EMAIL_FONT = Font(name="Calibri", size=10, color=ACCENT)
ALT_FILL   = PatternFill("solid", fgColor=ALT_ROW_BG)
WRAP_ALIGN = Alignment(vertical="top", wrap_text=True)
THIN       = Side(style="thin", color=BORDER_CLR)
BORDER     = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

COLUMNS = ["Company Name", "Location", "Job Title", "Experience", "Skills", "HR Email"]
COL_WIDTHS = {1: 30, 2: 28, 3: 35, 4: 20, 5: 45, 6: 35}


def write_to_excel(jobs: list[dict], output_path: str) -> None:
    """
    Convert parsed job list to a professionally styled Excel file.
    Sheet 1: Full data table  |  Sheet 2: Summary statistics
    """
    df = pd.DataFrame(jobs, columns=COLUMNS)

    # ── Deduplication ────────────────────────────────────────────────────
    before = len(df)
    df.drop_duplicates(subset=["Company Name", "Job Title"], keep="first", inplace=True)
    df.reset_index(drop=True, inplace=True)
    removed = before - len(df)
    if removed:
        log.info(f"Duplicates removed: {removed}")

    # ── Pandas initial dump ───────────────────────────────────────────────
    df.to_excel(output_path, index=False, sheet_name="QA Jobs")

    # ── openpyxl styling ──────────────────────────────────────────────────
    wb = load_workbook(output_path)
    ws = wb.active
    ws.title = "QA Jobs"

    total_rows = ws.max_row
    total_cols = ws.max_column

    # Header row (row 1)
    ws.row_dimensions[1].height = 32
    for col in range(1, total_cols + 1):
        cell = ws.cell(row=1, column=col)
        cell.font, cell.fill, cell.alignment, cell.border = (
            HDR_FONT, HDR_FILL, HDR_ALIGN, BORDER)

    # Data rows
    for row in range(2, total_rows + 1):
        ws.row_dimensions[row].height = 60
        for col in range(1, total_cols + 1):
            cell = ws.cell(row=row, column=col)
            cell.border    = BORDER
            cell.alignment = WRAP_ALIGN
            cell.font      = EMAIL_FONT if col == 6 else BODY_FONT
            if row % 2 == 0:
                cell.fill = ALT_FILL

    # Column widths
    for col_idx, width in COL_WIDTHS.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    # Freeze header + auto-filter
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions

    # ── Insert title rows above table ─────────────────────────────────────
    ws.insert_rows(1, amount=3)

    ws.merge_cells("A1:F1")
    t = ws["A1"]
    t.value     = "🗂️  QA Job Listings — Extracted from PDF"
    t.font      = Font(name="Calibri", bold=True, size=16, color=HEADER_BG)
    t.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 36

    ws.merge_cells("A2:F2")
    s = ws["A2"]
    s.value     = (
        f"Total Jobs: {len(df)}   |   "
        f"With Email: {df['HR Email'].ne('').sum()}   |   "
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )
    s.font      = Font(name="Calibri", italic=True, size=10, color="7F7F7F")
    s.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 20
    ws.row_dimensions[3].height = 6

    # ── Summary sheet ─────────────────────────────────────────────────────
    ws2 = wb.create_sheet("Summary")
    summary = [
        ["Metric",                 "Value"],
        ["Total Jobs Extracted",   len(df)],
        ["Jobs with HR Email",     int(df["HR Email"].ne("").sum())],
        ["Jobs Missing Email",     int(df["HR Email"].eq("").sum())],
        ["Unique Companies",       int(df["Company Name"].nunique())],
        ["Unique Locations",       int(df["Location"].nunique())],
        ["PDF Source",             os.path.basename(output_path.replace(".xlsx",".pdf"))],
        ["Generated On",           datetime.now().strftime("%Y-%m-%d %H:%M")],
    ]
    for r, row_data in enumerate(summary, start=1):
        for c, val in enumerate(row_data, start=1):
            cell = ws2.cell(row=r, column=c, value=val)
            if r == 1:
                cell.font  = Font(name="Calibri", bold=True, color="FFFFFF")
                cell.fill  = HDR_FILL
            else:
                cell.font  = Font(name="Calibri", size=10)
                if r % 2 == 0:
                    cell.fill = ALT_FILL
            cell.border    = BORDER
            cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws2.column_dimensions["A"].width = 30
    ws2.column_dimensions["B"].width = 45
    ws2.row_dimensions[1].height = 26

    wb.save(output_path)
    log.info(f"✅ Excel saved → {output_path}  ({len(df)} jobs)")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN PIPELINE – ties all steps together
# ─────────────────────────────────────────────────────────────────────────────
def main(pdf_path: str, output_path: str) -> None:
    log.info("═" * 60)
    log.info("  PDF → EXCEL  JOB EXTRACTOR  |  Start")
    log.info("═" * 60)

    # 1 Extract
    raw_text = extract_text_from_pdf(pdf_path)

    # 2 Clean
    clean = clean_text(raw_text)

    # 3 Split
    blocks = split_jobs(clean)

    # 4 Parse
    log.info("Parsing job blocks...")
    jobs = []
    for idx, block in enumerate(blocks, start=1):
        job = parse_job_block(block, idx)
        if job["Company Name"]:          # skip empty / noise blocks
            jobs.append(job)

    log.info(f"Parsed {len(jobs)} valid jobs")

    # 5 Export
    write_to_excel(jobs, output_path)
    log.info("═" * 60)
    log.info("  DONE!  Open your Excel file to view results.")
    log.info("═" * 60)


# ─────────────────────────────────────────────────────────────────────────────
# CLI entry point  →  python pdf_to_excel_jobs.py jobs.pdf [output.xlsx]
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract QA job listings from a structured PDF into Excel."
    )
    parser.add_argument(
        "pdf",
        nargs="?",
        default="LATEST-QA-JOBS_16-APRIL-2026.pdf",
        help="Path to the input PDF file (default: LATEST-QA-JOBS_23-APRIL-2026.pdf)",
    )
    parser.add_argument(
        "-o", "--output",
        default=r"C:\Users\Arpita Malakar\Downloads\job\QA_Jobs_Extracted.xlsx",
        help="Path for the output Excel file (default: QA_Jobs_Extracted.xlsx)",
    )
    args = parser.parse_args()
    main(r"C:\Users\Arpita Malakar\Downloads\job\LATEST QA JOBS_23 APRIL 2026.pdf", args.output)
