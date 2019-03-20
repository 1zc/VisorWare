# VisionEngine - Graphical Rendering Engine for VisorWare supported hardware.
# Packaged with VisorWare, a project by Liam Z. Charles.

#####################################################################################
#                                                                                   #
#    VisionEngine.py - Graphical Rendering Engine for VisorWare supported hardware. #
#    Copyright (C) 2019  Liam Z. Charles                                            #
#                                                                                   #
#    This program is free software: you can redistribute it and/or modify           #
#    it under the terms of the GNU General Public License as published by           #
#    the Free Software Foundation, either version 3 of the License, or              #
#    (at your option) any later version.                                            #
#                                                                                   #
#    This program is distributed in the hope that it will be useful,                #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#    GNU General Public License for more details.                                   #
#                                                                                   #
#    You should have received a copy of the GNU General Public License              #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.         #
#                                                                                   #
#####################################################################################

import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from termCol import *

#######################################
# i2C Display Initialization. DO NOT ALTER!
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

def dispclear():
    disp.clear()
    disp.display()

def dispappexit(LanguageSet):
    image = Image.open("img/"+LanguageSet+"/AppExit.ppm").convert('1')
    disp.image(image)
    disp.display()

def dispappstart(LanguageSet):
    image = Image.open("img/"+LanguageSet+"/AppLaunch.ppm").convert('1')
    disp.image(image)
    disp.display()

def dispimg(img):
    image = Image.open(img).convert('1')
    disp.image(image)
    disp.display()

#def disptext():
    #disp.clear()
    #disp.display()
    #image = "lol"
    #image = image.transpose(Image.FLIP_LEFT_RIGHT)
    #disp.image(image)
    #disp.display()

def ERR999(LanguageSet):
    idlevar = 0
    image = Image.open("img/"+LanguageSet+"/ERR999.ppm").convert('1')
    print(Base.FAILRED, "ERROR! Code: 999\n This application has a manufacturer lock and cannot be started.", Base.END)
    disp.image(image)
    disp.display()
    while GPIO.input(homeb) == True:
        idlevar = 1