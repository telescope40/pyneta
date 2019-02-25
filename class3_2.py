import yaml
from pprint import pprint

cisco3 = {"device_name":"cisco3","host":"cisco3.lasthop.io"}

cisco4 = {"device_name":"cisco4","host":"cisco4.lasthop.io"}

arista1 = {"device_name":"arista1","host":"arista1.lasthop.io"}

arista2 =  {"device_name":"arista2","host":"arista2.lasthop.io"}

mydevices = [cisco3, cisco4, arista1, arista2]

for device in mydevices:
    device["username"] = 'admin'
    device["password"] = 'admin'

print()
pprint(my_devices)
print()

with open("my_devices.yml", "w") as file:
    yaml.dump(my_devices, file, default_flow_style=False)
