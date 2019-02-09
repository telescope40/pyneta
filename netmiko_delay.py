import netmiko
import getpass

cisco3 = {
  'host':'cisco3.lasthop.io',
  'username': 'pyclass',
  'password':getpass(),
  'device_type':'cisco_ios',
}

net_connect = netmiko.ConnectHandler(**cisco3)
print(net_connect.find_prompt())

command = 'delete mytest'
net_connect.send_command(command, expect_string=r'?',
                            strip_prompt=False, strip_command=False)
output = net_connect.send_command('y', expect_string=r'#',
                            strip_prompt=False, strip_command=False)
print(output)
