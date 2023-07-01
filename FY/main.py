from pysnmp.hlapi import *

class SNMPInterfaceGetter:
    def __init__(self):
        self.target_ip = input("Enter target device IP address: ")
        self.community = input("Enter SNMP community string: ")

    def get_interface_ip_address(self, interface_index):
        snmp_community = CommunityData(self.community, mpModel=0)
        target = UdpTransportTarget((self.target_ip, 161))
        ip_address_oid = ObjectIdentity('IF-MIB', 'ifTable', 'ifEntry', 'ifIpAddress', interface_index)

        get_command = getCmd(
            snmp_community,
            target,
            ContextData(),
            ObjectType(ip_address_oid)
        )

        error_indication, error_status, error_index, var_binds = next(get_command)

        if error_indication:
            print(f'SNMP GET operation failed: {error_indication}')
        elif error_status:
            print(f'SNMP GET operation failed: {error_status.prettyPrint()}')
        else:
            for var_bind in var_binds:
                print(f'Interface IP Address: {var_bind[1].prettyPrint()}')

getter = SNMPInterfaceGetter()
interface_index = input("Enter interface index: ")
getter.get_interface_ip_address(interface_index)
