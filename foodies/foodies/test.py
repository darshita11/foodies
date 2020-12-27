import pyrebase
config={
    'apiKey': "AIzaSyBHNwg5mzUotvUpOjlusqcaz4FevdIvQsg",
    'databaseURL': "https://foodies-ece08-default-rtdb.firebaseio.com/",
    'authDomain': "foodies-ece08.firebaseapp.com",
    'projectId': "foodies-30804",
    'storageBucket': "foodies-30804.appspot.com",
    'messagingSenderId': "246611111789",
    'appId': "1:246611111789:web:3f401d08859a4bb386b464",
    'measurementId': "G-2R3D9XVG3G"
  }

firebase=pyrebase.initialize_app(config)
auth = firebase.auth()
auth.create_user_with_email_and_password('abc@gmail.com','123456')