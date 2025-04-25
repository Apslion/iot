#Before executing this program intsall Adafruit_DHT11 Library using follwing command
#sudo apt-get install Adafruit_DHT11
#connect rmc from c12 to c7
import time
import Adafruit_DHT
#for IoT Dashboard
import requests

#Set the type of sensor and the pin for sensor
sensor = Adafruit_DHT.DHT11
pin =4#board 11 of pi

# API endpoint details
API_URL = "https://iot.pcs.net.in/api/data"
API_TOKEN = "t8zajCdFyl1qofZLOBOkYi9oSHohW7GbCJFL"
API_TOPIC = "DHT11_mqtt"

def send_data_to_api(message):
    data = {
        "msg": str(message),
        "token": API_TOKEN,
        "topic": API_TOPIC
    }
    
    response = requests.post(API_URL, json=data)
    
    if response.status_code == 200:
        print("Data sent successfully!")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")


while(1):
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print ("Humidity ="+str(humidity))
        print ("Temperature ="+str(temperature))
        value = "Humidity ="+str(humidity) + "Temperature ="+str(temperature)
        send_data_to_api(value)
        
    except ValueError:
        value = ("Unable to read data")
        print(value)
        send_data_to_api(value)