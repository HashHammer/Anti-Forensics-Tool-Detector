#!/usr/bin/env python3
import os, time

def simulate_timestomp():
    print("[*] Simulating Timestomp...")
    file = os.path.expanduser("~/timestomped_file.txt")
    with open(file, "w") as f:
        f.write("Normal file before timestomp\n")
    fake_time = time.mktime(time.strptime("01 Jan 2001", "%d %b %Y"))
    os.utime(file, (fake_time, fake_time))
    print(f"[+] Modified timestamps to: 01 Jan 2001")

if __name__ == "__main__":
    simulate_timestomp()
