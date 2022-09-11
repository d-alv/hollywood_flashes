# here are general notes for the program while i design it
# I suggest a "sensor light" just for troubleshooting the night
# of so I know that I know it reads, just isn't flashing

# this file will comprise of all the other files, just because
# this is a bigger project than the other ones were.

import time
from datetime import datetime
from pirsense import Pir_Sense
from f_lights import Flights
from time_keeper import Time_Keeper


class MainClass:
    """the main class for compiling functions"""
    def __init__(self):
        self.flight = Flights()
        self.pir = Pir_Sense()
        self.tk = Time_Keeper()
        
        
        self.datetime = datetime
        self.time = time
        self.elapsed_time = 0
        self.start_time = 0
        self.end_time = 0
        self.need_time = 20 #subject to change
        
    def run_program(self):
        """function to keep the program going"""
        #self.time.sleep(self.need_time)
        self.start_time = time.time()
        self.flight.setup()
        while True:
            self.tk.check_time()
            if self.pir.sensing():
                if self.tk.elapsed_time >=self.need_time:
                    self.tk.set_start()
                    print("possibility")
                    self.flight._random_pick(start=True)
                    
                else:
                    pass

                    
                    
            # left off here
            # these are going to be the input modules
            # most likely be left to the time and the sensor, time first
            
if __name__ == "__main__":
    mc = MainClass()
    mc.run_program()
