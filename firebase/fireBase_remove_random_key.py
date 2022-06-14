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

	# remove the data from random key child(complicated)
	monday_task=db.child("listB").child("Monday").get()


	for task in monday_task.each():
		if(task.val()["deadline"]=="23pm"):
			key=task.key()		
			db.child("listB").child("Monday").child(key).child("detail").remove()

if __name__=="__main__":
	main()
