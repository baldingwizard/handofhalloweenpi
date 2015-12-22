from smbus import SMBus
from subprocess import call
from subprocess import Popen

import time
import RPi.GPIO as GPIO

#Set up capacitive sensors
address = 0x29
CAP1188_SENINPUTSTATUS = 0x3
CAP1188_SENLEDSTATUS = 0x4
CAP1188_MTBLK = 0x2A
CAP1188_PRODID = 0xFD
CAP1188_MANUID = 0xFE
CAP1188_STANDBYCFG = 0x41
CAP1188_REV = 0xFF
CAP1188_MAIN = 0x00
CAP1188_MAIN_INT = 0x01
CAP1188_LEDPOL = 0x73
CAP1188_INTENABLE = 0x27
CAP1188_REPRATE = 0x28
CAP1188_LEDLINK = 0x72

CAP1188_SENSITIVITY = 0x1f
CAP1188_CALIBRATE = 0x26

b = SMBus(0)
b.write_byte_data(address, CAP1188_MTBLK, 0)
b.write_byte_data(address, CAP1188_STANDBYCFG, 0x30)
b.write_byte_data(address, CAP1188_INTENABLE, 0x05)
b.write_byte_data(address, CAP1188_LEDLINK, 0xff)

b.write_byte_data(address, CAP1188_SENSITIVITY, 0x5f)
b.write_byte_data(address, CAP1188_CALIBRATE, 0xff)
 


# Initialise GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.output(18, False)
GPIO.output(17, False)
GPIO.output(21, False)

GPIO.output(22, False)
GPIO.output(23, False)
GPIO.output(24, False)
GPIO.output(25, False)




while True:
 time.sleep(0.05)
 b.write_byte_data(address, CAP1188_MAIN, 0x00)
 #time.sleep(0.05)
 t1 = b.read_byte_data(address, CAP1188_SENINPUTSTATUS)
 #t1 = b.read_byte_data(address, CAP1188_SENLEDSTATUS)
 #print(str(t1)+","+'{0:08b}'.format(t1))

 if t1 & 128 != 0:
 call(["amixer","set","PCM,0","92%"])
 #print "Blue"
 #Wind
 #print "Wind"
 Popen(["mpg321","sounds/wind.mp3"])

 #print "eyes"
 # Eyes
 GPIO.output(17, True)
 GPIO.output(21, True)

 time.sleep(2)

 #print "bell"
 Popen(["mpg321","sounds/bell.mp3"])
 
 time.sleep(2)
 
 # bell
 #print "bells"
 Popen(["mpg321","sounds/bell.mp3"])
 time.sleep(1)
 Popen(["mpg321","sounds/bell.mp3"])
 time.sleep(2)
 Popen(["mpg321","sounds/bell.mp3"])

 time.sleep(2)
 
 # bell
 #print "bells"
 Popen(["mpg321","sounds/bell.mp3"])
 time.sleep(1)
 Popen(["mpg321","sounds/bell.mp3"])
 time.sleep(1)
 Popen(["mpg321","sounds/bell.mp3"])
 time.sleep(1)
 Popen(["mpg321","sounds/bell.mp3"])
 time.sleep(1)
 Popen(["mpg321","sounds/bell.mp3"])

 time.sleep(6)

 # Eyes off
 GPIO.output(17, False)
 GPIO.output(21, False)

 # Re-read sensor to reset any residual touch
 t1 = b.read_byte_data(address, CAP1188_SENINPUTSTATUS)
 time.sleep(0.5)
 t1 = b.read_byte_data(address, CAP1188_SENINPUTSTATUS)
 time.sleep(0.5)

 call(["amixer","set","PCM,0","95%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","85%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","75%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","55%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","25%"])
 time.sleep(0.25)

 call(["killall","mpg321"])
 call(["killall","aplay"])

 if t1 & 64 != 0:
 call(["amixer","set","PCM,0","95%"])
 #print "green"
 #Wind
 #print "wind"
 Popen(["mpg321","sounds/wind.mp3"])

 time.sleep(2)

 # Eyes
 #print "eyes"
 GPIO.output(17, True)
 GPIO.output(21, True)

 time.sleep(2)
 
 # Wolf
 #print "wolf"
 Popen(["mpg321","sounds/Wolf.mp3"])

 #print "skull fade on"
 GPIO.output(22, True)
 time.sleep(0.5)
 GPIO.output(23, True)
 time.sleep(0.5)
 GPIO.output(24, True)
 time.sleep(0.5)
 GPIO.output(25, True)

 time.sleep(5)

 #print "skull fade off"
 GPIO.output(22, False)
 time.sleep(0.5)
 GPIO.output(23, False)
 time.sleep(0.5)
 GPIO.output(24, False)
 time.sleep(0.5)
 GPIO.output(25, False)

 time.sleep(3)

 #print "eyes off"
 # Eyes off
 GPIO.output(17, False)
 GPIO.output(21, False)

 # Re-read sensor to reset any residual touch
 t1 = b.read_byte_data(address, CAP1188_SENINPUTSTATUS)
 time.sleep(0.5)
 t1 = b.read_byte_data(address, CAP1188_SENINPUTSTATUS)
 time.sleep(0.5)


 call(["amixer","set","PCM,0","95%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","85%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","75%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","55%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","25%"])
 time.sleep(0.25)
 call(["killall","mpg321"])
 call(["killall","aplay"])

 if t1 & 32 != 0:
 call(["amixer","set","PCM,0","95%"])

 Popen(["aplay","sounds/thunder.wav"])
 GPIO.output(17, True)
 GPIO.output(21, True)
 for x in range(1,20):

 GPIO.output(22, True)
 GPIO.output(23, False)
 GPIO.output(24, True)
 GPIO.output(25, False)
 time.sleep(0.05)

 GPIO.output(22, False)
 GPIO.output(23, True)
 GPIO.output(24, False)
 GPIO.output(25, True)
 time.sleep(0.05)

 time.sleep(2)

 Popen(["aplay","sounds/SCREAM_4.wav"])

 time.sleep(5)

 call(["amixer","set","PCM,0","100%"])
 Popen(["aplay","sounds/cackle3.wav"])

 time.sleep(1)
 GPIO.output(22, True)
 time.sleep(1)
 GPIO.output(22, False)
 GPIO.output(23, True)
 time.sleep(1)
 GPIO.output(23, False)
 GPIO.output(24, True)
 time.sleep(1)
 GPIO.output(24, False)
 GPIO.output(25, True)
 time.sleep(1)
 # Popper!
 GPIO.output(18, True)

 call(["mpg321","sounds/Wolf.mp3"])

 GPIO.output(22, False)
 GPIO.output(23, False)
 GPIO.output(24, False)
 GPIO.output(25, False)

 time.sleep(5)
 GPIO.output(18, False)

 GPIO.output(17, False)
 GPIO.output(21, False)


 # Re-read sensor to reset any residual touch
 t1 = b.read_byte_data(address, CAP1188_SENINPUTSTATUS)
 time.sleep(0.5)
 t1 = b.read_byte_data(address, CAP1188_SENINPUTSTATUS)
 time.sleep(0.5)

 call(["amixer","set","PCM,0","95%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","85%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","75%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","55%"])
 time.sleep(0.25)
 call(["amixer","set","PCM,0","25%"])
 time.sleep(0.25)

 call(["killall","mpg321"])
 call(["killall","aplay"])

