from easysnmp import Session

# Define the SNMP parameters
target_ip = '41.70.47.57'
community = 'thom1'  # Replace with your SNMP community string

# Create an SNMP session
session = Session(hostname=target_ip, community=community, version=2)

# Retrieve the IP address and interface description information for each interface
interfaces = session.walk('1.3.6.1.2.1.4.20.1.1')  # OID for IP Address Table

# Iterate over the interfaces and print the IP address and interface description
for interface in interfaces:
    ip_address = interface.value

    # Retrieve interface description
    interface_description = session.get('.1.3.6.1.2.1.2.2.1.2'+'.'+str(if_index)).value

    print("IP Address: {}, Interface Description: {}".format(ip_address, interface_description))

def get_interface_index(self,interface_name):
        if_desc_oid = '1.3.6.1.2.1.2.2.1.2'
        interfaces = self.session.walk(if_desc_oid)

        for interface in interfaces:
            if interface.value == interface_name:
                return int(interface.oid_index)

        return None
