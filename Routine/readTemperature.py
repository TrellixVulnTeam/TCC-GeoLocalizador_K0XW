import RPi.GPIO as GPIO
import dht11


# read data using pin 14
instance = dht11.DHT11(pin = 4)
def readTemp():
    result = instance.read()

    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
    else:
        print("Error: %d" % result.error_code)
