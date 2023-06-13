import urequests
import ujson
import network
from time import sleep
import time
import machine

ssid="Limited"
password = "123.ILUV"


wlan = network.WLAN(network.STA_IF)
wlan.active(False)
time.sleep(1)

wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("I am in idle state!")
    machine.idle()
print("WiFi is up!")
print(wlan.ifconfig())
time.sleep(1)

d = {'Subhajit':'9903247560',
     'Debasmita':'8961931476',
     'Aratrik':'8420516142',
     'Soumyadeep':'9007203627',
     'Suman':'6295692351'}

for i,j in d.items():
    msg = 'Hello '+i+', This is an alert message For Temperature and Humidity'
    api2 = 'https://www.fast2sms.com/dev/bulkV2?authorization=jhfjfyjyMLpNYgXRu7F3Sr1kV6KstAiEnbIfyUxcOC0heQqaQ1zHi6ojFfKn0sOJ5Vm9BTwyRW4rA&sender_id=TXTIND&message='+msg+'&route=v3&numbers='+j
#print(api)


    try:
        request = urequests.get(api2)
        
        print(request)
        #print('API call done ')
        #print(api2)
        time.sleep(1)
        
    except:
        print('Something went wrong')