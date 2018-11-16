###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
###############################################################################


#                     VisorWare CTRL || Made for The Visor                    #

import os
import subprocess
import requests

majorUpgradeFlag = 0

print('Setting up clean update environment...')
os.system('cd /home/pi/VWUD && sudo mkdir temp')
os.system('cp /home/pi/VisorWare/src/cfg/langcfg.txt /home/pi/VWUD/temp/langcfg.txt')
print('Done.')

print('Deleting old VisorWare...')
os.system('cd /home/pi && sudo rm VisorWare -r -f')
print('Done.')

print('Getting new VisorWare...')
os.system('cd /home/pi && git clone https://github.com/LiamZC/VisorWare')
print('Done.')

print('Upgrading...')
cfgp = '/home/pi/VisorWare/src/cfg/udcfg.txt'
cfgfile = open(cfgp, 'r+')
if cfgfile.read(1) == '1':
    print("Major upgrade parameter detected.")
    majorUpgradeFlag = 1
    cfgfile.close()
else:
    print('Done. No upgrade parameter set.')
    majorUpgradeFlag = 0
    cfgfile.close()

print('Cleaning up update environment...')
os.system('sudo rm /home/pi/VisorWare/src/cfg/cfg.txt -f')
os.system('cp cfg.txt /home/pi/VisorWare/src/cfg/cfg.txt')
os.system('sudo rm /home/pi/VisorWare/src/cfg/langcfg.txt -f')
os.system('cp /home/pi/VWUD/temp/langcfg.txt /home/pi/VisorWare/src/cfg/langcfg.txt')
os.system('sudo rm /home/pi/VWUD/temp/langcfg.txt -f')
os.system('cd /home/pi/VWUD && sudo rm temp -r -f')
print('Done.')

try:
    print('...')
    exit()
finally:
    if majorUpgradeFlag == 1:
        os.system('python3 /home/pi/VisorWare/src/manualUD.py')
    else:
        os.system('sh /home/pi/VisorWare/launcher.sh')