import firebase_admin
from firebase_admin import db,credentials
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://netman-559dc-default-rtdb.firebaseio.com/Device"})

previous_value = None

# Define the callback function to handle real-time updates
def callback(event):
    ref = db.reference('/kaisi')
    state = ref.get("state")
    print(state[0])
# Create a reference to the Firebase Realtime Database node you want to listen to
ref = db.reference('/kaisi')
print("Hi")
# Listen for real-time updates
ref.listen(callback)

# Keep the script running to continue receiving updates
while True:
    pass
