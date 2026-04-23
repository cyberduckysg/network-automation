from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import datetime
nr = InitNornir(config_file="config.yaml")

result = nr.run(
    task=netmiko_send_command,
    command_string="show version"
)
time = datetime.datetime.now()
t = time.strftime("%Y-%m-%d_%H-%M-%S")
print(result["CiscoIOSv-1"][0].result)
for hostname, task_result in result.items():
    with open(f"audit_results_{t}.txt", "a") as file:
        
        file.write(f"=== {hostname} === \n")
        file.write(task_result[0].result)    