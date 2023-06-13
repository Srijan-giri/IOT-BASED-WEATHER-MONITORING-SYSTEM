# Complete project details at https://RandomNerdTutorials.com/micropython-whatsapp-esp32-esp826/

try:
  import urequests as requests
except:
  import requests
  
import network
import test_main as tm


import esp
esp.osdebug(None)

import gc
gc.collect()


ssid="SRIJAN Jio"
password = "123454321"

#Your phone number in international format
phone_number = '+916290138496'
#Your callmebot API key
api_key = '6474811'

# data
temp,hum=tm.measure()
Data={"Temparature":temp,"Hummidity":hum}
print(f'Temparature : {temp} and Humidity :{hum}')

def connect_wifi(ssid, password):
  #Connect to your network
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())
  
  


def send_message(phone_number, api_key, message):
  #set your host URL
  url = 'https://api.callmebot.com/whatsapp.php?phone='+phone_number+'&text='+message+'&apikey='+api_key

  #make the request
  response = requests.get(url)
  #check if it was successful
  if response.status_code == 200:
    print('Success!')
  else:
    print('Error')
    print(response.text)

    
if temp >=25 :
    
    temp_msg="it is hot, It is necessary to go outside with an umbrella"
elif temp >=15 and temp <=24:
    temp_msg="Weather is good "
elif temp >=7 and temp <15 :
    temp_msg="Cold"
else :
    temp_msg="Too Cold"

# Connect to WiFi
connect_wifi(ssid, password)
# Send message to WhatsApp "Hello"
message = f'Now%20Temparature%20is%20{temp}%20and%20Humidity%20is%20{hum}%20from%20ESP32%20%28(micropython)%29' #YOUR MESSAGE HERE (URL ENCODED)https://www.urlencoder.io/ 
send_message(phone_number, api_key, message)