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

	#Retrieve data from random key child(complicated)
	#get the value(university) of the object data
	users = db.child("users").get()
	list_uni=[]
	for user in users.each():
		dict={}
		dict=user.val()
		list_uni.append(dict["university"])
	for item in list_uni:
		print(item)

if __name__=="__main__":
	main()
