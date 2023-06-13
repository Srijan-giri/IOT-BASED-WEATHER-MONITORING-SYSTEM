import network
import machine, onewire, ds18x20, time
import ufirebase as firebase
import time
import test_main as tm
import network
import time
import machine

ssid="SRIJAN Jio"
password = "123454321"


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

URL =   'https://miniproject-weather-control-default-rtdb.firebaseio.com/Weather'


while True:
    
  #Data = {"Hello":"34"}       #Temp_Update()
    temp,hum=tm.measure()
    Data={"Temparature":temp,"Hummidity":hum}
    print(f'Temparature : {temp} and Humidity :{hum}')
    #print(Data)
    try:
        
        #firebase.put(URL,str(Data))
        firebase.put(URL,Data)
        print('Received Data: ',firebase.get(URL))
    except:
        print("Reconnecting....")
