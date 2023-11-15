import pyrebase

class FirebaseManager:
    """
    firebase 연결 매니저
    """

    def __init__(self):
        # Firebase database init
        self.config = {
                        'apiKey': "",
                        'authDomain': "cocl-pvwatts.firebaseapp.com",
                        'databaseURL': "https://cocl-pvwatts-default-rtdb.asia-southeast1.firebasedatabase.app",
                        'serverAccount' : "",
                        'projectId': "cocl-pvwatts",
                        'storageBucket': "cocl-pvwatts.appspot.com",
                        'messagingSenderId': "176612325455",
                        'appId': "1:176612325455:web:1e13ce5f3ec6fed9f6d23a"
                    }
        self.app = pyrebase.initialize_app(self.config) # firebase app에 대한 참조 가져오기
        self.db = self.app.database() # database 서비스에 대한 참조 가져오기
