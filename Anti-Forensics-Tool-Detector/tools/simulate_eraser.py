#!/usr/bin/env python3
import os, time, platform

def simulate_eraser():
    print("[*] Simulating Eraser secure deletion...")
    file = os.path.expanduser("~/sensitive_data.txt")
    with open(file, "w") as f:
        f.write("This file contains secret data\n")
    time.sleep(2)
    if platform.system() == "Linux":
        os.system(f"shred -uz {file}")
    else:
        os.remove(file)
    print("[+] File securely deleted (simulated)")

if __name__ == "__main__":
    simulate_eraser()
