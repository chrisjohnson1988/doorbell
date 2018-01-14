# 433mhz Doorbell

This project demostrates how to interact with a 433mhz based doorbell.
The one which I have used is a [Byron B306](https://www.amazon.co.uk/Byron-B306-Wireless-Plug-Through-Sounds/dp/B005JBN5K2).

Essentially, this project requires a 433mhz receiver connected to an Arduino
Pro Mini which specifically listens to the pulses triggered when the doorbell
is pushed. On detecting a signal, the arduino will print out over the serial
connection which is then detected by the raspberry pi.

# Building

1. Program the Arduino with the bundled `.ino` file.

2. Wire up a 433Mhz receiver, arduino pro mini (3v3) and a raspberry pi:

![Raspberry Pi Wiring](images/doorbell-rec_bb.png)

3. Disable Serial Getty:

       sudo systemctl stop serial-getty@ttyAMA0.service
       sudo systemctl disable serial-getty@ttyAMA0.service

4. Install required python packages

       sudo apt-get install python-serial python-requests

5. Run `doorbell_listen.py`

# Ring Ring

Provided is a python script which can use a 433mhz transmitter to ring the
doorbell. This is intended for testing purposes and can be run by executing:

    ring.py
