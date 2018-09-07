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
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

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

print("Installing updates...\n")
image = Image.open('UD.ppm').convert('1')
disp.image(image)
disp.display()
time.sleep(5)

print('\n\nDeleting old VisorWare...\n')
os.system('cd /home/pi && sudo rm VisorWare -r -f')
print('\n\nGetting new VisorWare...\n')
os.system('cd /home/pi && git clone https://github.com/LiamZC/VisorWare')
print('\n\nCleaning up...\n')
os.system('sudo rm /home/pi/VisorWare/src/cfg/cfg.txt')
os.system('cp cfg.txt /home/pi/VisorWare/src/cfg/cfg.txt')
try:
    sys.exit(0)
finally:
    os.system('sh /home/pi/VisorWare/src/launcher.sh')