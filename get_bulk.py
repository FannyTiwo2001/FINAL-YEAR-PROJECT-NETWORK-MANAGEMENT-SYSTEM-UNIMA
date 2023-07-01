from pysnmp import hlapi
from fetch import fetch
timeout_value = 5  # Adjust the timeout value as needed
   
def get_bulk(target, object_types, community, count, start_from=0, port=161,
             engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.bulkCmd(
        engine,
        community,
        hlapi.UdpTransportTarget((target, port)),
        context,
        start_from, count,
        *object_types
    )
    return fetch(handler, count)