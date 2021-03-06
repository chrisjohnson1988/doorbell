#!/usr/bin/python
import time
import os
import requests
import serial
import socket
from datetime import datetime

PULSE_WINDOW = 0.7
TRIGGER_COUNT = 15
MCAST_GRP = '224.0.0.1'
MCAST_PORT = 5007

ser = serial.Serial('/dev/ttyAMA0', 9600)
devid = os.environ['PUSHING_BOX_KEY']
multicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
multicast.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

def pulse():
  now = time.time()
  if pulse.count == 0:
    pulse.start = now
  if now - pulse.last < PULSE_WINDOW:
    pulse.count += 1
    if pulse.count == TRIGGER_COUNT: ring()
  elif pulse.count:
    print "[PULSES] Count " + str(pulse.count) + " length "+ str(pulse.last - pulse.start) + " @ " + str(datetime.fromtimestamp(pulse.last))
    pulse.count = 0
  pulse.last = now
pulse.start = 0
pulse.last = 0
pulse.count = 0

def ring():
  now = str(datetime.now())
  print "[INFO] Ring Ring @ " + now
  multicast.sendto("doorbell", (MCAST_GRP, MCAST_PORT))
  requests.get('http://api.pushingbox.com/pushingbox?devid=' + devid + '&time=' + now)
  time.sleep(10)
  print "[INFO] Listening again. Buffer contained: " + str(ser.read(ser.inWaiting()))

while True:
  try:
    data = ser.read(1)
    if data == 'x': pulse()
    else:
      print "[INFO] Non ring byte: " + data
  except Exception:
    pass
