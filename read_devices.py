import json
import netmiko
from netmiko import ConnectHandler

with open("devices.json", "r") as file:
    data = json.load(file)


for ip in data["devices"]:

    try:
      
        connection = ConnectHandler(**ip)
        show_version = connection.send_command("show version ", use_textfsm=True)
        parsed = show_version[0]
        version = parsed.get("version") or parsed.get("os") or parsed.get("image")
        hostname = parsed.get("hostname") or parsed.get("model") or ip['host']
        print(f"{hostname} → {version}")
    
    except Exception as e :
        print(f"Failed to connect to {ip['host']} - {e}")


