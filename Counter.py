import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay

GPIO.setmode(GPIO.BOARD)     # enable BOARD pin numberings
GPIO.setup(11,GPIO.OUT)      # Set pin 11 as output
GPIO.setup(7, GPIO.IN)

onOff = 1

alreadyPressed = 0
    
while(True):
    GPIO.output(11, onOff) # set LED state
     
    if (GPIO.input(7) == True):         # Check if switch is pressed
        if(alreadyPressed == 1):        # If its already pressed, skip everything below (i.e continue)
            continue
        
        alreadyPressed = 1              # If not, then change the state to pressed

        if(onOff == 1):
            onOff = 0
        else:
            onOff = 1
    else:
        alreadyPressed = 0
        
    time.sleep(0.010)
    
