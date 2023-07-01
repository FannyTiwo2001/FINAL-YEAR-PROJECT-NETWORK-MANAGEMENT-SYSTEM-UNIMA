from .scripts import interface_script
from .models import Interface ,Router
from .monitor_router import view_interfaces
import time
stop_flag = False
def monitor_interface(ip,index):
    interface = interface_script(ip,index)
    results = interface.get_interface_attributes()
    print("Router ip: "+ip+"\nInterface Index:"+index)
    return results

def update_database(result,ipaddress):
    router= Router.objects.get(ip=ipaddress)
    router_id=router.id
    router
    instance = Interface.objects.get(router=router_id)
    interface_data=result
    instance.ip=str(interface_data['IP'])
    instance.state = str(interface_data['State'])
    instance.speed = str(interface_data['Speed'])
    instance.interfaceType = str(interface_data['Type'])
    instance.description = str(interface_data['Description'])
    instance.macAddress = str(interface_data['MAC Address'])
    instance.inputPacketCount = str(interface_data['Input Packets'])
    instance.outputPacketCount = str(interface_data['Output Packets'])
    instance.inputErrorCount = str(interface_data['Input Errors'])
    instance.outputErrorCount = str(interface_data['Output Errors'])
    instance.save()

def monitor_now(ip_of_router,index):
    results = monitor_interface(ip_of_router,index)
    update_database(results,ip_of_router)

def start_monitoring_interface(ip_of_router,index):
    while not stop_flag:
        try:
            if type(monitor_now(ip_of_router,index)) ==str:
                call_back("No device Added!!")
                break
            else:
                for i in index:
                    monitor_now(ip_of_router,index[i])
        except:
            start_monitoring_interface(ip_of_router,index)
        time.sleep(5)
def stop_monitoring_interface(value):
    global stop_flag 
    stop_flag=value
    return stop_flag
#if a function is in thread then the call back willm handle returns
def call_back(result):
    return result
