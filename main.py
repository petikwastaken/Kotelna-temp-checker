import time as t
t.sleep(20)

from urllib.request import urlopen
import os
link = "http://213.108.160.85:666/"
# Import the following modules
import requests
import json


 
# Function to send Push Notification
 
 
def pushbullet_noti(title, body):
 
    TOKEN = 'o.f9BZI9VWMfn1BzKIU3PQHxIPdPKcNwxO'  # Pass your Access Token here
    # Make a dictionary that includes, title and body
    msg = {"type": "note", "title": title, "body": body}
    # Sent a posts request
    resp = requests.post('https://api.pushbullet.com/v2/pushes',
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:  # Check if fort message send with the help of status code
        raise Exception('Error', resp.status_code)
    else:
        print('Message sent')
pushbullet_noti("⚠KOTELNA⚠", "script started successfully.")
spatny = 0
while(True):
    t.sleep(30)
    f = urlopen(link)
    myfile = f.read()
    x = str(myfile)
    x = x.split(' ')
    #list navigace:: kotel: 50, aku: 43
    kotel = x[50]
    aku = x[43].split('%')
    aku = aku[0]
    print("accu" + aku)
    print("kotel" + kotel)
    i = 0
    kotelnaData = "KOTEL: " + kotel + "°C⚠!! ACCUM: " + aku + "%⚠!!"
    if(float(kotel) >= 92.00 or float(aku) >= 75.00):
        if(spatny == 1):
            t.sleep(300)
            spatny = 0
        while(i <= 3):
            pushbullet_noti("⚠KOTELNA⚠", kotelnaData)
            t.sleep(1)
            i = i + 1
            spatny = 1
