import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)     # enable BOARD pin numberings
GPIO.setup(11,GPIO.OUT)      # Set pin 11 as output
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0

def main():
    GPIO.add_event_detect(7, GPIO.RISING, callback=handler,bouncetime=400)
    GPIO.add_event_detect(12, GPIO.RISING, callback=handler,bouncetime=400)
    while True:
        time.sleep(0)
    

def handler(pin):
    global counter
    print("=====================================")
    if pin==7:
        print("counting up")
        counter += 1
        if counter == 8:
            counter = 0
        countUp(counter)
        
    if pin==12:
        print("counting down")
        counter -= 1
        if counter == -1:
            counter = 7
        countDown(counter)
   
    return
        
def countUp(x):
    binaryList = makeThreeBitBinary(x)
    
    GPIO.output(11, int(binaryList[0]))  #set state of led1
    GPIO.output(13, int(binaryList[1]))  #set state of led2
    GPIO.output(15, int(binaryList[2]))  #set state of led3
    print(binaryList)
    time.sleep(1)  #delay to make changes visible

def countDown(x):
    binaryList = makeThreeBitBinary(x)
        
    GPIO.output(11, int(binaryList[0]))  #set state of led1
    GPIO.output(13, int(binaryList[1]))  #set state of led2
    GPIO.output(15, int(binaryList[2]))  #set state of led3
    print(binaryList)
    time.sleep(1)  #delay to make changes visible
        
def makeThreeBitBinary(n):
    binaryString = str(bin(n))[2:]
    bitList = list(binaryString)

    while(len(bitList) < 3):
        bitList = ['0'] + bitList

    return bitList

    
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        #while True:
        main()
            
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
