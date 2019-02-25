import yaml
import netmiko

filename = input("Enter Filename")

with open(filename) as f:
    yaml_out = yaml.load(f)
    
    for keys in yaml_out:
        net_connect = netmiko.ConnectHandler()
        net_connect(**keys)
        print (net_connect.prompt())
    

print(yaml_out)
