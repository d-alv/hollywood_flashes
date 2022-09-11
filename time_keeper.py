import time
from datetime import datetime


class Time_Keeper:
    """class for keeping time as well
        as creating timers for individual items -
        sound, flashing"""
    def __init__(self):
        self.datetime = datetime
        self.time = time
        self.elapsed_time = 0
        self.start_time = self.time.time()
        self.end_time = 0
        self.mode = "" # timer modes flash, sense
        self.flash_wait = .5 # .5 seconds
        self.sense_wait = 2 # 2 seconds?
        # ^^ defaulting time-trackers to zero
        
    def check_time(self):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        

        
    def set_start(self):
        """method sets start_time to zero for timer"""
        self.start_time = self.time.time()
        self.check_time()
        
    def waiting(self):
        """this is a class that effectively works as a
            timer but also a shut off switch"""
        # maybe this can be used like while waiting()...
        # then the loop breaks once the timer is over? should be quick anyways
        self.check_time()
        if self.elapsed_time >= 10:
            return False
        else:
            return True 
