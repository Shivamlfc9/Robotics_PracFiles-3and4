import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor_1A = 4
motor_1B = 17
motor_2A = 23
motor_2B = 24
GPIO.setup(motor_1A, GPIO.OUT)
GPIO.setup(motor_1B, GPIO.OUT)
GPIO.setup(motor_2A, GPIO.OUT)
GPIO.setup(motor_2B, GPIO.OUT)

seq = [[1,0,0,1],[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]
delay = 0.005

for i in range(10):
    for h_step in range(8):
        for pin in range(4):
            GPIO.output(motor_1A,  seq[h_step][0])
            GPIO.output(motor_1B,  seq[h_step][1])
            GPIO.output(motor_2A,  seq[h_step][2])
            GPIO.output(motor_2B,  seq[h_step][3])
            time.sleep(delay)
            for h_step in reversed(range(8)):
                for pin in range(4):
                    GPIO.output(motor_1A,seq[h_step][0])
                    GPIO.output(motor_1B,seq[h_step][1])
                    GPIO.output(motor_2A,seq[h_step][2])
                    GPIO.output(motor_2B,seq[h_step][3])
                    time.sleep(delay)
GPIO.cleanup()



            
