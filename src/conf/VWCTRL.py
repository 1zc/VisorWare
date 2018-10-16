###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
###############################################################################


#                     VisorWare CTRL || Built for Visor2.0                    #

import os
import subprocess
import requests

print("Installing updates...\n")

print('Deleting old VisorWare...\n')
os.system('cd /home/pi && sudo rm VisorWare -r -f')
print('Done.')

print('\n\nGetting new VisorWare...\n')
os.system('cd /home/pi && git clone https://github.com/LiamZC/VisorWare')
print('Done.')

print('\nUpgrading...')
cfgp = '/home/pi/VisorWare/src/cfg/udcfg.txt'
cfgfile = open(cfgp, 'r+')
if cfgfile.read(1) == '1':
    os.system('sudo python3 /home/pi/VisorWare/src/manualUD.py')
    print('Done.')
    cfgfile.close()
else:
    print('Done. No upgrade parameter set.')
    cfgfile.close()

print('\nCleaning up...\n')
os.system('sudo rm /home/pi/VisorWare/src/cfg/cfg.txt')
os.system('cp cfg.txt /home/pi/VisorWare/src/cfg/cfg.txt')
print('Done.')

try:
    print('Relaunching VW...')
    exit()
finally:
    os.system('sh /home/pi/VisorWare/launcher.sh')