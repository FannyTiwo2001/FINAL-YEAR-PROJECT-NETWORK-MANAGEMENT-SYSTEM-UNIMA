from easysnmp import Session
import easysnmp

# SNMP settings
router_ip = '41.70.47.102'  # Replace with the IP address of your Cisco router
community = 'router'  # Replace with the SNMP community string of your router

# Create an SNMP session
session = Session(hostname=router_ip, community=community, version=2)

# Temperature
def get_temperature():
    oid = '1.3.6.1.4.1.9.9.13.1.3.1.3.1006'  # Replace with the appropriate OID for temperature
    response = session.get(oid)
    temperature = response.value
    # Process the temperature value if necessary
    return temperature

# Uptime
def get_uptime():
    oid = '1.3.6.1.2.1.1.3.0'
    response = session.get(oid)
    uptime = response.value
    # Process the uptime value if necessary
    return uptime

# Memory Utilization
def get_memory_utilization():
    oid = '1.3.6.1.4.1.9.9.48.1.1.1.6.1'  # Replace with the appropriate OID for memory utilization
    response = session.get(oid)
    memory_utilization = response.value
    # Process the memory utilization value if necessary
    return memory_utilization

# CPU Utilization
def get_cpu_utilization():
    oid = '1.3.6.1.4.1.9.9.109.1.1.1.1.4.7'  # Replace with the appropriate OID for CPU utilization
    response = session.get(oid)
    cpu_utilization = response.value
    # Process the CPU utilization value if necessary
    return cpu_utilization

# Main function
def main():
    try:
        temperature = get_temperature()
        uptime = get_uptime()
        memory_utilization = get_memory_utilization()
        cpu_utilization = get_cpu_utilization()

        print('Temperature:', temperature)
        print('Uptime:', uptime)
        print('Memory Utilization:', memory_utilization)
        print('CPU Utilization:', cpu_utilization)
    except easysnmp.exceptions.EasySNMPTimeoutError:
        print("Failed to Connect to router: "+router_ip)


if __name__ == '__main__':
    main()
