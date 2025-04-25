import spidev
import time

# Set up SPI communication (Bus 0, Device 0)
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, Device 0
spi.max_speed_hz = 1000000

# Start the main loop
try:
    while True:
        # Send SPI request to read from channel 0 of MCP3008
        r = spi.xfer2([1, (8 + 0) << 4, 0])  # Channel 0
        ldr_value = ((r[1] & 3) << 8) + r[2]  # Combine the bytes
        voltage = (ldr_value * 3.3) / 1023  # Convert ADC value to voltage

        # Print LDR value and corresponding voltage
        print(f"LDR Value: {ldr_value}, Voltage: {voltage:.2f}V")

        time.sleep(1)

except KeyboardInterrupt:
    spi.close()  # Close the SPI connection when the program stops
    print("Program stopped.")