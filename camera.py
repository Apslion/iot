import time
from picamera import PiCamera
camera = PiCamera()

try:
    while True:
        print("Taking picture")
        camera.capture('/home/CVR/Desktop/%S.jpg'time.time())
        time.sleep(10)

except KeyboardInterrupt:
    camera.close()
    print("Program exited cleanly")