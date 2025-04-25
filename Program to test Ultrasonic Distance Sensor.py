# Connect from c15 to c10
import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
#for IoT Dashboard
import requests
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
#For IoT Dashboard
topic='ultrasonic'
token='dKnB0dFlGPqiihTT5GP35nzGd4JMVdptb9ij'
#end of Variables for IoT Dashboard
TRIG = 19                                  #Associate pin 35 to TRIG
ECHO = 13                                  #Associate pin 33 to ECHO
print("Distance measurement in progress")
GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)
# API endpoint details
API_URL = "https://iot.pcs.net.in/api/data"
API_TOKEN = "YwAeL6VQlHWv6DodOXWD6l5phaGVa7tyrzSD"
API_TOPIC = "b0roll"
def send_data_to_api(distance):
    data = {
        "msg": str(distance),
        "token": API_TOKEN,
        "topic": API_TOPIC
    }
    
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        print("Data sent successfully!")
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
while True:

  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print("Waitng For Sensor To Settle")
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points
  
  if distance > 2 and distance < 400:      #Check whether the distance is within range
    print("Distance:",distance - 0.5,"cm")
    #sending data to dashboard
    send_data_to_api(distance)
        
  else:
    distance='Out of Range'
    print("Out Of Range")                   #display out of range
    #sending data to dashboard
    send_data_to_api(distance)