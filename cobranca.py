import pyrebase


Config = {
  "apiKey": "AIzaSyAXal4EpjRrRwbw3ZbOgCp37SwZhntDs6w",
  "authDomain": "relacionamento-d2f2a.firebaseapp.com",
  "projectId": "relacionamento-d2f2a",
  "storageBucket": "relacionamento-d2f2a.appspot.com",
  "databaseURL":"https://relacionamento-d2f2a-default-rtdb.firebaseio.com/",
  "messagingSenderId": "315669792394",
  "appId": "1:315669792394:web:ec4d1689f1e9ea682a4f73",
  "measurementId": "G-1K5LLKBJNM"
}

firebase = pyrebase.initialize_app(Config)

db = firebase.database()
def cobranca(key, code, uid):
    data = {"key": f"{key}", "code": f"{code}"}
    db.child("cobrancas").child(f"{uid}").set(data)