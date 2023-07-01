from .models import Router as r, Interface
from .scripts import router_script, interface_script
import time
import threading
from celery import shared_task,Celery
class Router():
    def __init__(self,id):
        
       # try:
        self.router = r.objects.get(pk=id)
        #except:
           # print(f"Router with id = {id} does not exist!!")
        self.r_script = router_script(self.router.ip,self.router.community_string)
        self.fetched_interface = self.r_script.get_all_interfaces()
        print(self.fetched_interface)
        self.interfaces_born =[]
        self.d_interfaces = []
        x=0
        for i in self.fetched_interface:
           self.interfaces_born.append(interface_script(self.router.ip,(x),self.router.community_string))
           #updating interface to database
           obj = Interface(name = str(self.interfaces_born[x].get_interface_description()),ip = str(self.interfaces_born[x].get_interface_ip()),router=self.router)
           obj.save()
           x=x+1
        self.stop_loop   =   False
        z = 1
        for i in self.fetched_interface:
            self.d_interfaces.append(Interface.objects.get(pk=z))
            z=z+1

    @shared_task
    def monitor_router(self):
        while not self.stop_loop:
            try:
                data = self.r_script.start_monitoring()
            except:
                print("Failed to monitor. Connection lost")
                break
            self.router.name = str(data['name'])
            self.router.temperature = str(data['Temp'])
            self.router.memoryUtelization =str(data['memory'])
            self.router.interfaces=str(data['interface_list'])
            self.router.state = str("UP")
            self.router.uptime =str(data['uptime'])
            self.router.save()
            #interface Monitoring
            w = 0
            for i in self.interfaces_born:
                interface_data = i.get_interface_attributes()
                self.d_interfaces[w].ip = str(interface_data["IP"])
                self.d_interfaces[w].state = str(interface_data["State"]) 
                self.d_interfaces[w].speed = str(interface_data["Speed"]) 
                self.d_interfaces[w].interfaceType = str(interface_data["Type"]) 
                self.d_interfaces[w].description = str(interface_data["Description"]) 
                self.d_interfaces[w].macAddress = str(interface_data["MAC Address"]) 
                self.d_interfaces[w].inputPacketCount = str(interface_data["Input Packets"]) 
                self.d_interfaces[w].outputPacketCount = str(interface_data["Output Packets"]) 
                self.d_interfaces[w].inputErrorCount = str(interface_data["Input Errors"])
                self.d_interfaces[w].outputErrorCount= str(interface_data["Output Errors"])
                w=w+1

                
                

            time.sleep(1)
    
    app = Celery('networkapi')
    @app.task
    def stop_monitoring_router(self):
        self.stop_loop = True
