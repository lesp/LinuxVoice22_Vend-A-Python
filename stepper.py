import RPi.GPIO as GPIO
import time, random
import easygui as eg

delay = 0.01

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
IN1 = 17
IN2 = 10
IN3 = 9
IN4 = 11
button = 23

outputs = [IN1,IN2,IN3,IN4]

for pin in outputs:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

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
    ccw(steps,delay)

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

while True:
    if GPIO.input(button) == False:
        steps = random.randint(1,512)
        cw(steps,delay)
        if steps >0 and steps < 128:
            answer = eg.choicebox(title="Question",msg="Which variable is storing a string?",choices=("a='Hello World'","b = 5","c = 2.0"))
            if answer == "a='Hello World'":
                eg.msgbox(title="CORRECT",msg="RIGHT ANSWER")
            else:
                eg.msgbox(title="INCORRECT",msg="WRONG ANSWER")
        elif steps >128 and steps < 256:
            answer = eg.choicebox(title="Question",msg="How can I add an item to a list?",choices=("append","pop","add"))
            if answer == "append":
                eg.msgbox(title="CORRECT",msg="RIGHT ANSWER")
            else:
                eg.msgbox(title="INCORRECT",msg="WRONG ANSWER")            
        elif steps >256 and steps < 384:
            answer = eg.choicebox(title="Question",msg="Which loop will go on forever?",choices=("While True","For","While False"))
            if answer == "While True":
                eg.msgbox(title="CORRECT",msg="RIGHT ANSWER")
            else:
                eg.msgbox(title="INCORRECT",msg="WRONG ANSWER")
        elif steps > 384 and steps < 512:
                answer = eg.choicebox(title="Question",msg="Which data type is best used for precise numerical data?",choices=("float","string","integer"))
                if answer == "float":
                    eg.msgbox(title="CORRECT",msg="RIGHT ANSWER")
                else:
                    eg.msgbox(title="INCORRECT",msg="WRONG ANSWER")
    else:
        print("Waiting")
        time.sleep(0.1)
