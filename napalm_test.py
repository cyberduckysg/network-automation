import json
import napalm
from napalm import get_network_driver

driver = get_network_driver("ios")
device = driver("192.162.99.100", "admin", "cisco123")
device.open()
facts = device.get_facts()
print(facts)
device.close()

