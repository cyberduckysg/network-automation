
core_routers = [

    "1.1.1.1", # core router 1
    "1.1.1.2", # core router 2
    "1.1.1.3", # core router 3

]


severs = [

    "100.100.100.1", # server 1
    "100.100.100.2", # server 2
    "100.100.100.3", # server 3
    "100.100.100.4", # server 4

]

print("=== Core routing Layer ===")
for ip in core_routers:
    print(f"  Checking Router: {ip}")

print("=== server Layer ===")
for ip in severs:
    print(f"  Checking Servers:  {ip}")

print("Scan complete.")