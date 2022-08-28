# hollywood_flashes
Cameras flash like at a red carpet for the oscars. 

Concept is overall quite simple:

The main class has access to the lights as well as the light sensor and timer class. 
The light sensor class has access to the volume/ sounds.

The main class is run on a loop cycling between the time classes and the 
motion sensor class so that both the time and presence of people are being 
constantly updated. 

Using the time class, the motion sensor is run on a timer so that it is not constantly playing, 
therefore not putting too much strain on the raspberry pi usw. 

This is how the code goes:

Motion detected, check if within the correct time bounds, if so, continue to 
randomly assign which lights flash at which points, the light positions are passed
to a shift register and then the lights flash accordingly with their respective 
camera shutter .wav files. This is all done with the background noise of a crowd cheering
for until the cheering audio is over. - this all lasts approximately 10 seconds. 
