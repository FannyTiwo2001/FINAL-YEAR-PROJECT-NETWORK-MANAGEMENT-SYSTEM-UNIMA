import firebase_admin
from firebase_admin import db,credentials
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://netman-559dc-default-rtdb.firebaseio.com/Device"})

ip =input("Enter Ip: ")
action =input("Enter Action: ")
address =str(ip).replace(".","_")
ref = db.reference(f"/Devices/{address}")
if action == "true":
    ref.update({"state":True})
    print("Status Changed To:",True)
else:
    ref.update({"state":False})
    print("Status Changed To:",False)