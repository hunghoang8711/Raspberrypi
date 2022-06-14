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
	
	monday_task = db.child("listB").child("Monday").get()
	
	#access to the random key(complicated)
	'''list1=[]
	for task in monday_task.each():
		list1.append(task.key())
	for item in list1:
		print(item)'''
	
	#access to the values of random key(complicated)
	'''dict1={}
	for task in monday_task.each():
		dict1=task.val()
		for item in dict1:
			print(item+" : "+dict1[item])'''

	#edit specific data in random key child(complicated)(many random child key)
	'''monday_task = db.child("listB").child("Monday").get()    
	for task in monday_task.each():
		if(task.val()["detail"]=="matlab"):
			key = task.key()
			db.child("listB").child("Monday").child(key).update({"deadline":"23pm"})'''

	#edit data in random key child(complicated)(only random child key)
	#wednesday_task = db.child("listB").child("Wednesday").get()	
	#for task in wednesday_task.each():
		#key=task.key()
		#db.child("listB").child("Wednesday").child(key).update({"deadline":"12pm","detail":"physics"})
 
if __name__=="__main__":
	main()
