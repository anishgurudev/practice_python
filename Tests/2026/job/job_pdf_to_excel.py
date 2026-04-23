"""
📌 PROJECT: PDF Job Parser → Excel

This script reads a structured job listing PDF and extracts:
- Company Name
- Job Title
- Experience
- Skills
- HR Email

Then saves everything into an Excel file.

💡 Designed specifically for structured job PDFs (NOT generic PDFs)
"""

# -------------------------------
# 📦 IMPORT LIBRARIES
# -------------------------------

import pdfplumber   # Used to read PDF files (better than PyPDF2 for structured text)
import re           # Used for pattern matching (like finding email, fields)
import pandas as pd # Used to create Excel file (DataFrame)
import sys          # Used to take input from command line


# -------------------------------
# 📄 STEP 1: READ PDF FILE
# -------------------------------

def extract_text_from_pdf(pdf_path):
    """
    👉 PURPOSE:
    Read the PDF file and extract all text into one string.

    👉 INPUT:
    pdf_path (string) → path of your PDF file

    👉 OUTPUT:
    full_text (string) → entire content of PDF
    """

    try:
        full_text = ""  # This will store entire PDF text

        # Open PDF file
        with pdfplumber.open(r"C:\Users\Arpita Malakar\Downloads\job\LATEST QA JOBS_23 APRIL 2026.pdf") as pdf:
            # Loop through each page
            for page_number, page in enumerate(pdf.pages):

                # Extract text from page
                text = page.extract_text()

                # If page has text, add it
                if text:
                    full_text += text + "\n"

        # 🧹 CLEANING STEP
        # Replace multiple spaces/newlines with single space
        full_text = re.sub(r'\s+', ' ', full_text)

        return full_text

    except Exception as e:
        print(f"❌ Error while reading PDF: {e}")
        return ""


# -------------------------------
# ✂️ STEP 2: SPLIT INTO JOB BLOCKS
# -------------------------------

def split_jobs(full_text):
    """
    👉 PURPOSE:
    Split full PDF text into multiple job sections.

    👉 LOGIC:
    Every job starts with 'Company:'
    So we split based on this keyword.

    👉 OUTPUT:
    List of job blocks
    """

    try:
        # Split text wherever "Company:" appears
        split_data = re.split(r'Company\s*:', full_text)

        job_blocks = []

        for block in split_data:
            block = block.strip()

            # Ignore empty blocks
            if block:
                # Add back "Company:" because split removed it
                job_blocks.append("Company: " + block)

        return job_blocks

    except Exception as e:
        print(f"❌ Error while splitting jobs: {e}")
        return []


# -------------------------------
# 📧 STEP 3: EXTRACT EMAIL
# -------------------------------

def extract_email(text):
    """
    👉 PURPOSE:
    Find email ID inside job block

    👉 LOGIC:
    Use regex pattern for email

    👉 OUTPUT:
    Email string OR 'Not Found'
    """

    # Regex pattern for email
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    match = re.search(email_pattern, text)

    if match:
        return match.group(0)  # Return matched email
    else:
        return "Not Found"


# -------------------------------
# 🔍 STEP 4: PARSE EACH JOB BLOCK
# -------------------------------

def parse_job_block(job_text):
    """
    👉 PURPOSE:
    Extract all required fields from ONE job block

    👉 INPUT:
    job_text → text of one job

    👉 OUTPUT:
    Dictionary with job details
    """

    try:
        job_data = {}  # Store extracted fields

        # -------------------------------
        # 🏢 Extract Company Name
        # -------------------------------
        company_match = re.search(
            r'Company:\s*(.*?)\s*(Job Title:|Location:)',
            job_text
        )

        if company_match:
            job_data["Company Name"] = company_match.group(1).strip()
        else:
            job_data["Company Name"] = "Not Found"

        # -------------------------------
        # 💼 Extract Job Title
        # -------------------------------
        title_match = re.search(
            r'Job Title:\s*(.*?)\s*(Experience Required:|Location:)',
            job_text
        )

        if title_match:
            job_data["Job Title"] = title_match.group(1).strip()
        else:
            job_data["Job Title"] = "Not Found"

        # -------------------------------
        # 📅 Extract Experience
        # -------------------------------
        exp_match = re.search(
            r'Experience Required:\s*(.*?)\s*(Skills Required:|$)',
            job_text
        )

        if exp_match:
            job_data["Experience"] = exp_match.group(1).strip()
        else:
            job_data["Experience"] = "Not Found"

        # -------------------------------
        # 🧠 Extract Skills (Important)
        # -------------------------------
        skills_match = re.search(
            r'Skills Required:\s*(.*?)\s*(Interested candidates|$)',
            job_text
        )

        if skills_match:
            skills = skills_match.group(1).strip()

            # Normalize skills (remove extra spaces)
            skills = re.sub(r'\s*,\s*', ', ', skills)

            job_data["Skills"] = skills
        else:
            job_data["Skills"] = "Not Found"

        # -------------------------------
        # 📧 Extract Email
        # -------------------------------
        job_data["HR Email"] = extract_email(job_text)

        return job_data

    except Exception as e:
        print(f"❌ Error parsing job: {e}")
        return {}


# -------------------------------
# 📊 STEP 5: WRITE TO EXCEL
# -------------------------------

def write_to_excel(all_jobs, output_file="job_output.xlsx"):
    """
    👉 PURPOSE:
    Convert list of job data into Excel file

    👉 INPUT:
    all_jobs → list of dictionaries
    """

    try:
        # Convert list → DataFrame
        df = pd.DataFrame(all_jobs)

        # Remove duplicate rows
        df.drop_duplicates(inplace=True)

        # Write to Excel
        df.to_excel(output_file, index=False)

        print(f"\n✅ Excel file created: {output_file}")

    except Exception as e:
        print(f"❌ Error writing Excel: {e}")


# -------------------------------
# 🚀 MAIN FUNCTION (ENTRY POINT)
# -------------------------------

def main(pdf_path):
    """
    👉 PURPOSE:
    Control entire flow of program
    """

    print("📄 Step 1: Reading PDF...")
    text = extract_text_from_pdf(pdf_path)

    if not text:
        print("❌ No text found in PDF")
        return

    print("✂️ Step 2: Splitting jobs...")
    job_blocks = split_jobs(text)

    print(f"📦 Total jobs found: {len(job_blocks)}")

    all_jobs = []

    # Loop through each job
    for index, job in enumerate(job_blocks, start=1):

        print(f"🔍 Processing Job {index}")

        parsed_job = parse_job_block(job)

        if parsed_job:
            all_jobs.append(parsed_job)

    print("📊 Step 3: Writing to Excel...")
    write_to_excel(all_jobs)


# -------------------------------
# ▶️ RUN SCRIPT FROM TERMINAL
# -------------------------------

if __name__ == "__main__":
    """
    👉 How to run:
    python script.py jobs.pdf
    """

    if len(sys.argv) < 2:
        print("❗ Please provide PDF path")
        print("Example: python script.py jobs.pdf")
    else:
        pdf_file_path = sys.argv[1]
        main(pdf_file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # fallback for local testing
        pdf_file_path = r"C:\Users\Arpita Malakar\Downloads\job\LATEST QA JOBS_23 APRIL 2026.pdf"
        print("⚠️ No argument passed, using default file")
    else:
        pdf_file_path = sys.argv[1]

    main(pdf_file_path)