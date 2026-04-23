from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
import textfsm

nr = InitNornir(config_file="config.yaml")

result = nr.run(
    task=netmiko_send_command,
    command_string="show version"
)

for hostname, result_task in result.items():
    platform = nr.inventory.hosts[hostname].platform
    raw_output = result_task[0].result
    
    if platform == "cisco_ios":
        with open("cisco_ios_show_version.textfsm") as template:
            fsm = textfsm.TextFSM(template)
            parsed = fsm.ParseTextToDicts(raw_output)
            print(f"=== {hostname} ===")
            print(parsed[0]["HOSTNAME"],parsed[0]["UPTIME"] )
    elif platform == "cisco_nxos" :
        with open("cisco_nxos_show_version.textfsm") as template:
            fsm = textfsm.TextFSM(template)
            parsed = fsm.ParseTextToDicts(raw_output)
            print(f"=== {hostname} ===")
            print(parsed[0]["HOSTNAME"],parsed[0]["UPTIME"])

    elif platform == "arista_eos" :
        with open("arista_eos_show_version.textfsm") as template:
            fsm = textfsm.TextFSM(template)
            parsed = fsm.ParseTextToDicts(raw_output)
            print(f"=== {hostname} ===")
            print(hostname,parsed[0]["UPTIME"])
    
    else:
        print(f"=== {hostname} === (skipped, not Cisco IOS)")