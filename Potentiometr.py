import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.CE0)
mcp = MCP.MCP3008(spi, cs)
value1= AnalogIn(mcp, MCP.P0)

# Setup LEDs
led = digitalio.DigitalInOut(board.D10)
led.direction = digitalio.Direction.OUTPUT

led1 = digitalio.DigitalInOut(board.D24)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.D23)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.D18)
led3.direction = digitalio.Direction.OUTPUT

while True:
    value1 = AnalogIn(mcp, MCP.P0)
    print('ADC Voltage:'+str(value1.voltage)+'v')
    time.sleep(0.5)

    if value1.voltage <0.5:
        print("EMPTY")
        led.value = False
        led1.value = False
        led2.value = False
        led3.value = False

    if (value1.voltage>0.5)&(value1.voltage<1):
        print("LOW")
        led.value = True
        led1.value = False
        led2.value = False
        led3.value = False

    if (value1.voltage>1)&(value1.voltage<2):
        print("MEDIUM")
        led.value = True
        led1.value = True
        led2.value = False
        led3.value = False

    if (value1.voltage>2)&(value1.voltage<3):
        print("HIGH")
        led.value = True
        led1.value = True
        led2.value = True
        led3.value = False

    if value1.voltage >3:
        print("FULL")
        led.value = True
        led1.value = True
        led2.value = True
        led3.value = True