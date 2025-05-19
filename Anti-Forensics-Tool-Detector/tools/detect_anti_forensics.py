#!/usr/bin/env python3
import os
import time
import platform
from datetime import datetime

def check_shred_traces():
    print("\n[🔍] Checking for 'shred' tool usage logs (Linux only)...")
    try:
        with open('/var/log/syslog', 'r') as log:
            lines = log.readlines()
            shred_logs = [line for line in lines if 'shred' in line]
            if shred_logs:
                print("[!] Potential 'shred' usage detected:")
                for line in shred_logs[-5:]:
                    print("    ", line.strip())
            else:
                print("[+] No 'shred' logs found.")
    except:
        print("[x] Cannot access syslog. Try running with sudo or unsupported OS.")

def detect_timestomp(file_path):
    print(f"\n[🔍] Checking file timestamp for: {file_path}")
    try:
        stat = os.stat(file_path)
        atime = datetime.fromtimestamp(stat.st_atime)
        mtime = datetime.fromtimestamp(stat.st_mtime)
        ctime = datetime.fromtimestamp(stat.st_ctime)

        print(f"    Access Time : {atime}")
        print(f"    Modify Time : {mtime}")
        print(f"    Change Time : {ctime}")

        suspicious_years = [2000, 2001, 1999]
        if any(t.year in suspicious_years for t in [atime, mtime, ctime]):
            print("[!] Suspicious timestamps detected — possible timestomping.")
        else:
            print("[+] Timestamps look normal.")
    except Exception as e:
        print("[x] Could not read timestamp:", e)

def detect_missing_files(paths):
    print("\n[🔍] Checking for missing files indicating secure deletion...")
    for path in paths:
        if not os.path.exists(path):
            print(f"[!] File missing: {path} — may have been securely deleted.")
        else:
            print(f"[+] File exists: {path}")

if __name__ == "__main__":
    print("=== 🧪 Anti-Forensics Tool Detection Started ===")
    
    # 1. Detect shred (Linux)
    if platform.system() == "Linux":
        check_shred_traces()

    # 2. Detect timestomping
    sample_file = os.path.expanduser("~/timestomped_file.txt")
    detect_timestomp(sample_file)

    # 3. Detect deleted file traces
    deleted_paths = [
        os.path.expanduser("~/sensitive_data.txt"),
        os.path.expanduser("~/bleachbit_temp_sim/tempfile_0.log")
    ]
    detect_missing_files(deleted_paths)
