#File by Jiten Singh

import RPi.GPIO as GPIO
import time
import sys

ledPin = 11
buttonPin = 12
ledState = False

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)    
    GPIO.setup(ledPin, GPIO.OUT) 
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonEvent(channel):
    global ledState
    print('buttonEvent GPIO%d' %channel)
    ledState = not ledState
    
def loop():
    print('Please press the button.')
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback = buttonEvent, bouncetime=300)
            while ledState == False:
                GPIO.output(ledPin,GPIO.HIGH)   # turn on led
                time.sleep(1)
                GPIO.output(ledPin,GPIO.LOW) #turn off led
                time.sleep(1)
            else:
                GPIO.output(ledPin,GPIO.LOW) #turn the led off completely
                sys.exit('Led off') #quit program
            while True:
                pass


def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print('Program is running...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
