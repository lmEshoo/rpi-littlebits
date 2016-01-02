import RPi.GPIO as GPIO
import time

LedPin = 7
littlebitsPin =11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.setup(littlebitsPin, GPIO.OUT)
#pwm = GPIO.PWM(18, 1000)
#pwm.start(50) #50%

try:
    while True:
        print '...led off'
        GPIO.output(LedPin, GPIO.LOW)
        GPIO.output(littlebitsPin, GPIO.LOW)
        time.sleep(0.5)
        print 'led on...'
        GPIO.output(LedPin, GPIO.HIGH)
        GPIO.output(littlebitsPin, GPIO.HIGH)
        time.sleep(1.5)
except KeyboardInterrupt:
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.output(littlebitsPin, GPIO.HIGH)

    GPIO.cleanup()
