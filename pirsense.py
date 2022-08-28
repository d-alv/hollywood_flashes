# library help: gpiozero.readthedocs.io/en/stable/api_input.html
import RPi.GPIO as GPIO
import time

pir_sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_sensor, GPIO.IN)

GPIO.setwarnings(False)
current_state = GPIO.input(4)
current_state = 0

# make a 'movement flag' to control whether it can sense
class Pir_Sense():
    def __init__(self):
        self.current_state = 0
        self.current_state = GPIO.input(pir_sensor)
        

    def sensing(self):
        if GPIO.input(pir_sensor):
            return True
        else:
            return False
    

    
