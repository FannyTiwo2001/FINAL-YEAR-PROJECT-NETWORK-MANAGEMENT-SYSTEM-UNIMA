import firebase_admin
from firebase_admin import db,credentials
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://netman-559dc-default-rtdb.firebaseio.com/Device"})
device_node = db.reference("/Devices")
devices = device_node.get()

router =[]
switch =[]
work_station=[]

def main():
    print(devices_exist())
    fetching_devices_in_monitoring()
#Checking if the devices have been added
def devices_exist():
    if devices is not None:
        return True
    else:
        return False
def fetching_devices_in_monitoring():
    devices = device_node.get()
    for key,value in devices.items():
        
        if value['state']==True:
            if value['type'] == 'router':
                data ={'ip':str(key).replace("_","."),'community':value['community']}
                router.append(data)
                ref =db.reference(f"/{key}")
                #creating table if it doesnt exist
                if ref.get() is None:
                    path =db.reference("/")
                    new_node_ref = path.child(key)
                    path2 = db.reference(f"/{key}")
                    operation_node = path2.child("Operation_Status")
                    

                    new_node_ref.set({
                        "Device_State":1,
                        "Operational_Status":{"FastEthernet0_0":2, "FastEthernet0_1": 2},
                        "Host_name":"router",
                        "Admin_Status":{"FastEthernet0_0":2, "FastEthernet0_1": 2},
                        "Traffic_In":{"FastEthernet0_0":0, "FastEthernet0_1": 0},
                        "Traffic_Out":{"FastEthernet0_0":0, "FastEthernet0_1": 0},
                        "Bandwidth":{"FastEthernet0_0":0, "FastEthernet0_1": 0},
                        "Total_Memory":0,
                        "Memory_Usage":0,
                        "Cpu_Usage":0
                    })
            
                
            elif value['type'] == 'switch':
                data ={'ip':str(key).replace("_","."),'community':value['community']}
                switch.append(data)
                ref =db.reference(f"/{key}")
                if ref.get() is None:
                    path =db.reference("/")
                    new_node_ref = path.child(key)
                    
                    new_node_ref.set({
                        "Device_State":1,
                        "Operational_Status":{"GE1_1":2, "GE1_2": 2,"GE1_3":2,"GE1_4":2,"GE1_5":2},
                        "Host_name":"switch",
                        "Admin_Status":{"GE1_1":2, "GE1_2": 2,"GE1_3":2,"GE1_4":2,"GE1_5":2},
                        "Traffic_In":{"GE1_1":0, "GE1_2": 0,"GE1_3":0,"GE1_4":0,"GE1_5":0},
                        "Traffic_Out":{"GE1_1":0, "GE1_2": 0,"GE1_3":0,"GE1_4":0,"GE1_5":0},
                        "Bandwidth":{"GE1_1":0, "GE1_2": 0,"GE1_3":0,"GE1_4":0,"GE1_5":0},
                        "Total_Memory":0,
                        "Memory_Usage":0,
                        "Cpu_Usage":0
                    })
            elif value['type'] == 'station':
                data ={'ip':str(key).replace("_","."),'community':value['community']}
                work_station.append(data)         
def getting_monitored_routers():
    return router
def getting_monitored_switches():
    return switch
def getting_monitored_work_station():
    return work_station
def changing_device_state_down(ip):
    ip1 =str(ip).replace(".","_")
    device_state =db.reference(f"/{ip1}")
    if device_state.get() is not None:
        device_state.update({"Device_State":2})
def changing_device_state_up(ip):
    ip1 =str(ip).replace(".","_")
    device_state =db.reference(f"/{ip1}")
    if device_state.get() is not None:
        device_state.update({"Device_State":1})
def updating_router(ip,data,traffic_in,traffic_out,operation,admin):
    ref =db.reference(f'/{str(ip).replace(".","_")}')
    ref.update(data)
    child_traffic_in =ref.child("Traffic_In")
    child_traffic_in.update({
        "FastEthernet0_0":traffic_in["FastEthernet0/0"],
        "FastEthernet0_1":traffic_in["FastEthernet0/1"]

    })
    child_traffic_out =ref.child("Traffic_Out")
    child_traffic_out.update({
        "FastEthernet0_0":traffic_out["FastEthernet0/0"],
        "FastEthernet0_1":traffic_out["FastEthernet0/1"]

    })
    child_operational =ref.child("Operational_Status")
    child_operational.update({
        "FastEthernet0_0":operation["FastEthernet0/0"],
        "FastEthernet0_1":operation["FastEthernet0/1"]

    })
    child_admin =ref.child("Admin_Status")
    child_admin.update({
        "FastEthernet0_0":admin["FastEthernet0/0"],
        "FastEthernet0_1":admin["FastEthernet0/1"]

    })
def updating_switch(ip,data,traffic_in,traffic_out,operation,admin):
    ref =db.reference(f'/{str(ip).replace(".","_")}')
    ref.update(data)
    child_traffic_in =ref.child("Traffic_In")
    child_traffic_in.update({
        "GE1_1":traffic_in["GigabitEthernet1/1"], "GE1_2":traffic_in["GigabitEthernet1/2"],"GE1_3":traffic_in["GigabitEthernet1/3"],"GE1_4":traffic_in["GigabitEthernet1/4"],"GE1_5":traffic_in["GigabitEthernet1/5"]

    })
    child_traffic_out =ref.child("Traffic_Out")
    child_traffic_out.update({
        "GE1_1":traffic_out["GigabitEthernet1/1"], "GE1_2":traffic_out["GigabitEthernet1/2"],"GE1_3":traffic_out["GigabitEthernet1/3"],"GE1_4":traffic_out["GigabitEthernet1/4"],"GE1_5":traffic_out["GigabitEthernet1/5"]


    })
    child_operational =ref.child("Operational_Status")
    child_operational.update({
        "GE1_1":operation["GigabitEthernet1/1"], "GE1_2":operation["GigabitEthernet1/2"],"GE1_3":operation["GigabitEthernet1/3"],"GE1_4":operation["GigabitEthernet1/4"],"GE1_5":operation["GigabitEthernet1/5"]


    })
    child_admin =ref.child("Admin_Status")
    child_admin.update({
        "GE1_1":admin["GigabitEthernet1/1"], "GE1_2":admin["GigabitEthernet1/2"],"GE1_3":admin["GigabitEthernet1/3"],"GE1_4":admin["GigabitEthernet1/4"],"GE1_5":admin["GigabitEthernet1/5"]


    })

if __name__ == '__main__':
    main()