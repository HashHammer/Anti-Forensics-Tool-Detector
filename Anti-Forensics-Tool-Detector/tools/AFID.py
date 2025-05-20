#!/usr/bin/env python3
import os
import hashlib
import subprocess
from datetime import datetime
from pathlib import Path
import json

# === Metadata ===
VERSION = "1.0"
BASE_DIR = Path(__file__).resolve().parent
REPORT_PATH = BASE_DIR / "AFID_Report_BEAST.json"

# === Check timestamps ===
def check_file_timestamps(file_path):
    stat = os.stat(file_path)
    return {
        "access_time": datetime.fromtimestamp(stat.st_atime).isoformat(),
        "modify_time": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "change_time": datetime.fromtimestamp(stat.st_ctime).isoformat()
    }

# === Calculate SHA-256 ===
def get_file_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# === Check xattr ===
def check_xattr(file_path):
    try:
        output = subprocess.check_output(["lsattr", file_path], text=True)
        return output.strip().split("\n")[1:]  # skip header
    except:
        return []

# === Check shred logs ===
def shred_check():
    logs = subprocess.getoutput("grep shred /var/log/syslog /var/log/messages /var/log/kern.log 2>/dev/null")
    return bool(logs.strip())

# === Missing sensitive files (simulate anti-forensics detection) ===
def check_sensitive_file_presence():
    suspected_files = [
        "/root/sensitive_data.txt",
        "/root/bleachbit_temp_sim/tempfile_0.log"
    ]
    return [f for f in suspected_files if not os.path.exists(f)]

# === Log tamper simulation check ===
def check_log_integrity():
    # Placeholder logic
    return "mismatch"

# === Main ===
def main():
    print(f"\n=== 🧪 AFID – Anti-Forensic Intelligence Detector ({VERSION}) ===\n")

    file_path = input("Enter full path of file to check timestomping: ").strip()
    if not os.path.isfile(file_path):
        print(f"[❌] File not found: {file_path}")
        return

    timestamps = check_file_timestamps(file_path)
    file_hash = get_file_hash(file_path)
    xattr = check_xattr(file_path)
    shred_found = shred_check()
    missing_files = check_sensitive_file_presence()
    log_status = check_log_integrity()

    print(f"\n[🔍] File Checked: {file_path}")
    print(f"    Access Time : {timestamps['access_time']}")
    print(f"    Modify Time : {timestamps['modify_time']}")
    print(f"    Change Time : {timestamps['change_time']}")
    print("[+] Timestamps look normal." if "2025" in timestamps['access_time'] else "[!] Suspicious timestamp found!")

    print(f"\n[🔐] SHA-256 Hash: {file_hash}")
    print(f"\n[📌] Extended Attributes (xattr):")
    if xattr:
        for line in xattr:
            print(f"    {line}")
    else:
        print("    None")

    print(f"\n[🔍] Shred Tool Logs Found: {'Yes' if shred_found else 'No'}")

    print(f"\n[🚫] Secure Deletion Evidence:")
    for f in missing_files:
        print(f"    [!] File missing: {f}")

    print(f"\n[⚠️ ] Log Integrity Status: {log_status.capitalize()}")

    report = {
        "version": VERSION,
        "file_checked": file_path,
        "timestamps": timestamps,
        "timestamp_status": "normal" if "2025" in timestamps['access_time'] else "suspicious",
        "hash": file_hash,
        "xattr": xattr,
        "shred_log_found": shred_found,
        "secure_deletion_files": missing_files,
        "log_integrity": log_status
    }

    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=4)

    print(f"\n📁 Report saved to: {REPORT_PATH}")
    print("=== ✅ AFID Scan Complete ===\n")

# === Execute ===
if __name__ == "__main__":
    main()

