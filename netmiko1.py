import netmiko
cisco3 = {
  'host':'cisco3.lasthop.io',
  'username': 'pyclass',
  'password':'88newclass',
  'device_type':'cisco_ios',
}

net_connect = netmiko.ConnectHandler(**cisco3)
print(net_connect.find_prompt())
