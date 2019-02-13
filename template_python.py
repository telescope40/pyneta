# usr/bin/bash
_author_="ldevicto"
import netmiko
import getpass
import sys

password = "88newclass"
host = (sys.argv[1])


device = {
"device_type":"cisco_nxos",
"host":host,
"username":"pyclass",
"password":password,
}

net_connect = netmiko.ConnectHandler(**device)
print(net_connect.find_prompt())
