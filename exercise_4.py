def get_device_info(hostname,ip):
    return f"{hostname} - {ip}"


hosts = [
   
{"hostname": "CiscoIOSv-1", "ip":"192.162.99.100" },
{"hostname": "CiscoIOSv-2", "ip":"192.162.99.101" },
{"hostname": "CiscoNX-OSv-1", "ip":"192.162.99.102" },
{"hostname": "AristaEOS-1", "ip":"192.162.99.103" }

]

for device in hosts:
    print(device)
    info = get_device_info(device["hostname"], device["ip"])
    print(info)