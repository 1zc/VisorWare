# VisionEngine - Graphical Rendering Engine for VisorWare supported hardware.
# Packaged with VisorWare, a project by Liam Z. Charles.

#####################################################################################
#                                                                                   #
#    VisionEngine - Graphical Rendering Engine for VisorWare supported hardware.    #
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

def renderFlip(imagePath):
    image = Image.open(imagePath).convert('1')
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    disp.image(image)
    disp.display()

def render(imagePath, debugStatus):
    image = Image.open(imagePath).convert('1')
    if debugStatus == True:
        disp.image(image)
        disp.display()
    else:
        renderFlip(image)

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

def disptext(s1, s2, s3, s4, off1, off2, off3, off4):
    image = Image.new('1',  (disp.width, disp.height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)

    draw.text((x, top+off1), s1.decode('utf-8'),  font=font, fill=255)
    draw.text((x, top+off2), s2.decode('utf-8'),  font=font, fill=255)
    draw.text((x, top+off3), s3.decode('utf-8'),  font=font, fill=255)
    draw.text((x, top+off4), s4.decode('utf-8'),  font=font, fill=255)

    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    disp.image(image)
    disp.display()
