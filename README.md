# 🧪 AFID – Anti-Forensic Intelligence Detector (v1.0)

> **By Mr Vasu Garg aka HashHammer** | Built & tested on **Kali Linux**

---

## 🚀 Introduction

Hey folks 👋

I built **AFID** as a personal toolkit to help detect **anti-forensics activities** like timestamp manipulation (timestomping), secure file deletion (via `shred`, `BleachBit`, etc.), log tampering, and file attribute forging — all in one scan.
---

## 🔧 Features

- 📁 Checks for missing files that may have been securely deleted
- 🕒 Analyzes **Access / Modify / Change** timestamps (for timestomping)
- 📜 Scans for traces of **shred**, **BleachBit**, etc.
- 🔍 Detects **log wiping or tampering patterns**
- 🔐 Generates **SHA-256 file hash** for integrity
- 🧷 Lists **extended attributes (xattr)** if present
- 📁 Saves a clean, structured JSON report in the `tools/` folder

---

## 💻 How to Run

```bash
# Step 1: Clone the repository
git clone https://github.com/yourusername/Anti-Forensics-Tool-Detector.git

# Step 2: Navigate into the project
cd Anti-Forensics-Tool-Detector/tools

# Step 3: Run with root privileges
sudo python3 AFID.py


Input Example

AFID will prompt you like this:

Enter full path of file to check timestomping: /home/kali/Desktop/rockyou.txt



Sample Output:

=== 🧪 AFID – Anti-Forensic Intelligence Detector (v1.0) ===

[🔍] File Checked: /home/kali/Desktop/rockyou.txt
    Access Time : 2025-05-19T17:01:49.360415
    Modify Time : 2023-01-15T08:30:00
    Change Time : 2025-05-19T17:01:51.600362
[+] Timestamps look normal.

[🔐] SHA-256 Hash: d41d8cd98f00b204e9800998ecf8427e

[📌] Extended Attributes (xattr):
    None

[🔍] Shred Tool Logs Found: No

[🚫] Secure Deletion Evidence:
    [!] File missing: /root/sensitive_data.txt
    [!] File missing: /root/bleachbit_temp_sim/tempfile_0.log

[⚠️ ] Log Integrity Status: Mismatch

📁 Report saved to: ./tools/AFID_Report_BEAST.json
=== ✅ AFID Scan Complete ===

