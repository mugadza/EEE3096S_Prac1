import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)     # enable BOARD pin numberings
GPIO.setup(11,GPIO.OUT)      # Set pin 11 as output
GPIO.setup(13,GPIO.OUT)       # Set pin 13 as output
GPIO.setup(15,GPIO.OUT)      # Set pin 15 as output
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set button 1 as input
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set button 2 as input

counter = 0

def main():
    # making the button intrupts and link to handle method
    GPIO.add_event_detect(7, GPIO.RISING, callback=handler,bouncetime=400)
    GPIO.add_event_detect(12, GPIO.RISING, callback=handler,bouncetime=400)
   
    

def handler(pin):
    global counter # call on the global counter
    print("=====================================")
    
    if pin==7: #check which button is pressed
        print("counting up")
        counter += 1
        if counter == 8: #check if maximum is reached
            counter = 0
        countUp(counter)
        
    if pin==12:#check which button is pressed
        print("counting down")
        counter -= 1
        if counter == -1:
            counter = 7 #check if manimum is reached
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
    #convert string to 3 bit binary number
    binaryString = str(bin(n))[2:]
    bitList = list(binaryString)

    while(len(bitList) < 3): #add zeroes in front if number has kess than 3 bits
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
