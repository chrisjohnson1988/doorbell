#!/usr/bin/python
import time
import os
import RPi.GPIO as GPIO
import requests
from datetime import datetime
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

devid = os.environ['PUSHING_BOX_KEY']

def ring(channel):
  now = str(datetime.now())
  print "Ring Ring @ " + now
  requests.get('http://api.pushingbox.com/pushingbox?devid=' + devid + '&time=' + now)

GPIO.add_event_detect(26, GPIO.RISING, callback=ring)

while True:
  time.sleep(10)
