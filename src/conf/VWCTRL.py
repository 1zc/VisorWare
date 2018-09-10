###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
###############################################################################


#                     VisorWare CTRL || Built for Visor2.0                    #



import time
import RPi.GPIO as GPIO
import os
import subprocess
import sys

print("Installing updates...\n")

print('\n\nDeleting old VisorWare...\n')
os.system('cd /home/pi && sudo rm VisorWare -r -f')
print('\n\nGetting new VisorWare...\n')
os.system('cd /home/pi && git clone https://github.com/LiamZC/VisorWare')
print('\n\nCleaning up...\n')
os.system('sudo rm /home/pi/VisorWare/src/cfg/cfg.txt')
os.system('cp cfg.txt /home/pi/VisorWare/src/cfg/cfg.txt')
try:
    print('Relaunching VW...')
    exit()
finally:
    os.system('sh /home/pi/VisorWare/launcher.sh')