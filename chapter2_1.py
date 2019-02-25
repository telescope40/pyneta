import netmiko 

device = {
"device_type":"cisco_ios",
"host":"cisco1.lasthop.io",
"username":"pyclass",
"password":"88newclass",
"fast_cli":True
}

net_connect = netmiko.ConnectHandler(**device)
print(net_connect.find_prompt())

output = net_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
)

output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)

output += net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)

output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
net_connect.disconnect()

print()
print(output)
print()
