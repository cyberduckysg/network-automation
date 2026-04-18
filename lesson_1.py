device1 = "192.168.1.1"
device2 = "192.168.1.2"
device3 = "192.168.1.3"

# A list of  network devices.

devices = [ 

    "192.168.1.1",  # Spine-01
    "192.168.1.2",  # Spine-02
    "192.168.1.3",  # Leaf-01
    "192.168.1.4",  # Leaf-02
    "192.168.1.5",  # Mgmt switch
]

for ip in devices: 
    print(ip)