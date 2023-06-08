import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor1 = 4
motor2 = 17
motor3 = 23
motor4 = 24

GPIO.setup(motor1,GPIO.OUT)
GPIO.setup(motor2,GPIO.OUT)
GPIO.setup(motor3,GPIO.OUT)
GPIO.setup(motor4,GPIO.OUT)

seq = [[1,0,0,1],[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]

path = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]
delay = 0.05

for step in path:
    GPIO.out(motor1,step[0])
    GPIO.out(motor2,step[1])
    GPIO.out(motor3,step[2])
    GPIO.out(motor4,step[3])
    time.sleep(delay)

GPIO.cleanup()



    
