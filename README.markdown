# 433mhz Doorbell

This project demostrates how to interact with a 433mhz based doorbell.
The one which I have used is a [Byron B306](https://www.amazon.co.uk/Byron-B306-Wireless-Plug-Through-Sounds/dp/B005JBN5K2).

Essentially, this project requires a 433mhz receiver connected to an Arduino
Pro Mini which specifically listens to the pulses triggered when the doorbell
is pushed. On detecting a signal, the arduino will raise an interrupt on the
connected raspberry pi.

# Ring Ring

Provided is a python script which can use a 433mhz transmitter to ring the
doorbell. This is intended for testing purposes and can be run by executing:

    ring.py
