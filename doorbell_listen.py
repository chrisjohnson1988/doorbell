#!/usr/bin/python
import time
import os
import requests
import serial
from datetime import datetime

PULSE_WINDOW = 3
TRIGGER_COUNT = 3

ser = serial.Serial('/dev/ttyAMA0', 9600)
devid = os.environ['PUSHING_BOX_KEY']

def pulse():
  now = time.time()
  if now - pulse.last < PULSE_WINDOW:
    pulse.count += 1
    if pulse.count == TRIGGER_COUNT: ring()
  elif pulse.count:
    print "[PULSES] Last " + str(pulse.count) + " @ " + str(datetime.fromtimestamp(pulse.last))
    pulse.count = 0
  pulse.last = now
pulse.last = 0
pulse.count = 0

def ring():
  now = str(datetime.now())
  print "[INFO] Ring Ring @ " + now
  requests.get('http://api.pushingbox.com/pushingbox?devid=' + devid + '&time=' + now)

while True:
  if ser.read(1) == 'x': pulse()

