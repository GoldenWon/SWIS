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
	
def testWrist():
	kit.servo[WRIST].angle = 0
	time.sleep(2)
	kit.servo[WRIST].angle = 180
	
def wristNormal():
	kit.servo[WRIST].angle = 90
	
	
	
# Perform middle finger
giveMiddleFinger()
# wait
time.sleep(2)
# Perform fingers straight
fingersStraight()

time.sleep(1)

# try 'B'
letterB()
# wait
time.sleep(2)
# Perform fingers straight
fingersStraight()

time.sleep(1)

# try 'A'
letterA()
# wait
time.sleep(2)
# back to straight
fingersStraight()

time.sleep(1)

# try 'C'
letterC()
#wait
time.sleep(2)
#back to straight
fingersStraight()

time.sleep(1)

# try 'D'
letterD()
# wait
time.sleep(2)
# back to straight
fingersStraight()

time.sleep(1)

# try 'E'
letterE()
# wait
time.sleep(2)
# back to straight
fingersStraight()

time.sleep(0.5)

# try 'F'
letterF()
# wait
time.sleep(2)
# back to straight
fingersStraight()

# try wrist
testWrist()
# wait
time.sleep(2)

testWrist()
time.sleep(2)

testWrist()
time.sleep(2)

wristNormal()


