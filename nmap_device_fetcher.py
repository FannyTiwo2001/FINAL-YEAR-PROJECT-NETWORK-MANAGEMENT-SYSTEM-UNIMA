import nmap

def discover_devices(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')
    
    devices = []
    
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            device = {
                'ip': nm[host]['addresses']['ipv4'],
                'mac': nm[host]['addresses']['mac'],
                'vendor': nm[host]['vendor'].get(nm[host]['addresses']['mac'])
            }
            devices.append(device)
    
    return devices

# Specify your network IP address range
network = '192.168.56.0/24'

# Discover devices on the network
devices = discover_devices(network)

# Print the discovered devices
for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {device['vendor']}")
