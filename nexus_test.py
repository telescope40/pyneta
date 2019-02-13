

# Nexus Show Command Script 
_author_ ='ldevicto'


import netmiko
import time
import sys
import getpass

#nexus_file = open('nxc021_22_snapshot.txt', 'w')

template = {
    'device_type':'cisco_ios',
    'username':'pyclass',
    'password':'88newclass',
    'global_delay_factor': 1,

    }


commands = [ "show version","show module","show inventory","show vPC","show vPC role","show port-channel summary","show span sum","show vlan sum","show running-config","show ip int brief vrf all","show int status","show cdp nei","show trunk","show port-channel capacity",]
 
switches = ['cisco1.lasthop.io','cisco2.lasthop.io']

for i in switches:
    connection = netmiko.ConnectHandler(i ,**template)
    try:
        print (connection.find_prompt())
        for w in commands:
            print (connection.send_command(w))
            print (i + " Information Gathered")
            connection.disconnect()
    except:
        print (i +"Unable to Access")
        connection.disconnect()
#nexus_file.close()
