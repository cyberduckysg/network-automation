import subprocess
import datetime

network = "192.162.99"

ip_address = []
total_up = 0
total_down = 0
up_devices = []
down_devices = []

for i in range(99, 110):
    ip_address = f"{network}.{i}"
    result = subprocess.run(["ping", "-c", "1", "-W", "0.5", ip_address ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time = datetime.datetime.now()
    t = (time.strftime("%H:%M:%S"))
    
    if result.returncode == 0  :
       
        up_devices.append(f"{t} - {ip_address}")     
        total_up += 1
    else:
        down_devices.append(f"{t} - {ip_address}")
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
    
    
