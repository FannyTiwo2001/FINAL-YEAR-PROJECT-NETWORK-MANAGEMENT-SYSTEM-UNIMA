import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Set up Firebase credentials
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-url.firebaseio.com'
})

# Get a database reference
ref = db.reference('/path/to/collection')

# Collect data from Firebase
data = ref.get()

# Process the collected data
if data is not None:
    for key, value in data.items():
        # Do something with the data
        print(f"Key: {key}, Value: {value}")
else:
    print("No data found in the database.")
