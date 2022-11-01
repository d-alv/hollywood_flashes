# just a note for now, there will be a "shutoff" protocol
# so that each light turns off when this function is called"

# set the lights up here, as well as the shift module

import RPi.GPIO as GPIO
import sys
from random import choice
from time import sleep
from time_keeper import Time_Keeper
from papparazi import Noise

dataPIN = 21
latchPIN = 20 # this is pin that lets us see output
clockPIN = 19 # pulse here forces register to take in one bit and
# store it 

GPIO.setmode(GPIO.BCM)
GPIO.setup((dataPIN, latchPIN, clockPIN), GPIO.OUT)
GPIO.setwarnings(False)

class Flights():
    """class to control movement of lights"""
    def __init__(self):
        """declare variables"""
        self.IO = GPIO
        self.ns = Noise()
        self.tk = Time_Keeper()
        self.sleep = sleep
        self.choice = choice
        self.pause = .16
        self.repetitions= int(10/(self.pause * 6))
        
        self.light1 = '10000000'
        self.light2 = '01000000'
        self.light3 = '00100000'
        self.light4 = '00010000'
        self.light5 = '00001000' # remember I only use first 5 pins
        self.light6 = '00000100'
        self.lights = [self.light1,self.light2,self.light3,
                       self.light4,self.light5, self.light6]
        self.nlights =[]
        self.ulights=[]
        self.current_rotation = 0
        
        # below a dictionary for each light's sound
        
        
    def setup(self):
        """reverses order so that each number is element
        in the list"""
        self.IO.output(dataPIN, 0)
        self.IO.output(latchPIN, 0)
        self.IO.output(clockPIN, 0)
        
        for value in self.lights:
            value = value[::-1]
            diff = list(value)
            self.nlights.append(diff)
        
        self._random_pick(rotation=9)
            
            
    def _random_pick(self, start=False, rotation=1):
        if start == True:
            self.ns.play_pap()
        self.current_rotation = self.current_rotation + rotation
        if self.current_rotation == self.repetitions:
            self.current_rotation = 0
        elif self.current_rotation > 0:
            """random led selector"""
            rlights = self.nlights.copy()
            self.ulights=[]
            self.first = self.choice(rlights)
            self.ulights.append(self.first)
            rlights.remove(self.first)
            self.second= self.choice(rlights)
            self.ulights.append(self.second)
            rlights.remove(self.second)
            self.third = self.choice(rlights)
            self.ulights.append(self.third)
            rlights.remove(self.third)
            self.fourth = self.choice(rlights)
            self.ulights.append(self.fourth)
            rlights.remove(self.fourth)
            self.fifth = self.choice(rlights)
            self.ulights.append(self.fifth)
            rlights.remove(self.fifth)
            self.sixth = rlights[0]
            self.ulights.append(self.sixth)
            del rlights
        
       # for value in self.ulights:
            for value in self.ulights:
                if value == ['0', '0', '0', '0', '0', '0', '0', '1']:
                    self.light1 = value
                elif value ==['0','0','0','0','0','0','1','0']:
                    self.light2 = value
                elif value ==['0','0','0','0','0','1','0','0']:
                    self.light3 = value
                elif value ==['0','0','0','0','1','0','0','0']:
                    self.light4 = value
                elif value ==['0','0','0','1','0','0','0','0']:
                    self.light5 = value
                elif value == ['0','0','1','0','0','0','0','0']:
                    self.light6 = value
        
            self.flash_on(self.ulights)
            print("lights are good")
        
    

    def flash_on(self, source):
        
        # insert paparazzi noises first?
        # as it stands, this only runs once, I need it to run more than once...
       
        
        print("should work")
        for cam in source: # remember source is a list of lists now       
            self.tk.check_time()
            # if cam != 
            for bit in cam:
                if bit == "0":
                    val = 0
                else:
                    val=1
                    
                self.IO.output(dataPIN, val)
                self.clock()
               
            self.latch()
                
            if cam == self.light1:
                self.ns.play_shutter("/home/pi/Desktop/hollywood/far_left_nnnew.wav")
            elif cam ==self.light2:
                self.ns.play_shutter("/home/pi/Desktop/hollywood/mid_left_nnew.wav")
            elif cam ==self.light3:
                self.ns.play_shutter("/home/pi/Desktop/hollywood/mid_nnew.wav")
            elif cam ==self.light4:
                self.ns.play_shutter("/home/pi/Desktop/hollywood/mid_right_nnew.wav")
            elif cam ==self.light5:
                self.ns.play_shutter("/home/pi/Desktop/hollywood/far_right_nnnew.wav")
            elif cam ==self.light6:
                self.ns.play_shutter("/home/pi/Desktop/hollywood/new_new.wav")
              
                #self.ns.play_shutter("/home/pi/Desktop/hollywood/bolt2.wav")
             
            self.sleep(self.pause)
            self.clear()
            self.latch()      
        self.clear()
        self.latch()
        self._random_pick()
            
    def clear(self):
        self.IO.output(dataPIN,0)
        for x in range (0,8):
            self.IO.output(clockPIN, 0)
            self.IO.output(clockPIN, 1)
            self.IO.output(clockPIN, 0)
        
    def latch(self):
        self.IO.output(latchPIN, 1)
        self.IO.output(latchPIN, 0)
    
    def clock(self):
        self.IO.output(clockPIN, 1)
        self.IO.output(clockPIN, 0)
