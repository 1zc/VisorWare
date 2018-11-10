###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
###############################################################################

# $$$$$$$$$$$$$$$$$$$$$$$$$$ || VisorWare v1.0 || $$$$$$$$$$$$$$$$$$$$$$$$$$$ #

# Advanced additional update commands will be run from this script when
# udcfg.txt is set to 1. 

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
padding = -2
top = padding
bottom = height=padding
x = 0
font = ImageFont.load_default()
disp.clear()
disp.display()
#
#######################################

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

import time
import RPi.GPIO as GPIO
import os
import subprocess
import requests
import math
from termCol import *
import VWUtils

os.system("clear")
print(Base.WARNING,"Running Additional Upgrade. This may take some more time.", Base.END)
print("")

# Installing screenfetch.
print('Configuring screenfetch...')
os.system('sudo cp /home/pi/VisorWare/src/sf/screenfetch /usr/bin/screenfetch')
os.system('sudo chmod 755 /usr/bin/screenfetch')
print(ANSI.Color(120), "DONE.", ANSI.END)
# Configuring important interfaces.
print('Configuring Audio and Boot configs...')
os.system('sudo rm /boot/config.txt -f && sudo cp /home/pi/VisorWare/src/conf/config.txt /boot/config.txt')
os.system('sudo rm /home/pi/.asoundrc -f && sudo cp /home/pi/VisorWare/src/conf/.asoundrc /home/pi/')
print(ANSI.Color(120), "DONE.", ANSI.END)
# Configuring start-up interfaces.
print('Configuring Start-Up Interfaces...\n')
os.system('sudo chmod u+x /home/pi/VisorWare/launcher.sh')
os.system('sudo rm /etc/systemmd/system/lzc_visorware.service -f')
os.system('sudo cp conf/lzc_visorware.service /etc/systemd/system/lzc_visorware.service')
os.system('sudo systemctl enable lzc_visorware.service')
os.system('sudo systemctl disable apt-daily.service')
os.system('sudo systemctl disable apt-daily-upgrade.service')
print(ANSI.Color(120), "DONE.", ANSI.END)
# Updating VW Update service files.
print('Configuring VWUD configs...')
os.system('cd /home/pi/ && sudo rm VWUD -r')
os.system('cd /home/pi/ && mkdir VWUD')
os.system('sudo cp /home/pi/VisorWare/src/conf/VWCTRL.py /home/pi/VWUD/VWCTRL.py')
os.system('sudo cp /home/pi/VisorWare/src/conf/cfg.txt /home/pi/VWUD/cfg.txt')
print(ANSI.Color(120), "DONE.", ANSI.END)

print(Base.OKGREEN,"MANUAL UPGRADE HAS BEEN COMPLETED!", Base.END)
try:
    print("Relaunching VisorWare...")
    exit()
finally:
    os.system('sh /home/pi/VisorWare/launcher.sh')
