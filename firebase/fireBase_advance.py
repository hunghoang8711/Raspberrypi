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
	
	#Retrieve data advance
	result = db.child("users").order_by_child("firstname").equal_to("Pham").limit_to_first(2).get()
	#print(result.val())
	
	#equal_to
	#limit_to_first/end
	#start_at and end_at

	for person in result.each():
		print(person.val())	
if __name__=="__main__":
	main()
