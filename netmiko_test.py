import netmiko
from netmiko import ConnectHandler
devices =[

 {
    "device_type": "cisco_ios",     # what kind of device
    "host": "192.162.99.100",            # IP address
    "username": "admin",        # login
    "password": "cisco123",        # password
},

 {
    "device_type": "cisco_ios",     # what kind of device
    "host": "192.162.99.101",            # IP address
    "username": "admin",        # login
    "password": "cisco123",        # password
},

 {
    "device_type": "cisco_nxos",     # what kind of device
    "host": "192.162.99.102",            # IP address
    "username": "admin",        # login
    "password": "cisco123",        # password
},
 {
    "device_type": "arista_eos",     # what kind of device
    "host": "192.162.99.103",            # IP address
    "username": "admin",            # login
    "password": "cisco123",        # password
}



]

for device in devices :
    connection = ConnectHandler(**device)

    show_version = connection.send_command("show version ")

    print(show_version)