
import RPi.GPIO as GPIO          
from time import sleep

in1 = 23
in2 = 24
in3 = 6
in4 = 5
en = 25
en2 = 26
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(en,1000)
p1=GPIO.PWM(en2,1000)
p.start(25)
p1.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run b-stop w-forward s-backward l-low m-medium h-high  a-left d-right e-exit")
print("\n")

while(1):

    x=raw_input()

    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
	 GPIO.output(in3,GPIO.HIGH)
	 GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
	 GPIO.output(in3,GPIO.LOW)
	 GPIO.output(in4,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='f':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='w':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.HIGH)
	GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='s':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(50)
	p1.ChangeDutyCycle(50)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(75)
	p1.ChangeDutyCycle(75)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(100)
	p1.ChangeDutyCycle(100)
        x='z'

    elif x=='a':
        print("left")
        p.ChangeDutyCycle(50)
        p1.ChangeDutyCycle(75)
        x='z'

    elif x=='d':
        print("right")
        p.ChangeDutyCycle(75)
        p1.ChangeDutyCycle(50)
        x='z'


    elif x=='e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
