import netmiko
import re
cisco3 = {
  'host':'cisco3.lasthop.io',
  'username': 'pyclass',
  'password':'88newclass',
  'device_type':'cisco_ios',
}

net_connect = netmiko.ConnectHandler(**cisco3)
arp_data = (net_connect.send_command("Show ip arp", use_textfsm=True))


arp_data = arp_data.strip()
arp_list = arp_data.splitlines()

processed_list = []

for arp_entry in arp_list:
    if re.search(r"^Protocol.*Interface", arp_entry):
        continue
    _, ip_addr, _, mac_addr, _, intf = arp_entry.split()
    arp_dict = {"mac_addr": mac_addr, "ip_addr":ip_addr, "interface":intf}
    processed_list.append(arp_dict)

print()
print(processed_list)
print()

net_connect.disconnect()
