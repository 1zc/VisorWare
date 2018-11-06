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
os.system('sudo cp sf/screenfetch /usr/bin/screenfetch')
os.system('sudo chmod 755 /usr/bin/screenfetch')
print(ANSI.Color(120), "DONE.", ANSI.END)
# Configuring important interfaces.
print('Configuring Audio and Boot configs...')
os.system('sudo rm /boot/config.txt -f && sudo cp conf/config.txt /boot/config.txt')
os.system('sudo rm /home/pi/.asoundrc -f && sudo cp conf/.asoundrc /home/pi/')
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
os.system('sudo cp conf/VWCTRL.py /home/pi/VWUD/VWCTRL.py')
os.system('sudo cp conf/cfg.txt /home/pi/VWUD/cfg.txt')
print(ANSI.Color(120), "DONE.", ANSI.END)

print(Base.OKGREEN,"MANUAL UPGRADE HAS BEEN COMPLETED!", Base.END)
try:
    print("Relaunching VisorWare...")
    exit()
finally:
    os.system('sh /home/pi/VisorWare/launcher.sh')
