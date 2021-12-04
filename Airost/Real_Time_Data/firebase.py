import pyrebase
import datetime

firebaseConfig={
    'apiKey': "AIzaSyAvLVPU1PawfERdrLDPGz1Z8AiKjx5R6LA",
    'authDomain': "parking-991b7.firebaseapp.com",
    'databaseURL' : "https://parking-991b7-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'projectId': "parking-991b7",
    'storageBucket': "parking-991b7.appspot.com",
    'messagingSenderId': "708245170791",
    'appId': "1:708245170791:web:022828b1b437a96c4382c2"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

data={
    'age':40,
    'address': "New York"
}



def update_db(parkingId, occupied):
    json = {
        'Space': occupied,
        'TimeStamp': datetime.datetime.now().timestamp()
    }
    db.child('Car Park A').child(parkingId).update(json)
    print("Update Successfully")

