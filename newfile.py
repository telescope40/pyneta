import netmiko
cisco3 = {
  'host':'cisco3.lasthop.io',
  'username': 'pyclass',
  'password':'88newclass',
  'device_type':'cisco_ios',
}

net_connect = netmiko.ConnectHandler(**cisco3)
output = (net_connect.send_command("Show ip arp", use_textfsm=True))
print(output)

net_connect.disconnect()
