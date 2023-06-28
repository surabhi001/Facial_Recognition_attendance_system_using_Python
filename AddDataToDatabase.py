import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendance-28ec5-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "20204217":
        {
            "name": "Taniya",
            "major": "cse",
            "starting_year":2020,
            "total_attendance":8,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:11"
        },
    "20204215":
        {
            "name": "Sushma",
            "major": "cse",
            "starting_year":2020,
            "total_attendance":75,
            "standing": "G",
            "year": 8,
            "last_attendance_time": "2022-12-11 00:54:11"
        },
    "20204213":
        {
            "name": "Surabhi",
            "major": "cse",
            "starting_year":2020,
            "total_attendance":9,
            "standing": "B",
            "year": 7,
            "last_attendance_time": "2022-12-11 00:54:11"
        },
    "20204204":
        {
            "name": "Siddharth",
            "major": "cse",
            "starting_year":2020,
            "total_attendance":41,
            "standing": "G",
            "year": 8,
            "last_attendance_time": "2022-12-11 00:54:11"
        }
}

for key,value in data.items():
    ref.child(key).set(value)