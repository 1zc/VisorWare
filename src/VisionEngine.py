# VisionEngine - Graphical Rendering Engine for VisorWare supported hardware.
# Packaged with VisorWare, a project by Liam Z. Charles.

#####################################################################################
#                                                                                   #
#    VisionEngine - Graphical Rendering Engine for VisorWare supported hardware.    #
#    Copyright (C) 2019  Liam Z. Charles                                            #
#                                                                                   #
#    This program is free software: you can redistribute it and/or modify           #
#    it under the terms of the GNU Affero General Public License as published       #
#    by the Free Software Foundation, either version 3 of the License, or           #
#    (at your option) any later version.                                            #
#                                                                                   #
#    This program is distributed in the hope that it will be useful,                #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#    GNU Affero General Public License for more details.                            #
#                                                                                   #
#    You should have received a copy of the GNU Affero General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.         #
#                                                                                   #
#####################################################################################

import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import SOLED
import Adafruit_SSD1306

import sys
import logging
import time

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

logging.basicConfig(
    level=logging.CRITICAL,
    format='%(asctime)-15s - %(message)s'
)
logging.getLogger('PIL').setLevel(logging.CRITICAL)

#######################################
# Display Initialization. DO NOT ALTER!
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
#disp = SOLED.R128x64(rst=RST)
#disp = SOLED.R96x48(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000)) ### FOR SPI
disp.begin()
width = disp.width
height = disp.height
padding = -2
top = padding
bottom = height=padding
x = 0
fontsize = 12
font = ImageFont.truetype("fonts/roboto.ttf", fontsize)
disp.clear()
disp.display()
#
#######################################

# INFORMATION ON PARAMETERS:
#
# > imagePath = Directory of the image file. Example: img/test.ppm
# > debugStatus = Bool variable. If true, the display will display stuff correctly 
#                 for a testing scenario. Example: Display on a Breadboard.
# > LanguageSet = Use 'en' for English. Used by VisorWare to display images from
#                 correct languages.

def renderFlip(imagePath):
    image = Image.open(imagePath).convert('1')
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    disp.image(image)
    disp.display()

def render(imagePath, debugStatus):
    image = Image.open(imagePath).convert('1')
    if debugStatus == True:
        renderFlip(imagePath)        
    else:
        disp.image(image)
        disp.display()

def clr():
    disp.clear()
    disp.display()

def appExit(LanguageSet, debugStatus):
    imagePath = "img/"+LanguageSet+"/AppExit.ppm"
    render(imagePath, debugStatus)

def appStart(LanguageSet, debugStatus):
    imagePath = "img/"+LanguageSet+"/AppLaunch.ppm"
    render(imagePath, debugStatus)

def dispimg(img):
    image = Image.open(img).convert('1')
    image = image.resize((width, height))
    disp.image(image)
    disp.display()

def sspnd():
    clr()
    time.sleep(0.3)
    print("[VISIONENGINE] : Display suspended. Press suspend button again to exit suspended state.")

def disptext(s1, s2, s3, s4, x1, x2, x3, x4, y1, y2, y3, y4, debugStatus, UTFDecode): 
    # s1,s2,s3,s4 are the strings to be printed. 
    # y1,y2,y3,y4 are the vertical offset distances between the strings. 
    # x1,x2,x3,x4 are the horizontal offset distances from the left-end of display. 
    # UTFDecode ('8' for UTF-8) decides the mode of string decode.
    image = Image.new('1',  (disp.width, disp.height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
    if UTFDecode == '8':
        draw.text((x+x1, top+y1), s1.decode('utf-8'),  font=font, fill=255)
        draw.text((x+x2, top+y2), s2.decode('utf-8'),  font=font, fill=255)
        draw.text((x+x3, top+y3), s3.decode('utf-8'),  font=font, fill=255)
        draw.text((x+x4, top+y4), s4.decode('utf-8'),  font=font, fill=255)
    else:
        draw.text((x+x1, top+y1), s1,  font=font, fill=255)
        draw.text((x+x2, top+y2), s2,  font=font, fill=255)
        draw.text((x+x3, top+y3), s3,  font=font, fill=255)
        draw.text((x+x4, top+y4), s4,  font=font, fill=255)

    if debugStatus == True:
        disp.image(image)
        disp.display()    
    else:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
        disp.image(image)
        disp.display()  
        
