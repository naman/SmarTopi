import RPi.GPIO as GPIO
import time
import os
#from gopro import run
import subprocess

def pushbutton():
	GPIO.setmode(GPIO.BCM)
	
	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	while True:
	    input_state = GPIO.input(18)
	    if input_state == False:
	        print('Button Pressed')
        	time.sleep(0.2)
		proc = subprocess.Popen(['python2 gopro.py'], shell=True)
		

			
pushbutton()
