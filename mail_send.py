# Complete project details: https://RandomNerdTutorials.com/micropython-send-emails-esp32-esp826/
# Micropython lib to send emails: https://github.com/shawwwn/uMail
import umail
import network
import test_main as tm

# Your network credentials
ssid = 'SRIJAN Jio'
password = '123454321'

# Email details
sender_email = 'srijangiri2003@gmail.com'
sender_name = 'ESP32' #sender name
sender_app_password = 'nmtnxlvnkrefwbgm'
recipient_email ='srijangiri2003@gmail.com'
email_subject ='Weather Report'

def connect_wifi(ssid, password):
  #Connect to your network
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())
    
# Connect to your network
connect_wifi(ssid, password)

# data
temp,hum=tm.measure()
Data={"Temparature":temp,"Hummidity":hum}
print(f'Temparature : {temp} and Humidity :{hum}')

# Send the email
smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
smtp.login(sender_email, sender_app_password)
smtp.to(recipient_email)
smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
smtp.write("Subject:" + email_subject + "\n")
smtp.write("Temperature " + str(temp) + "\n")
smtp.write("Humidity " + str(hum) + "\n")

if temp >=25 :
    smtp.write("The weather outside is very hot , It is necessary to go outside with an umbrella")
elif temp >=15 and temp <=24:
    smtp.write("Weather is good ")
elif temp >=7 and temp <15 :
    smtp.write("Cold")
else :
    smtp.write("Too Cold")
    
    
smtp.send()
smtp.quit()