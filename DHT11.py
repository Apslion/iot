import Adafruit_DHT
import time

# Set the sensor type to DHT11
sensor = Adafruit_DHT.DHT11

# Set the GPIO pin where the sensor is connected (GPIO17)
pin = 17

# Function to read temperature and humidity
def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
    else:
        print('Failed to retrieve data from the sensor')

# Main loop to continuously read and display data
try:
    while True:
        read_sensor()
        time.sleep(2)  # Wait for 2 seconds before reading again

except KeyboardInterrupt:
    print("Program interrupted")