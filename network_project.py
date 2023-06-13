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