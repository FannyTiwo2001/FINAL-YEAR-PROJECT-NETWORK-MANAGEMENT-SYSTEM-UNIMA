from easysnmp import Session

def get_all_interfaces(router_ip, community):
    # Create an SNMP session
    session = Session(hostname=router_ip, community=community, version=2)

    # OID for interface description (ifDescr)
    oid_ifDescr = '1.3.6.1.2.1.2.2.1.2'

    try:
        # Retrieve the interface descriptions
        response = session.walk(oid_ifDescr)

        # Extract the interface names from the response
        interfaces = [interface.value for interface in response]

        return interfaces
    except Exception as e:
        print("Error retrieving interfaces:", str(e))

# Example usage
router_ip = '41.70.47.57'  # Replace with the IP of your router
community = 'thom1'  # Replace with the SNMP community string

interfaces = get_all_interfaces(router_ip, community)

# Print the retrieved interfaces
for interface in interfaces:
    print(interface)
