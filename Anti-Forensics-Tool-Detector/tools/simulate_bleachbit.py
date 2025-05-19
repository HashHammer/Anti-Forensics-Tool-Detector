#!/usr/bin/env python3
import os, platform, time

def simulate_bleachbit():
    print("[*] Simulating BleachBit wiping...")
    temp_dir = os.path.expanduser("~/bleachbit_temp_sim")
    os.makedirs(temp_dir, exist_ok=True)
    for i in range(5):
        with open(os.path.join(temp_dir, f"tempfile_{i}.log"), "w") as f:
            f.write("Sensitive data that should be wiped\n")
    print(f"[+] Created dummy files in {temp_dir}")
    time.sleep(2)
    if platform.system() == "Linux":
        for file in os.listdir(temp_dir):
            os.system(f"shred -uz {os.path.join(temp_dir, file)}")
    else:
        for file in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, file))
    print("[+] Wiping simulation complete.")

if __name__ == "__main__":
    simulate_bleachbit()
