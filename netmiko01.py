from netmiko import ConnectHandler
device_ip = "172.31.174."
username = "admin"
password = "cisco"

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

for ip_last in range(4,10):
    device_ip = device_ip + str(ip_last)
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
