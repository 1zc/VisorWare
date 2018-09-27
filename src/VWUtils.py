# VWUtils - contains utility functions.
# Packaged with VisorWare, a project by Liam Z. Charles.

#####################################################################################
#                                                                                   #
#    VWUtils.py - Module for provision of various utility functions for VisorWare.  #
#    Copyright (C) 2018  Liam Z. Charles                                            #
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

import socket

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

def connCheck(): # Checks for availability of internet connection.
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

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



