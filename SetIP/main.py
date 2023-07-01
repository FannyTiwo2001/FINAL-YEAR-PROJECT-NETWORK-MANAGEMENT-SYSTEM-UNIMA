from pysnmp.hlapi import *

def set_interface_ip_address():
    community = input("Enter SNMP community string: ")
    target_ip = input("Enter target device IP address: ")
    target = UdpTransportTarget((target_ip, 161))
    interface_index = input("Enter interface index: ")
    new_ip_address = input("Enter new IP address to set: ")

    snmp_community = CommunityData(community, mpModel=0)
    ip_address_oid = ObjectIdentity('IF-MIB', 'ifTable', 'ifEntry', 'ifIpAddress', interface_index)
    set_command = setCmd(snmp_community, target, ContextData(), ObjectType(ip_address_oid, new_ip_address))

    error_indication, error_status, error_index, var_binds = next(set_command)

    if error_indication:
        print(f'SNMP SET operation failed: {error_indication}')
    elif error_status:
        print(f'SNMP SET operation failed: {error_status.prettyPrint()}')
    else:
        print('Interface IP address set successfully.')

set_interface_ip_address()

