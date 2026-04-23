
words = ["Hello", "World"]
print(" ".join(words))
name = "Anish"
print(name.isalpha())

'''
🎯 Task
Count errors
Extract only error messages
'''
logs = [
    "INFO: Login Success",
    "ERROR: Invalid Password",
    "ERROR: Timeout",
    "INFO: Logout"
]
def log_analyser(logs):
    count=0
    error_msg = []
    for log in logs:
        if "ERROR" in log:
            error_msg.append(log.split(":")[1].strip())
            count+=1
    return count, error_msg
print(log_analyser(logs))

import re

text = "Order ID: 12345, Amount: 678"
match = re.search(r"\d+",text)
numbers = re.findall(r"\d+",text)
print(match.group())
print(numbers)

"""
Build: 👉 “Smart Log Analyzer”
Features:
Count INFO, ERROR, WARNING
Extract all ERROR messages
Normalize logs (case + spaces)
Print report
"""

logs = [
    "INFO: User logged in",
    "ERROR: Failed to load page",
    "warning: Disk space low",
    "INFO:  File uploaded",
    "ERROR: Timeout occurred ",
    "Warning: CPU usage high"
]
def smart_log_analyzer(logs):
    count_info = 0
    count_error = 0
    count_warning = 0
    error_message = []
    warning_message = []
    normalize_log = []
    for log in logs:
        # cleaning & adding to normalizing log
        clean_log = log.strip().upper()
        normalize_log.append(clean_log)
        #counting info
        if log.upper().startswith("INFO"): # / "INFO" in log:
            count_info+=1
        #counting warning message & adding
        elif log.upper().startswith("WARNING") : # / "WARNING" in log.upper():
            count_warning +=1
            warning_message.append(log.upper().replace("WARNING: ","").strip())
        #counting Error message & adding
        elif log.upper().startswith("ERROR"): # / "ERROR" in log.upper
            count_error+=1
            error_message.append(log.upper().replace("ERROR: ","").strip())
    #printing clean report
    # add to report file
    with open("report.txt", "w") as file:
        file.write("LOG ANALYSIS REPORT\n")
        file.write("----------------------\n")
        file.write(f'INFO   : {count_info}\n')
        file.write(f'WARNING: {count_warning}\n')
        file.write(f'ERROR  : {count_error}\n')
        file.write("----------------------\n")
        file.write("Error Message\n")
        file.write("----------------------\n")
        for message in error_message:
            file.write(f'- {message}\n')
        file.write("----------------------\n")
        file.write("Warning Message\n")
        file.write("----------------------\n")
        for message in warning_message:
            file.write(f'- {message}\n')
        file.write("----------------------\n")
        file.write("Normalize log\n")
        file.write("----------------------\n")
        for log in normalize_log:
            file.write(f'{log}\n')


def smart_log_analyzer_(logs):
    info_count = 0
    error_count = 0
    warning_count = 0
    error_messages = []
    normalized_logs = []

    for log in logs:
        # ✅ Normalize (case + spaces)
        clean_log = log.strip().upper()
        # clean_log = re.sub(r"\s+", " ", clean_log)  # remove extra spaces
        normalized_logs.append(clean_log)

        # ✅ Count log levels
        if clean_log.startswith("INFO"):
            info_count += 1

        elif clean_log.startswith("ERROR"):
            error_count += 1

            # ✅ Extract ERROR message
            message = clean_log.replace("ERROR: ", "")
            error_messages.append(message)

        elif clean_log.startswith("WARNING"):
            warning_count += 1

    # ✅ Print Report
    print("\n📊 LOG ANALYSIS REPORT")
    print("-" * 30)
    print(f"INFO Count    : {info_count}")
    print(f"ERROR Count   : {error_count}")
    print(f"WARNING Count : {warning_count}")

    print("\n❌ ERROR Messages:")
    for msg in error_messages:
        print(f"- {msg}")

    print("\n🧹 Normalized Logs:")
    for log in normalized_logs:
        print(log)


# Run
smart_log_analyzer(logs)

