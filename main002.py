import paho.mqtt.client as mqtt
import time
import sys
import Adafruit_DHT
import csv
import datetime

import os
import smtplib
from email.message import EmailMessage

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
 

username = "8e1fab50-cda9-11ec-8da3-474359af83d7"

password = "3c7bb0509b202f0ed8d9b1d8fa51353e5fcc0ea5"

clientid = "473fd5d0-d36b-11ec-8c44-371df593ba58"

 

mqttc = mqtt.Client(client_id=clientid)
mqttc.username_pw_set(username, password=password)
mqttc.connect("mqtt.mydevices.com", port=1883, keepalive=60)
mqttc.loop_start()


topic_dht11_temp = "v1/" + username + "/things/" + clientid + "/data/1"

topic_dht11_humidity = "v1/" + username + "/things/" + clientid + "/data/2"

i = 1
while True:
    
    try:
        if i % 5 == 0:
            f=open("data.csv","a")
            humidity11, temp11 = Adafruit_DHT.read_retry(11,17)
            if temp11 is not None:
                temp11 = str(temp11)
                print(temp11)
                mqttc.publish(topic_dht11_temp, payload=temp11, retain=True)

            if humidity11 is not None:

                humidity11 =str(humidity11)
                print(humidity11)

                mqttc.publish(topic_dht11_humidity, payload=humidity11, retain=True)

            now=datetime.datetime.now()
            #f.write(temp11+humidity11)
            #writer=csv.writer(file)
            f.write(now.strftime("%d/%m/%Y, %H:%M:%S")+","+temp11+"°C"+","+humidity11+"%"+"\n")
        
        if i % 30 == 0:
            #The mail addresses and password
            sender_address = 'nguyenle09871@gmail.com'
            sender_pass = 'Hunghoang871212'
            receiver_address = 'hunghoang87121@gmail.com'

            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'WARNING TEMPERATURE AND HUMIDITY'
            #The body and the attachments for the mail
            
            
            mail_content1 = f"The  temperature: {temp11}°C, humidity: {humidity11}%."
            mail_content2 = "See anything: https://cayenne.mydevices.com/cayenne/dashboard/device/473fd5d0-d36b-11ec-8c44-371df593ba58"

            mail_content = mail_content1 + "\n" + mail_content2
            print(mail_content)

            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(sender_address, sender_pass)
            text = message.as_string()
            
            if float(temp11) > 26:
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
                
                print('Send successful')
            else:
                print("Send error")

        i = i + 1
        time.sleep(1)

           
    except (EOFError, SystemExit, KeyboardInterrupt):
        mqttc.disconnect()
        sys.exit()



