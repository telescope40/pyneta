from netmiko import ConnectHandler
from pprint import pprint

device1 = {
    "device_type":"cisco_ios",
    "host":"cisco1.lasthop.io",
    "username":"pyclass",
    "password":"88newclass",
    "fast_cli":True
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
output = net_connect.send_command("show ip arp",use_textfsm=True)
pprint(output)
net_connect.disconnect()
