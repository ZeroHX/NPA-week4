from netmiko import ConnectHandler
device_ip = "172.31.174."
username = "admin"
password = "cisco"

## Assign loopback IP
# for ip_last in range(1, 10):
#     device_ip = device_ip + str(ip_last)
#     print(device_ip)
#     device_para = {'device_type': 'cisco_ios',
#                 'ip': device_ip,
#                 'username': username,
#                 'password': password
#                 }
#     with ConnectHandler(**device_para) as ssh:
#         loopback_ip = '172.20.174.' + str(ip_last) + ' 255.255.255.255'
#         commands = ['int loopback 0', 'ip address '+ loopback_ip]
#         result = ssh.send_config_set(commands)
#         print(result)
#         result = ssh.send_command('sh ip int br')
#         result = ssh.send_command('wri')
#         print(result)
    
#     device_ip = device_ip[:-1]

## Assign IP
# for ip_last in range(4,10):
#     device_ip = device_ip + str(ip_last)
#     print(device_ip)
#     if ip_last != 8:
#         print(device_ip)
#         device_para = {'device_type': 'cisco_ios',
#                     'ip': device_ip,
#                     'username': username,
#                     'password': password
#                     }
#         with ConnectHandler(**device_para) as ssh:
#             if ip_last < 8:
#                 router_file = 'config_ip/r%d.txt'%(ip_last-3)
#             else:
#                 router_file = 'config_ip/r%d.txt'%(ip_last-4)
#             result = ssh.send_config_from_file(router_file)
#             result = ssh.send_command('sh ip int br')
#             print(result)
#     device_ip = device_ip[:-1]


## Add ACL
# for ip_last in range(4,10):
#     device_ip = device_ip + str(ip_last)
#     print(device_ip)
#     if ip_last != 8:
#         print(device_ip)
#         device_para = {'device_type': 'cisco_ios',
#                     'ip': device_ip,
#                     'username': username,
#                     'password': password
#                     }
#         with ConnectHandler(**device_para) as ssh:
#             router_file = 'config_acl.txt'
#             result = ssh.send_config_from_file(router_file)
#             print(result)
#             ssh.save_config()
#     device_ip = device_ip[:-1]

## Add SSH
# for ip_last in range(1,10):
#     if ip_last not in [2,3,8]:
#         device_ip = device_ip + str(ip_last)
#         print(device_ip)
#         device_para = {'device_type': 'cisco_ios',
#                     'ip': device_ip,
#                     'username': username,
#                     'password': password
#                     }
#         with ConnectHandler(**device_para) as ssh:
#             router_file = 'config_ssh.txt'
#             result = ssh.send_config_from_file(router_file)
#             ssh.save_config()
#             print(result)
#         device_ip = device_ip[:-1]

## Add OSPF
for ip_last in range(4,10):
    device_ip = device_ip + str(ip_last)
    print(device_ip)
    if ip_last != 8:
        print(device_ip)
        device_para = {'device_type': 'cisco_ios',
                    'ip': device_ip,
                    'username': username,
                    'password': password
                    }
        with ConnectHandler(**device_para) as ssh:
            if ip_last < 8:
                router_file = 'config_ip/r%d.txt'%(ip_last-3)
            else:
                router_file = 'config_ip/r%d.txt'%(ip_last-4)
            result = ssh.send_config_from_file(router_file)
            result = ssh.send_command('sh ip int br')
            print(result)
    device_ip = device_ip[:-1]


    
