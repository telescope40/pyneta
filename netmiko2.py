import netmiko 
import getpass


nxos1 = {
     "host" : "nxos1.lasthop.io",
     "username" : "pyclass",
     "password" :"88newclass",
     "device_type":"cisco_nxos",
     }
 
nxos2 = {
     "host":"nxos2.lasthop.io",
     "username":"pyclass",
     "password":"88newclass",
     "device_type":"cisco_nxos",
     }

list_o_devices = [nxos1, nxos2]
for i in list_o_devices:
        net_connect = netmiko.ConnectHandler(**i)
        print(net_connect.find_prompt())
