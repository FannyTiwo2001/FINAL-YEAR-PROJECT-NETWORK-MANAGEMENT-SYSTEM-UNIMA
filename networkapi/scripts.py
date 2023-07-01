from easysnmp import Session
import easysnmp
class router_script():
    def __init__(self,ip,community):
        self.router_ip = ip
        self.community = community
        self.session = Session(hostname=self.router_ip, community=self.community, version=2)

    # Temperature
    def get_temperature(self):
        oid = '1.3.6.1.4.1.9.9.13.1.3.1.3'  # Replace with the appropriate OID for temperature
        response = self.session.get(oid)
        temperature = response.value
        # Process the temperature value if necessary
        return temperature

    # Uptime
    def get_uptime(self):
        oid = '1.3.6.1.2.1.1.3.0'
        response = self.session.get(oid)
        uptime = response.value
        # Process the uptime value if necessary
        return uptime

    # Memory Utilization
    def get_memory_utilization(self):
        oid = '1.3.6.1.4.1.9.9.48.1.1.1.6.1'  # Replace with the appropriate OID for memory utilization
        response = self.session.get(oid)
        memory_utilization = response.value
        # Process the memory utilization value if necessary
        return memory_utilization

    # CPU Utilization
    def get_cpu_utilization(self):
        oid = '1.3.6.1.4.1.9.9.109.1.1.1.1.8'  # Replace with the appropriate OID for CPU utilization
        response = self.session.get(oid)
        cpu_utilization = response.value
        # Process the CPU utilization value if necessary
        return cpu_utilization
    def get_all_interfaces(self):

        # OID for interface description (ifDescr)
        oid_ifDescr = '1.3.6.1.2.1.2.2.1.2'

        try:
            # Retrieve the interface descriptions
            response = self.session.walk(oid_ifDescr)

            # Extract the interface names from the response
            interfaces = [interface.value for interface in response]

            return interfaces
        except Exception as e:
            print("Error retrieving interfaces:", str(e))
        
    def get_router_name(self):
            result = self.session.get('1.3.6.1.2.1.1.5.0')
            if result is not None:
                return result.value
            else:
                return None


    def start_monitoring(self):
        try:
            temperature = self.get_temperature()
            uptime = self.get_uptime()
            memory_utilization = self.get_memory_utilization()
            cpu_utilization = self.get_cpu_utilization()
            interface_list = self.get_all_interfaces()
            name = self.get_router_name()
            return {
                'Temp':temperature,
                'uptime': uptime,
                'memory': memory_utilization,
                'cpu':cpu_utilization,
                'interface_list': interface_list,
                'name':name
            }
        except easysnmp.exceptions.EasySNMPTimeoutError:
            print("Failed to Connect to router: "+self.router_ip)
            return {'Error':'Connection Failed'}

#Interface Script
class interface_script():
    
    def __init__(self,ip,index,community='thom1'):
        
        OID_BASE = '.1.3.6.1.2.1'
        # OIDs for each attribute
        self.OID_IP_ADDRESS = OID_BASE + '.4.20.1.1.1.2'
        self.OID_INTERFACE_STATE = OID_BASE + '.2.2.1.8'
        self.OID_INTERFACE_SPEED = OID_BASE + '.2.2.1.5'
        self.OID_INTERFACE_TYPE = OID_BASE + '.2.2.1.3'
        self.OID_INTERFACE_DESCRIPTION = OID_BASE + '.2.2.1.2'
        self.OID_INTERFACE_MAC = OID_BASE + '.2.2.1.6'
        self.OID_INPUT_PACKETS = OID_BASE + '.2.2.1.10'
        self.OID_OUTPUT_PACKETS = OID_BASE + '.2.2.1.16'
        self.OID_INPUT_ERRORS = OID_BASE + '.2.2.1.14'
        self.OID_OUTPUT_ERRORS = OID_BASE + '.2.2.1.20'
        self.router_ip = ip
        self.community = community
        self.session = Session(hostname=self.router_ip, community=self.community, version=2)
        self.all_interfaces_ip_list=[]
        self.compute_ip_address()
        self.interface_index =index#self.get_interface_index(interface_name)

    def get_interface_ip(self):
        
        return self.all_interfaces_ip_list[self.interface_index]

    def get_interface_state(self):
        state_oid = self.OID_INTERFACE_STATE + '.' + str(self.interface_index)
        return self.session.get(state_oid).value

    def get_interface_speed(self):
        speed_oid = self.OID_INTERFACE_SPEED + '.' + str(self.interface_index)
        return self.session.get(speed_oid).value

    def get_interface_type(self):
        type_oid = self.OID_INTERFACE_TYPE + '.' + str(self.interface_index)
        return self.session.get(type_oid).value

    def get_interface_description(self):
        description_oid = self.OID_INTERFACE_DESCRIPTION + '.' + str(self.interface_index)
        return self.session.get(description_oid).value

    def get_interface_mac(self):
        mac_address_oid = self.OID_INTERFACE_MAC + '.' + str(self.interface_index)
        return self.session.get(mac_address_oid).value

    def get_interface_input_packets(self):
        input_packets_oid = self.OID_INPUT_PACKETS + '.' + str(self.interface_index)
        return self.session.get(input_packets_oid).value

    def get_interface_output_packets(self):
        output_packets_oid = self.OID_OUTPUT_PACKETS + '.' + str(self.interface_index)
        return self.session.get(output_packets_oid).value
    
    def get_interface_input_errors(self):
        input_errors_oid = self.OID_INPUT_ERRORS + '.' + str(self.interface_index)
        return self.session.get(input_errors_oid).value

    def get_interface_output_errors(self):
        output_errors_oid = self.OID_OUTPUT_ERRORS + '.' + str(self.interface_index)
        return self.session.get(output_errors_oid).value

    
    def compute_ip_address(self):
        interfaces = self.session.walk('1.3.6.1.2.1.4.20.1.1')
        for interface in interfaces:
            ip_address = interface.value
            self.all_interfaces_ip_list.append(ip_address)


    def get_interface_attributes(self):
        
        interface_attributes = {
            'IP': self.get_interface_ip(self.session),
            'State': self.get_interface_state(self.session),
            'Speed': self.get_interface_speed(self.session),
            'Type': self.get_interface_type(self.session),
            'Description': self.get_interface_description(self.session),
            'MAC Address': self.get_interface_mac(self.session),
            'Input Packets': self.get_interface_input_packets(self.session),
            'Output Packets': self.get_interface_output_packets(self.session),
            'Input Errors': self.get_interface_input_errors(self.session),
            'Output Errors': self.get_interface_output_errors(self.session)
        }

        return interface_attributes

