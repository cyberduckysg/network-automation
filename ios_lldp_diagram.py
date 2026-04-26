from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_netmiko.tasks import netmiko_send_config
from pyvis.network import Network

nr = InitNornir(config_file="config.yaml")

ios = nr.filter(platform="cisco_ios")

net = Network()
def lldp_find(task):
    interface = task.host["link_interface"]
    print(f"{task.host.name} → show lldp neighbors  {interface} detail ")
    commands = f"show lldp neighbors {interface} detail "
    result = task.run(
        task=netmiko_send_command, 
        command_string=commands,
        use_textfsm=True,
        textfsm_template="cisco_ios_show_lldp_detail.textfsm"
     )
    
    print(f"=== {task.host.name} ===")
    print(result[0].result)


result = ios.run(task=lldp_find)

for hostname, r in result.items():
    neighbor = r[1].result[0]["sys_name"].split(".")[0]
    port = r[1].result[0]["local_intf"]
    net.add_node(hostname)
    net.add_node(neighbor)
    net.add_edge(hostname, neighbor, label=port)

net.show("network_diagram.html", notebook=False)
