
def scan_devices(device_list):
    for device in device_list:
        print(f"Scanning: {device}")


my_devices = ["CiscoIOSv-1", "CiscoIOSv-2", "AristaEOS-1", "CiscoNX-OSv-1"]

scan_devices(my_devices)