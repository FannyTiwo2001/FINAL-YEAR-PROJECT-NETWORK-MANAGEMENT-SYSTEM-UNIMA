from pysnmp import *
from pysnmp.hlapi import *
from get_bulk import get_bulk
from set import set_value

class Router:
    def __init__(self, community, router_ip):
        self.community = community
        self.router_ip = router_ip
        self.arp_cache = {}

    def get_stats(self):
        stats = []   
        interface_status = {}
        interface_op_status = {}
        ram_used = {}
        ram = {}
        cpu = {}
        in_octects = {}
        out_octects = {}
        interface_speed = {}
        interface_in = {}
        interface_out = {}
        interface_speed = {}
        hostname = {}
        #arp_cache = {}
        #get up time
        #get access control rules

        interface_object_types = [ObjectType(ObjectIdentity('IF-MIB', 'ifDescr'))]
        interface_result = get_bulk(target = self.router_ip, object_types = interface_object_types, community = CommunityData(self.community), count = 2)

        interface_status_object_types = [ObjectType(ObjectIdentity('IF-MIB', 'ifAdminStatus'))]
        interface_status_result = get_bulk(target = self.router_ip, object_types = interface_status_object_types, community = CommunityData(self.community), count = 2)

        interface_op_status_object_types = [ObjectType(ObjectIdentity('IF-MIB', 'ifOperStatus'))]
        interface_operational_status_result = get_bulk(target = self.router_ip, object_types = interface_op_status_object_types, community = CommunityData(self.community), count = 2)
       
        j = 0
        k = 0

        for interface in interface_result:
            interface_status[interface] = interface_status_result[j]
            interface_op_status[interface] = interface_operational_status_result[j] 
            j = j + 1
        stats.append(interface_status)
        stats.append(interface_op_status)  

        interface_in_octects_object_types = [ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets'))]
        interface_in_octects_result = get_bulk(target = self.router_ip, object_types = interface_in_octects_object_types, community = CommunityData(self.community), count = 2)

        l = 0

        for interface in interface_result:
            interface_in[interface] = interface_in_octects_result[l] 
            l = l + 1
        stats.append(interface_in)

        interface_out_octects_object_types = [ObjectType(ObjectIdentity('IF-MIB', 'ifOutOctets'))]
        interface_out_octects_result = get_bulk(target = self.router_ip, object_types = interface_out_octects_object_types, community = CommunityData(self.community), count = 2)

        m = 0

        for interface in interface_result:
            interface_out[interface] = interface_out_octects_result[m] 
            m = m + 1
        stats.append(interface_out)

        interface_speed_object_types = [ObjectType(ObjectIdentity('IF-MIB', 'ifSpeed'))]
        interface_speed_result = get_bulk(target = self.router_ip, object_types = interface_speed_object_types, community = CommunityData(self.community), count = 2)

        n = 0
       
        for interface in interface_result:
            interface_speed[interface] = interface_speed_result[n] 
            n = n + 1
        stats.append(interface_speed)

        ram_total_object_type = [ObjectType(ObjectIdentity('1.3.6.1.4.1.9.9.48.1.1.1.6.1'))] 
        ram_total_result = get_bulk(target = self.router_ip, object_types = ram_total_object_type, community = CommunityData(self.community), count = 1)

        ram['RAM'] = ram_total_result[0]
        stats.append(ram)

        ram_used_object_type = [ObjectType(ObjectIdentity('1.3.6.1.4.1.9.9.48.1.1.1.5.1'))] 
        ram_used_result = get_bulk(target = self.router_ip, object_types = ram_used_object_type, community = CommunityData(self.community), count = 1)
    
        ram_used["RAM_used"] = ram_used_result[0]
        stats.append(ram_used)

        cpu_utilization_object_type = [ObjectType(ObjectIdentity('1.3.6.1.4.1.9.2.1.58.0'))]
        cpu_result = get_bulk(target = self.router_ip, object_types = cpu_utilization_object_type, community = CommunityData(self.community), count = 1)

        cpu["CPU"] = cpu_result[0]
        stats.append(cpu)

        hostname_object_type = [ObjectType(ObjectIdentity('1.3.6.1.4.1.9.2.1.3'))]
        hostname_result = get_bulk(target = self.router_ip, object_types = hostname_object_type, community = CommunityData(self.community), count = 1)

        hostname["hostname"] = hostname_result[0]
        stats.append(hostname)

        return stats

    def get_num_interfaces(self):
        interface_object_types = [ObjectType(ObjectIdentity('IF-MIB', 'ifDescr'))]
        interface_result = get_bulk(target = self.router_ip, object_types = interface_object_types, community = CommunityData(self.community), count = 2)
        return len(interface_result)   

    def get_interfaces(self):
        interface_object_types = [ObjectType(ObjectIdentity('IF-MIB', 'ifDescr'))]
        interface_result = get_bulk(target = self.router_ip, object_types = interface_object_types, community = CommunityData(self.community), count = 2)
        interfaces = {}
        for x in range(0, self.get_num_interfaces()):
            interfaces[f"{x}"] = interface_result[x]
        return interfaces

    def get_arp_cache(self):
        arp_cache_object_type = [ObjectType(ObjectIdentity('1.3.6.1.2.1.3.1.1.2'))]
        arp_cache_result = get_bulk(target = self.router_ip, object_types = arp_cache_object_type, community = CommunityData(self.community), count = 1)
        print(arp_cache_result[0])

    def set_hostname(self, new_hostname):
        set_value(target = self.router_ip, new_value = new_hostname, community = CommunityData(self.community))