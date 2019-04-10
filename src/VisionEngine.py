# VisionEngine - Graphical Rendering Engine for VisorWare supported hardware.
# Packaged with VisorWare, a project by Liam Z. Charles.

#####################################################################################
#                                                                                   #
#    VisionEngine - Graphical Rendering Engine for VisorWare supported hardware.    #
#    Copyright (C) 2019  Liam Z. Charles | All Rights Reserved                      #
#                                                                                   #
#  >>> UNAUTHORIZED DISTRIBUTION and UNAUTHORIZED MODIFICATION                      #
#      of this software is NOT ALLOWED.                                             #
#                                                                                   #
#####################################################################################

import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

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
    disp.image(image)
    disp.display()

def sspnd():
    clr()
    time.sleep(0.3)
    print("[VISIONENGINE] : Display suspended. Press suspend button again to exit suspended state.")

def disptext(s1, s2, s3, s4, off1, off2, off3, off4, debugStatus, UTFDecode): 
    # s1,s2,s3,s4 are the strings to be printed. 
    # #off1,off2,off3,off4 are the vertical offset distances between the strings. 
    # UTFDecode ('8' for UTF-8) decides the mode of string decode.
    image = Image.new('1',  (disp.width, disp.height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
    if UTFDecode == '8':
        draw.text((x, top+off1), s1.decode('utf-8'),  font=font, fill=255)
        draw.text((x, top+off2), s2.decode('utf-8'),  font=font, fill=255)
        draw.text((x, top+off3), s3.decode('utf-8'),  font=font, fill=255)
        draw.text((x, top+off4), s4.decode('utf-8'),  font=font, fill=255)
    else:
        draw.text((x, top+off1), s1,  font=font, fill=255)
        draw.text((x, top+off2), s2,  font=font, fill=255)
        draw.text((x, top+off3), s3,  font=font, fill=255)
        draw.text((x, top+off4), s4,  font=font, fill=255)

    if debugStatus == True:
        disp.image(image)
        disp.display()    
    else:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
        disp.image(image)
        disp.display()  
        
