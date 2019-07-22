import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay

GPIO.setmode(GPIO.BOARD)     # enable BOARD pin numberings
GPIO.setup(11,GPIO.OUT)      # Set pin 11 as output

onOff = 1

while(True):
    GPIO.output(11, 1)
    time.sleep(0.5)
    GPIO.output(11, 0)
    time.sleep(0.5)
    
