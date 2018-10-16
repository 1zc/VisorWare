###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
###############################################################################

# $$$$$$$$$$$$$$$$$$$$$$$$$$ || VisorWare v1.0 || $$$$$$$$$$$$$$$$$$$$$$$$$$$ #

import time
import RPi.GPIO as GPIO
import os
import subprocess
import requests
import math
from termCol import *
import VWUtils

print("Reading configuration file...")
cfgp = 'cfg/cfg.txt'
cfgfile = open(cfgp, 'r+')

os.system("clear")
print(Base.WARNING,"Running Additional Upgrade. This may take some more time.", Base.END)
print("")

# Installing screenfetch.
print('\n\nConfiguring screenfetch...')
os.system('sudo cp sf/screenfetch /usr/bin/screenfetch')
os.system('sudo chmod 755 /usr/bin/screenfetch')
print(ANSI.Color(120), "\nDONE.", ANSI.END)
# Configuring important interfaces.
print('\n\nConfiguring Audio and Boot configs...')
os.system('sudo rm /boot/config.txt -f && sudo cp conf/config.txt /boot/config.txt')
os.system('sudo rm /home/pi/.asoundrc -f && sudo cp conf/.asoundrc /home/pi/')
print(ANSI.Color(120), "\nDONE.", ANSI.END)
# Configuring start-up interfaces.
print('\n\nConfiguring Start-Up Interfaces...\n')
os.system('sudo chmod u+x /home/pi/VisorWare/launcher.sh')
os.system('sudo cp conf/lzc_visorware.service /etc/systemd/system/lzc_visorware.service')
os.system('sudo systemctl enable lzc_visorware.service')
os.system('sudo systemctl disable apt-daily.service')
os.system('sudo systemctl disable apt-daily-upgrade.service')
print(ANSI.Color(120), "\nDONE.", ANSI.END)


cfgfile.close()
cfgfile = open(cfgp, 'w')
cfgfile.write('1')
cfgfile.close()

print(Base.OKGREEN,"MANUAL UPGRADE HAS BEEN COMPLETED!", Base.END)
exit()
