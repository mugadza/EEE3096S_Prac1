import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay

GPIO.setmode(GPIO.BOARD)     # enable BOARD pin numberings
GPIO.setup(11,GPIO.OUT)      # Set pin 11 as output
onOff = 1

while(True):
    GPIO.output(11, onOff)

    if(onOff == 1):
        onOff = 0
    else:
        onOff = 1
    time.sleep(0.5)
    
