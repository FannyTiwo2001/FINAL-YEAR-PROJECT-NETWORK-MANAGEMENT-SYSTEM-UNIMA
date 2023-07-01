#getting ip addresseses of routers
from .models import Router
import threading as t
from .scripts import router_script
import time
stop_flag = False
def get_ip():
    #retrieving all router objects from the database
    ip_list=[]
    router_objects=Router.objects.all()
    for object in router_objects:
        ip_list.append(object.ip)
        print(object.ip)
    return ip_list
def monitor_router(ip,community):
    router=router_script(ip,community)
    return router.start_monitoring()
def updating_database(data,ipaddress):
    instance = Router.objects.get(ip=ipaddress)
    router_data=data
    instance.memoryUtelization = str(router_data['memory'])
    instance.temperature = str(router_data['Temp'])
    instance.uptime = str(router_data['uptime'])
    
    instance.save()
def monitor_now():
    results=[]
    ip_list=get_ip()
    if len(ip_list)==0:
        print("No Device Added !")
        return "No Device added!!"
    else:
        i=0
        x=0
        #monitoring all the routers
        for ip in ip_list:
            results.append(monitor_router(ip_list[i],'thom1'))
            i=1+i
        
        for result in results:
            updating_database(results[x],ip_list[x])
            x=1+x

def stop_monitoring(value):
    global stop_flag 
    stop_flag=value
    return stop_flag
def start_monitoring_all_routers(frequency):
    while not stop_flag:
        try:
            if type(monitor_now()) ==str:
                call_back("No device Added!!")
                break
            else:
                monitor_now()
        except:
            start_monitoring_all_routers()
        time.sleep(frequency)
def view_interfaces(id,community='thom1'):
    ip_list=get_ip()
    router=router_script(ip_list[id-1],community)
    return router.get_all_interfaces()

def call_back(result):
    return result
