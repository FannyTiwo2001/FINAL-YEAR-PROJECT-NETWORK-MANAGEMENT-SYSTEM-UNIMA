from pysnmp import hlapi
from pysnmp.hlapi import *
from pysnmp import *
from fetch import fetch
from construct_value_pairs import construct_value_pairs

def set_value(target, new_value, community, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = setCmd(
        engine,
        community,
        UdpTransportTarget((target, port)),
        context,
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0), OctetString(new_value))
    )
    return fetch(handler, 1)[0]