class switch_script():
    def __init__(self,ip,community):
        self.switch_ip = ip
        self.community = community
        self.session = Session(hostname=self.switch_ip, community=self.community, version=2)


    def get_temperature(self):
        temperature_oid = '1.3.6.1.4.1.9.9.13.1.3.1.3.1006'  # Cisco environmental monitoring temperature OID
        temperature_value = self.session.get(temperature_oid).value
        return temperature_value

    def get_uptime(self):
        uptime_oid = '1.3.6.1.2.1.1.3.0'  # SNMPv2-MIB sysUpTime OID
        uptime_ticks = int(self.session.get(uptime_oid).value)
        uptime_seconds = uptime_ticks / 100  # Convert uptime from 100ths of a second to seconds
        return uptime_seconds

    def get_memory_utilization(self):
        memory_util_oid = '1.3.6.1.4.1.9.9.48.1.1.1.6.1'  # Cisco memory pool utilization OID
        memory_utilization = self.session.get(memory_util_oid).value
        return memory_utilization
    def get_switch_attributes(self):
        switch_attributes={
            'uptime':self.get_uptime(),
            'memory_utelization':self.get_memory_utilization(),
            'temperature':self.get_temperature()
        }

class port_script():
    def __init__(self,ip,community,port_index):
        self.switch_ip = ip
        self.port_index=port_index
        self.community = community
        self.session = Session(hostname=self.switch_ip, community=self.community, version=2)
    def get_port_status(self, port_index):
        port_status_oid = f'1.3.6.1.2.1.2.2.1.8.{port_index}'  # IF-MIB ifOperStatus OID
        port_status = self.session.get(port_status_oid).value
        return port_status

    def get_port_speed(self):
        port_speed_oid = f'1.3.6.1.2.1.2.2.1.5.{self.port_index}'  # IF-MIB ifSpeed OID
        port_speed = self.session.get(port_speed_oid).value
        return port_speed

    def get_input_packet_count(self):
        input_packet_count_oid = f'1.3.6.1.2.1.2.2.1.11.{self.port_index}'  # IF-MIB ifInOctets OID
        input_packet_count = self.session.get(input_packet_count_oid).value
        return input_packet_count

    def get_output_packet_count(self):
        output_packet_count_oid = f'1.3.6.1.2.1.2.2.1.17.{self.port_index}'  # IF-MIB ifOutOctets OID
        output_packet_count = self.session.get(output_packet_count_oid).value
        return output_packet_count

    def get_input_error_count(self):
        input_error_count_oid = f'1.3.6.1.2.1.2.2.1.14.{self.port_index}'  # IF-MIB ifInErrors OID
        input_error_count = self.session.get(input_error_count_oid).value
        return input_error_count

    def get_output_error_count(self):
        output_error_count_oid = f'1.3.6.1.2.1.2.2.1.20.{self.port_index}'  # IF-MIB ifOutErrors OID
        output_error_count = self.session.get(output_error_count_oid).value
        return output_error_count

    def get_vlan_id(self):
        vlan_id_oid = f'1.3.6.1.4.1.9.9.68.1.2.2.1.2.{self.port_index}'  # CISCO-VTP-MIB vtpVlanEditTable vtpVlanEditEntry vtpVlanEditVlanIndex OID
        vlan_id = self.session.get(vlan_id_oid).value
        return vlan_id

    def get_trunk_setting(self):
        trunk_setting_oid = f'1.3.6.1.4.1.9.9.46.1.6.1.1.14.{self.port_index}'  # CISCO-STACK-MIB portChannelTable portChannelEntry portChannelAdminPortEncap OID
        trunk_setting = self.session.get(trunk_setting_oid).value
        return trunk_setting

    def get_duplex_setting(self):
        duplex_setting_oid = f'1.3.6.1.2.1.10.7.2.1.19.{self.port_index}'  # EtherLike-MIB dot3StatsDuplexStatus OID
        duplex_setting = self.session.get(duplex_setting_oid).value
        return duplex_setting
    
    def get_port_attributes(self):
        port_attributes={
            'status':self.get_port_status(),
            'speed':self.get_port_speed(),
            'input_packets':self.get_input_packet_count(),
            'output_packets':self.get_output_packet_count(),
            'input_error':self.get_input_error_count(),
            'output_error':self.get_output_error_count(),
            'vlan_id':self.get_vlan_id(),
            'trunk_setting':self.get_trunk_setting(),
            'duplex_setting':self.get_duplex_setting()
        }
