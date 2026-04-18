import json
import napalm
from napalm import get_network_driver

with open("napalm_devices.json", "r") as file:
    data = json.load(file)



for d in data["devices"]:

    driver =  get_network_driver(d["driver"])
    device = driver (d["host"], d["username"], d["password"] )
    device.open()
    facts = device.get_facts()
    print(facts)
    device.close()