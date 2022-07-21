import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)
url = "https://notify-api.line.me/api/notify"
access_token = 'S34eZYHJy8NemqQ3BZkiEjh9M6ZZYBA8EJXChYyB0Og'
headers = {'Authorization': 'Bearer ' + access_token}


while True:
    result = instance.read()
    if result.is_valid():
        #print("Last valid input: " + str(datetime.datetime.now()))

        #print("Temperature: %-3.1f C" % result.temperature)
        #print("Humidity: %-3.1f %%" % result.humidity)

        # line post
        message = "\nTemperature: %-3.1f C" % result.temperature
        message = message + "\nHumidity: %-3.1f %%" % result.humidity
        payload = {'message': message}
        requests.post(url, headers=headers, params=payload,)

        time.sleep(10)
        break
