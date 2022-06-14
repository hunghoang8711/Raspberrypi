from pyrebase import pyrebase
from time import sleep

def main():
	config= {
	"apiKey": "AIzaSyDdEWbqSvKoPdEoE6T90vhjGpEAlVelGcE",
	"authDomain": "lm35-7f0ff.firebaseapp.com",
	"databaseURL":"https://lm35-7f0ff-default-rtdb.asia-southeast1.firebasedatabase.app/",
	"storageBucket": "lm35-7f0ff.appspot.com"
	}
	firebase = pyrebase.initialize_app(config)
	db = firebase.database()
	#edit data in own key child
	#db.child("listA").child("Monday").update({"deadline":"5pm"})	
	
	#edit multiple data in different location in own key child
	data={"listA/Monday":{"detail":"biology"},"listA/Tuesday":{"deadline":"4am"}}
	db.update(data)	
	#lose data in the same child (note)
if __name__=="__main__":
	main()
