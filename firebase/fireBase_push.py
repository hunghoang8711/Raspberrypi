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

	#push data with random key
	#data={"name":"Tuan","age":30,"address":["Hanoi","Ho CHi Minh"]}
	#db.push(data)
	
	#push data with own key(Real-time)
	#data={"age":30,"address":["Hanoi","Ho CHi Minh"],"university":"UET"}
	#db.child("Minh").set(data)

	#push data with  key(with child is random key)
	#data={"age":30,"address":["Hanoi","Ho CHi Minh"],"university":"UET"}
	#db.child("Ly").push(data)

	#push data with many childs  with own key
	#data={"age":30,"address":["Hanoi","Ho CHi Minh"],"university":"UET"}
	#data1={"age":32,"address":["Haiduong","Binhdinh"],"university":"UEB"}
	#db.child("people").child("male").child("Tuan").push(data)
	#db.child("people").child("male").child("Minh").push(data1)

	#data1={"deadline":"12pm","detail":"math"}
	#data2={"deadline":"3am","detail":"matlab"}
	#data3={"paper":{"deadline":"4pm","detail":"physics"}}
	#db.child("listB").child("Monday").push(data1)
	#db.child("listB").child("Monday").push(data2)
	#db.child("listB").child("Wednesday").push(data3)


	data1={"lastname":"Tuan","firstname":"Pham","age":23,"university":"UET"}
	data2={"lastname":"Thang","firstname":"Pham","age":50,"university":"UET"}
	data3={"lastname":"Tung","firstname":"Tran","age":34,"university":"HUS"}
	data4={"lastname":"Ly","firstname":"Pham","age":23,"university":"ULIS"}
	data5={"lastname":"Minh","firstname":"Nguyen","age":36,"university":"UEB"}
	data6={"lastname":"Hoang","firstname":"Dao","age":228,"university":"IS"}

	db.child("users").push(data1)
	db.child("users").push(data2)
	db.child("users").push(data3)
	db.child("users").push(data4)
	db.child("users").push(data5)
	db.child("users").push(data6)
if __name__=="__main__":
	main()
