import json
import netmiko
from netmiko import ConnectHandler
import napalm
from napalm import get_network_driver
import datetime

with open("napalm_devices.json", "r") as file:
    data = json.load(file)


for d in data["devices"]:

    driver =  get_network_driver(d["driver"])
    device = driver (d["host"], d["username"], d["password"] )
    try:
        device.open()
        facts = device.get_facts()
        if  facts["vendor"] == "Arista" :

            arista_netmiko = {
            "device_type": "arista_eos",
             "host": d["host"],
             "username": d["username"],
             "password": d["password"]
            }
            connection = ConnectHandler(**arista_netmiko)
            show_version = connection.send_command("show version ")
            time = datetime.datetime.now()
            t = time.strftime("%Y-%m-%d_%H-%M-%S")
            print(show_version)
            with open(f"audit_results_{t}.txt", "w") as file:
                file.write(show_version)             
        else:
            print(f"{facts['hostname']}")
        
      
    except Exception as e:
        print(f" Connection failed: {e}")
    finally:
        device.close()