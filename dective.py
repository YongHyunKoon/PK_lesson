import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

DETECT = 40
RED = 11

on = GPIO.HIGH
off = GPIO.LOW

GPIO.setup(DETECT, GPIO.IN, GPIO.PUD_DOWN)

GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)

DETECT_IN_LVL = GPIO.LOW
time_elapsed = 0

try:
    while True:
        DETECT_IN_LVL_P = DETECT_IN_LVL
        DETECT_IN_LVL = GPIO.input(DETECT)
        if DETECT_IN_LVL is not DETECT_IN_LVL_P:
            time_elapsed = 0
        else:
            time_elapsed += 1
        if DETECT_IN_LVL==0:
            print('INPUT LEVEL:LOW, time_elasped: %s sec' %time_elapsed)
            GPIO.output(RED,off)
        else:
            print('INPUT LEVLE:HIGH time_elasped: %s sec' %time_elapsed)
            GPIO.output(RED,on)

        time.sleep(1)
#            sleep_time = 0.1
#        sleep_dur = 0
#        while sleep_dur <= 1:
#            if DETECT_IN_LVL == 0:
#                GPIO.output(RED,off)
#            else:
#                GPIO.output(RED,on)
#            time.sleep(sleep_time/2)
#            sleep_dur += sleep_time

except KeyboardInterrupt:
    pass

GPIO.cleanup()
print('GPIO. Cleanup\n')
