from router import Router
from switch import Switch
import datetime,time
from pysnmp import hlapi
import json
from device_status_checker import devices_exist, fetching_devices_in_monitoring,getting_monitored_routers,updating_router,changing_device_state_down,changing_device_state_up,updating_switch,getting_monitored_switches
def main():
    while True:
        #checking if there are devices in monitoring state
        if devices_exist():
            print("Fetching Devices")
            getting_monitored_routers().clear()
            getting_monitored_switches().clear()
            fetching_devices_in_monitoring()
            print("Fetching Done")
            monired_routers = getting_monitored_routers()
            monired_switches =getting_monitored_switches()
            if len(monired_routers) >0:
                for routers in monired_routers:
                    community =routers["community"]
                    ip = routers['ip']
                    try:
                        results=monitor_router(community,ip)
                        changing_device_state_up(ip)
                    except Exception as e:
                        print("Connection Failed!")
                        #changing Device Status to Off
                        changing_device_state_down(ip)
                        #else:

                        print(e)
                        time.sleep(1)
                        #main()
                    print("Writing Data:",ip)
                    sending_router_data(ip,results)
                    print("Successfully updated")
                    #time.sleep(1)
            else:
                print("No Router In Monitoring State")
                time.sleep(1)
            if len(monired_switches)>0:
                print(monired_switches)
                for switches in monired_switches:
                    community =switches["community"]
                    ip = switches['ip']
                    try:
                        results2=monitor_switch(community,ip)
                        changing_device_state_up(ip)
                    except Exception as e:
                        print("Connection Failed!")
                        #changing Device Status to Off
                        changing_device_state_down(ip)
                        #else:

                        print(e)
                        time.sleep(1)
                        #main()
                    print("Writing Data:",ip)
                    sending_switch_data(ip,results2)
                    print("Successfully updated")
                    #time.sleep(1)
            else:
                print("No Switch In Monitoring State")
                time.sleep(1)
                
        else:
            print("No Device Added")
            print("Waiting")
            time.sleep(3)
            main()



def monitor_router(community_string,ip):
    r = Router(community_string,ip)
    return r.get_stats()
def monitor_switch(community_string,ip):
    s = Switch(community_string,ip)
    return s.get_stats()
def sending_router_data(ip,data):
    datetime_key=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    keeping ={
            "Admin_status":0,
            "Operation_status":0,
            "Traffic_in":0,
            "Traffic_out":0,
    }
    data_x = {
        
            "Host_name":data[8]["hostname"],
            "Total_Memory":data[5]["RAM"],
            "Memory_Usage":data[6]["RAM_used"],
            "Cpu_Usage":data[7]["CPU"]
        
    }
    updating_router(ip,data_x,data[2],data[3],data[1],data[0])
def sending_switch_data(ip,data):
    datetime_key=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    keeping ={
            "Admin_status":0,
            "Operation_status":0,
            "Traffic_in":0,
            "Traffic_out":0,
    }
    data_x = {
        
            "Host_name":data[8]["hostname"],
            "Total_Memory":data[5]["RAM"],
            "Memory_Usage":data[6]["RAM_used"],
            "Cpu_Usage":data[7]["CPU"]
        
    }
    updating_switch(ip,data_x,data[2],data[3],data[1],data[0])
if __name__ == '__main__':
    main()