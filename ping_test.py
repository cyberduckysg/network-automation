import subprocess
import datetime

devices = [
    "192.162.99.100",     # Google DNS  (should be UP)
    "192.162.99.101",     # Cloudflare  (should be UP)
    "192.162.99.102",   # Fake device (should be DOWN)
    "192.162.99.103",   # Fake device (should be DOWN)
]

total_up = 0
total_down = 0
up_devices = []
down_devices = []


for ip in devices:

    result = subprocess.run(["ping", "-c", "1", ip ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time = datetime.datetime.now()
    t = (time.strftime("%H:%M:%S"))
    
    if result.returncode == 0  :
       
        up_devices.append(f"{t} - {ip}")     
        total_up += 1
    else:
        down_devices.append(f"{t} - {ip}")
        total_down += 1

print("=== UP Devices ===")
for ip_up in up_devices:
 print (f"Host {ip_up} up")

print("=== DOWN Devices ===")
for ip_down in down_devices:
 print(f" Host {ip_down} down" )

print("=== Summary ===")

print (f"Total UP   :{total_up}") 

print (f"Total DOWN  :{total_down}") 