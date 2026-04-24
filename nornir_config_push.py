from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_netmiko.tasks import netmiko_send_config

nr = InitNornir(config_file="config.yaml")

ios = nr.filter(platform="cisco_ios")

def configure_link(task):
    interface = task.host["link_interface"]
    ip = task.host["link_ip"]
    mask = task.host["link_mask"]
    
    print(f"{task.host.name} → configuring {interface} with {ip}")
    commands = [f"interface {interface}", f"ip address {ip} {mask}", "no shut" ]
    task.run(task=netmiko_send_config, config_commands=commands)


def verify_link(task):
    commands = "show ip interface brief "
    result = task.run(task=netmiko_send_command, command_string=commands)
    print(f"=== {task.host.name} ===")
    print(result[0].result)


ios.run(task=configure_link)
ios.run(task=verify_link)
