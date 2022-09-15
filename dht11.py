#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import requests, json
from influxdb import InfluxDBClient as influxdb
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

pin = 2 

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:   
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:                                                  
        print('Failed to get reading. Try again!')

while(True):
    time.sleep(1)
    data = [{
        'measurement' : 'pir',        
        'tags':{
            'VisionUni' : '2410',
        },
        'fields':{
            'temper' : temperature,
            'human' : humidity
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print ("Exception" + str(e))
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print ("Exception write " + str(e))
        finally:
            client.close()
    print("running influxdb OK")

