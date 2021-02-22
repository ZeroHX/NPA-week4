from netmiko import ConnectHandler

username = "admin"
password = "cisco"
device_dict = {'r0': '172.31.174.1', 's0':'172.31.174.2', 's1':'172.31.174.3', 'r1':'172.31.174.4',
'r2':'172.31.174.5', 'r3':'172.31.174.6', 'r4':'172.31.174.7', 's2':'172.31.174.8', 'r5':'172.31.174.9'}
for device in device_dict:
    device_para = {'device_type': 'cisco_ios',
                'ip': device_dict[device],
                'username': username,
                'password': password
                }
    with ConnectHandler(**device_para) as ssh:
        print("Configuring %s..."%device)
        ssh.send_config_from_file('config_ip/%s.txt'%(device))

        #Configure ssh on all devices.
        ssh.send_config_from_file('config_ssh.txt')

        #Configure acl in control plane.
        if device[0].lower() == 'r' and device != 'r0':
            ssh.send_config_from_file('config_acl.txt')

        cdp_result = ssh.send_command('show cdp nei')
        lst = cdp_result.splitlines()
        for line in lst:
            lst2 = line.split(' '*7)
            if 'npa.com' in line:
                device2 = lst2[0].strip()[:2]
                int1 = lst2[1].strip()
                int2 = lst2[-1].strip()
                command = ['int %s'%int1, 'description connect to %s of %s'%(int2,device2)]
                ssh.send_config_set(command)
        ssh.save_config()
