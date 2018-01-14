#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

for x in range(0, 100):
  GPIO.output(17, GPIO.HIGH);
  time.sleep(0.001530)
  GPIO.output(17, GPIO.LOW);
  time.sleep(0.000433);
