import os
import random
import pygame as pg
import time
import simpleaudio as sa
import wave

class Noise():
    """class for generating the noise - camera, flash, papparazi"""
    def __init__(self):

        # here each light gets assigned its shutter sound
        self.pap_list = ["/home/pi/Desktop/hollywood/questioning.wav", "/home/pi/Desktop/hollywood/r_carp-02.wav", "/home/pi/Desktop/hollywood/r_carp-03.wav",
                         "/home/pi/Desktop/hollywood/r_carp-04.wav", "/home/pi/Desktop/hollywood/r_carp-05.wav", "/home/pi/Desktop/hollywood/r_carp-06.wav",
                         "/home/pi/Desktop/hollywood/r_carp-09.wav", "/home/pi/Desktop/hollywood/r_carp-10.wav", "/home/pi/Desktop/hollywood/r_carp-11.wav",
                         "/home/pi/Desktop/hollywood/r_carp-06.wav", "/home/pi/Desktop/hollywood/r_carp-07.wav", "/home/pi/Desktop/hollywood/r_carp-08.wav"]
        self.sa = sa
        self.random = random
        # basically a shutter assigned to each flash
        self.selectedpap = 'x' # temporary variable this one is random - just what they say
        self.wave = wave
        
        
    def play_pap(self):
        pap = self.random.choice(self.pap_list)
        pap_play = sa.WaveObject.from_wave_file(pap)
        pap_play.play()
        
    def play_shutter(self,sound):
        sound_play = self.wave.open(sound, 'rb')
        sound_playd = sa.WaveObject.from_wave_read(sound_play)
        sound_plays = sound_playd.play()


        


#wave_obj = sa.WaveObject.from_wave_file("/home/pi/Desktop/hollywood/zap1.wav")
#wave_obj2 = sa.WaveObject.from_wave_file("/home/pi/Desktop/hollywood/bolt2.wav")

#wave_obj.play()
#wave_obj2.play()

# this audio code allows audio to override one another (play over eachother!)