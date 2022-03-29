import time

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

THUMB = 0
INDEX = 1
MIDDLE = 2
RING = 3
PINKY = 4
WRIST = 5

def giveMiddleFinger():
	kit.servo[THUMB].angle = 110
	kit.servo[INDEX].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180

def fingersStraight():
	kit.servo[THUMB].angle = 0
	kit.servo[INDEX].angle = 0
	kit.servo[MIDDLE].angle = 0
	kit.servo[RING].angle = 0
	kit.servo[PINKY].angle = 0
	
def letterA():
	kit.servo[THUMB].angle = 110
	kit.servo[INDEX].angle = 180
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
def letterB():
	
	kit.servo[MIDDLE].angle = 0
	kit.servo[RING].angle = 0
	kit.servo[PINKY].angle = 0
	kit.servo[THUMB].angle = 180
	kit.servo[INDEX].angle = 0

def letterC():
	kit.servo[THUMB].angle = 110
	kit.servo[INDEX].angle = 100
	kit.servo[MIDDLE].angle = 100
	kit.servo[RING].angle = 100
	kit.servo[PINKY].angle = 100
	
def letterD():
	kit.servo[THUMB].angle = 180
	kit.servo[INDEX].angle = 0
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
def letterE():
	kit.servo[THUMB].angle = 180
	kit.servo[INDEX].angle = 110
	kit.servo[MIDDLE].angle = 110
	kit.servo[RING].angle = 110
	kit.servo[PINKY].angle = 110
	
def letterF():
	kit.servo[THUMB].angle = 110
	kit.servo[INDEX].angle = 110
	kit.servo[MIDDLE].angle = 0
	kit.servo[RING].angle = 0
	kit.servo[PINKY].angle = 0
	
def letterG():
	# Best can do
	kit.servo[THUMB].angle = 130
	kit.servo[INDEX].angle = 0
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
def letterH():
	kit.servo[THUMB].angle = 150
	kit.servo[INDEX].angle = 0
	kit.servo[MIDDLE].angle = 0
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
def letterI():
	kit.servo[INDEX].angle = 180
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 0
	time.sleep(0.6)
	kit.servo[THUMB].angle = 150
	
def letterJ():
	# No real way to draw J
	kit.servo[INDEX].angle = 180
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 0
	time.sleep(0.6)
	kit.servo[THUMB].angle = 150
	kit.servo[WRIST].angle = 180
	time.sleep(0.6)
	kit.servo[WRIST].angle = 90
	
def letterK():
	# Here's H again because
	# of limited movement
	kit.servo[THUMB].angle = 150
	kit.servo[INDEX].angle = 0
	kit.servo[MIDDLE].angle = 0
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
def letterL():
	kit.servo[THUMB].angle = 0
	kit.servo[INDEX].angle = 0
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
def letterM():
	kit.servo[THUMB].angle = 180
	time.sleep(0.6)
	kit.servo[INDEX].angle = 180
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
def letterN():
	# Copy of M limit of hand
	kit.servo[THUMB].angle = 180
	time.sleep(0.6)
	kit.servo[INDEX].angle = 180
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
def letterO():
	kit.servo[THUMB].angle = 100
	kit.servo[INDEX].angle = 100
	kit.servo[MIDDLE].angle = 100
	kit.servo[RING].angle = 100
	kit.servo[PINKY].angle = 100
	
def letterP():
	# Again limits of hand
	# Can't bend at wrist
	kit.servo[THUMB].angle = 100
	kit.servo[INDEX].angle = 0
	kit.servo[MIDDLE].angle = 120
	kit.servo[RING].angle = 100
	kit.servo[PINKY].angle = 120
	
def letterQ():
	# Can't bend at wrist
	kit.servo[THUMB].angle = 100
	kit.servo[INDEX].angle = 95
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
def letterR():
	kit.servo[THUMB].angle = 180
	kit.servo[INDEX].angle = 0
	kit.servo[MIDDLE].angle = 0
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
def letterS():
	kit.servo[INDEX].angle = 180
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	# have to wait to close thumb
	# on top of other fingers
	time.sleep(0.6)
	kit.servo[THUMB].angle = 180
	
def letterT():
	kit.servo[THUMB].angle = 180
	# Thumb must close first
	time.sleep(0.6)
	kit.servo[INDEX].angle = 180
	kit.servo[MIDDLE].angle = 180
	kit.servo[RING].angle = 180
	kit.servo[PINKY].angle = 180
	
	
	
def testWrist():
	kit.servo[WRIST].angle = 0
	time.sleep(2)
	kit.servo[WRIST].angle = 180
	
def wristNormal():
	kit.servo[WRIST].angle = 90
	
# make sure to set fingersStraight()
# inbetween each gesture for at least
# time.sleep(1) (maybe can go a little faster (0.6 or so)
# This is to prevent INDEX and THUMB from crashing/breaking



# try 'P'
letterP()
# wait
time.sleep(2)

# back to straight
fingersStraight()
time.sleep(0.8)

# try 'Q'
letterQ()
# wait
time.sleep(2)

# back to straight
fingersStraight()
time.sleep(0.8)

# try 'R'
letterR()
# wait
time.sleep(2)

# back to straight
fingersStraight()
time.sleep(0.8)

# try 'S'
letterS()
# wait
time.sleep(2)

# back to straight
fingersStraight()
time.sleep(0.8)

# try 'T'
letterT()
# wait
time.sleep(2)

# back to straight
fingersStraight()
time.sleep(0.8)
