# SWIS

This is the Python gesture repo for our project.

***IMPORTANT***

# make sure to set fingersStraight()
# inbetween each gesture for at least
# time.sleep(1) (maybe can go a little faster (0.6 or so)
# This is to prevent INDEX and THUMB from crashing/breaking

I imagine the main program will be a loop containing code to fetch
next word from the mic (probably the word will go into a FICO queue,
then sent through the database to find the gesture.

The next part of the main loop should be to pause a couple seconds
to give time to see the gesture, then call fingersStraight() for at
least time.sleep(#) -- # = 0.6 - 1
ex:psuedocode

loop(true)
	getTextFromMic()
	sendToDatabase()
	performGesture()
	time.sleep(2)
	
	fingersStraight()
	time.sleep(0.6)
	
	
**May vary a bit from this, but trying to paint a reasonable picture.

My files:

Gestures.py is the main file with all gesture functions.

TestCases.py is where I can save the Tests to try the gestures
so I don't have to comment them out, and I don't have to 
wait through them all each test run.
