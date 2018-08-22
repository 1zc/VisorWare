###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
###############################################################################


#                VisorWare ALPHA v0.1 || Built for Visor2.0                    #


###############################################################################
#                                                                             #
#                       Copyright 2018 LIAM CHARLES                           #
#                                                                             #
#   Licensed under the Apache License, Version 2.0 (the "License");           #
#   you may not use this file except in compliance with the License.          #
#   You may obtain a copy of the License at                                   #
#                                                                             #
#               http://www.apache.org/licenses/LICENSE-2.0                    #
#                                                                             #
#   Unless required by applicable law or agreed to in writing, software       #
#   distributed under the License is distributed on an "AS IS" BASIS,         #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#   See the License for the specific language governing permissions and       #
#    limitations under the License.                                           #
#                                                                             #
###############################################################################

import time
import RPi.GPIO as GPIO
import os

print("Reading configuration file...")
cfgp = 'cfg.txt'
cfgfile = open(cfgp, 'r+')

if cfgfile.read(1) == '0':
    print("First time VisorWare is being launched.")
    print(Base.WARNING,"RUNNING FIRST TIME SETUP!", Base.END)
    time.sleep(3)

    os.system('sudo apt-get update')
    os.system('sudo apt-get --yes --force-yes install python-imaging python-smbus')

    cfgfile.close()
    cfgfile = open(cfgp, 'w')
    cfgfile.write('1')
    cfgfile.close()

else:
    print("cfgfile good. Continuing...")
    cfgfile.close()

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from termCol import *

#######################################
# Display Initialization. DO NOT ALTER!
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
width = disp.width
height = disp.height
disp.clear()
disp.display()
#
#######################################

print("Launching VisorWare...\n")
image = Image.open('img/splash.ppm').convert('1')
disp.image(image)
disp.display()

##################################################
# Button input board initialization. DO NOT ALTER!
GPIO.setmode(GPIO.BCM)
leftb = 17
homeb = 27
rightb = 22
GPIO.setup(leftb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(homeb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
##################################################

os.system('clear')
print ("                     -----------------------------------")
print (ANSI.Color(120),"                         L I A M  Z.  C H A R L E S", ANSI.END)                          
print ("                     -----------------------------------") 

print ("\n\n\nVisorWare v0.1\n\n")

print (Base.FAILRED,"THIS IS AN ALPHA VERSION. BEWARE OF BUGS.", Base.END)
print (Base.WARNING,"Proper functionality cannot be guaranteed in a BETA build of VisorWare. Please install a stable version of VisorWare for stable and proper functionality.\n\n", Base.END)

print ("BUTTON INTERFACE TESTING LIVE!")
while True:
    if GPIO.input(leftb) == False:
        print("[INTERFACE] : LEFT")
        time.sleep(0.2)
    elif GPIO.input(homeb) == False:
        print("[INTERFACE] : HOME")
        time.sleep(0.2)
    elif GPIO.input(rightb) == False:
        print("[INTERFACE] : RIGHT")
        time.sleep(0.2)