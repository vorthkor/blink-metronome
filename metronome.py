# libraries
import RPi.GPIO as GPIO
import os
from time import sleep

# INITIAL MESSAGE
os.system('clear')
print('\n Welcome to the blinking metronome project!')
print('''\
                                _                          
                  __      _____| | ___ ___  _ __ ___   ___ 
                  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ |
                   \ V  V /  __/ | (_| (_) | | | | | |  __/
                    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
                                                            

                ''')
print('\n Press ctrl+C to exit...\n')

# disable warnings (optional)
GPIO.setwarnings(False)

# Select GPIO Mode
GPIO.setmode(GPIO.BCM)

# set red,green, blue and buzzer pins
redPin = 12
bluePin = 19
greenPin = 13
buzzerPin = 23

# set pins as outputs
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(buzzerPin, GPIO.OUT)


def turnOff():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.LOW)
    GPIO.output(buzzerPin, GPIO.LOW)


def red():
    GPIO.output(redPin, GPIO.HIGH)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.LOW)


def green():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.HIGH)
    GPIO.output(bluePin, GPIO.LOW)


def blue():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.HIGH)


def yellow():
    GPIO.output(redPin, GPIO.HIGH)
    GPIO.output(greenPin, GPIO.HIGH)
    GPIO.output(bluePin, GPIO.LOW)


def main():
    while True:
        red()
        sleep(1)
        green()
        sleep(1)
        blue()
        sleep(1)
        green()
        sleep(1)


try:
    main()
except KeyboardInterrupt:
    turnOff()
