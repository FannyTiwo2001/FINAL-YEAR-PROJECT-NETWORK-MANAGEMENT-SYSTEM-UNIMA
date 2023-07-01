from netmiko import ConnectHandler

# Define the device details
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',        # Replace with the router's IP address
    'username': 'your_username',  # Replace with your username
    'password': 'your_password',  # Replace with your password
}

# Establish an SSH connection to the device
net_connect = ConnectHandler(**device)


net_connect.enable()

# Configure OSPF on the device
ospf_config = [
    'router ospf 1',             # OSPF process ID
    'network 192.168.1.0 0.0.0.255 area 0',   # Replace with the network and subnet mask
    'network 192.168.2.0 0.0.0.255 area 0',   # Add more network statements as needed
    'network 192.168.3.0 0.0.0.255 area 0',
    'exit',
]

output = net_connect.send_config_set(ospf_config)

# Print the output
print(output)

# Close the SSH connection
net_connect.disconnect()
