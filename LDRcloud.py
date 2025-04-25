#CONNECT CN6 TO P14
import RPi.GPIO as GPIO
import time
#for IoT Dashboard
import requests

light = 37 #Board number

# API endpoint details
API_URL = "https://physitech.net/iot/api/data"
API_TOKEN = "dKnB0dFlGPqiihTT5GP35nzGd4JMVdptb9ij"
API_TOPIC = "iottest"
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

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(light,GPIO.IN)

def read_light():
    while True:
        light_state = GPIO.input(light)
        if light_state == 0:
            code ="Light Detected"
            print(code)
            send_data_to_api(code)
        elif light_state == 1:
            code = "Light Not Detected"
            print(code)
            send_data_to_api(code)
        
        time.sleep(.3)

def destroy():   #When program ending, the function is executed. 
    GPIO.cleanup()
    

if _name_ == '_main_': #Program starting from here 
    try:
        setup()
        read_light()
    except KeyboardInterrupt:  
        destroy()