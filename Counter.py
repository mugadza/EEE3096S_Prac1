import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)     # enable BOARD pin numberings
GPIO.setup(11,GPIO.OUT)      # Set pin 11 as output
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(7, GPIO.IN)


def main():
    #toggle()
    countUpKhomo()
    
def toggle():
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

#def countUp():
#    for x in range (0,8):
#        BinString = str(bin(x))
#        BinList = list(BinString)
#        for i in range(2, len(BinList)):
#            GPIO.output(11, i)
#            GPIO.output(13, onOff)
#            GPIO.output(15, onOff)
              
        
def countUpKhomo():
    for x in range (0,7):         #increament decimal
        BinString = str(bin(x))     #covert decimal to binary
        InitList = [0,0]                #list to keep Binlist big enough
        TempList = list(BinString)    #binary number split to list
        BinList = TempList + InitList  #concatinate lists to ensure index is 3 or bigger
        
        
        GPIO.output(11, int(BinList[2]))  #set state of led1
        GPIO.output(13, int(BinList[3]))  #set state of led2
        GPIO.output(15, int(BinList[4]))  #set state of led3
        
        time.sleep(0.5)  #delay to make changes visible
    
    
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
