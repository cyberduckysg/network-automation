import subprocess
import platform

devices = [
    "8.8.8.8",     # Google DNS  (should be UP)
    "1.1.1.1",     # Cloudflare  (should be UP)
    "192.168.1.254",   # Fake device (should be DOWN)
    "10.0.0.99",   # Fake device (should be DOWN)
]

flag = "-n" if platform.system() == "Windows" else "-c"
result = subprocess.run(["ping", flag, "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("\n=== Continuous Monitor — Press Ctrl+C to stop ===")
print("=== Reachability Check ===")
for ip in devices:
    if  ip:
        print(f" {ip}" Up)
    else:
        print(f" {ip} Down")

print("Scan Complete... ")

