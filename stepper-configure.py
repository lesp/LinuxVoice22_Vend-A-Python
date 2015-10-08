#!/usr/bin/env python3.4
import RPi.GPIO as GPIO
import time

delay = 0.01

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
IN1 = 17
IN2 = 10
IN3 = 9
IN4 = 11

outputs = [IN1,IN2,IN3,IN4]

for pin in outputs:
    GPIO.setup(pin, GPIO.OUT)

def cw(steps,delay):
    for i in range(steps):
        GPIO.output(IN1, True)
        GPIO.output(IN2, False)
        GPIO.output(IN3, False)
        GPIO.output(IN4, False)
        time.sleep(delay)
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
        GPIO.output(IN3, False)
        GPIO.output(IN4, False)
        time.sleep(delay)
        GPIO.output(IN1, False)
        GPIO.output(IN2, False)
        GPIO.output(IN3, True)
        GPIO.output(IN4, False)
        time.sleep(delay)
        GPIO.output(IN1, False)
        GPIO.output(IN1, False)
        GPIO.output(IN1, False)
        GPIO.output(IN1, True)
        time.sleep(delay)
    time.sleep(5)
    #ccw(steps,delay)

def ccw(steps,delay):
    for i in range(steps):
        GPIO.output(IN1, False)
        GPIO.output(IN2, False)
        GPIO.output(IN3, False)
        GPIO.output(IN4, True)
        time.sleep(delay)
        GPIO.output(IN1, False)
        GPIO.output(IN2, False)
        GPIO.output(IN3, True)
        GPIO.output(IN4, False)
        time.sleep(delay)
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
        GPIO.output(IN3, False)
        GPIO.output(IN4, False)
        time.sleep(delay)
        GPIO.output(IN1, True)
        GPIO.output(IN1, False)
        GPIO.output(IN1, False)
        GPIO.output(IN1, False)
        time.sleep(delay)