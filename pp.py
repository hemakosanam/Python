from netmiko import ConnectHandler

CSR={
    "device_type":"Cisco_ios",
    "ip":"sandbox-iosxe-latest-l,cisco.com",
    "username":"developer",
    "password":"C1sco12345"
 }

net_connect=ConnectHandler(**CSR)

output=net_connect.send_command('show ip int brief')

print(output)
output_clock=net_connect.send_command('show clock')
print(output_clock)
