# Sign-Dictionary module v1.0.
# Packaged with VisorWare, a project by Liam Z. Charles.


print('Loading dictionary of signs...')

###############################################################################
#                                                                             #
#                       Copyright 2018 LIAM CHARLES                           #
#                                                                             #
#   Licensed under the Apache License, Version 2.0 (the "License");           #
#   you may not use this file except in compliance with the License.          #
#   You may obtain a copy of the License at                                   #
#                                                                             #
#               http://www.apache.org/licenses/LICENSE-2.0                    #
#                                                                             #
#   Unless required by applicable law or agreed to in writing, software       #
#   distributed under the License is distributed on an "AS IS" BASIS,         #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#   See the License for the specific language governing permissions and       #
#    limitations under the License.                                           #
#                                                                             #
###############################################################################


import math
import time
import os

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import VWCoreUtil


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
#
#######################################

def hello():
    VWCoreUtil.dispimg("dictionary/Hello1.ppm")
    time.sleep(0.15)
    VWCoreUtil.dispimg("dictionary/Hello2.ppm")
    time.sleep(0.15)
    VWCoreUtil.dispimg("dictionary/Hello3.ppm")
    time.sleep(0.15)
    VWCoreUtil.dispimg("dictionary/Hello4.ppm")
    time.sleep(0.15)
    VWCoreUtil.dispimg("dictionary/Hello5.ppm")
    time.sleep(0.15)
    VWCoreUtil.dispimg("dictionary/Hello6.ppm")
    time.sleep(0.15)
    VWCoreUtil.dispimg("dictionary/Hello7.ppm")
    time.sleep(2.5)
    disp.clear()
    disp.display()

def yes():
    VWCoreUtil.dispimg("dictionary/Yes1.ppm")
    time.sleep(1)
    VWCoreUtil.dispimg("dictionary/Yes2.ppm")
    time.sleep(2.5)
    disp.clear()
    disp.display()

def how():
    VWCoreUtil.dispimg("dictionary/How1.ppm")
    time.sleep(0.3)
    VWCoreUtil.dispimg("dictionary/How1.ppm")
    time.sleep(2.5)
    disp.clear()
    disp.display()

def you():
    VWCoreUtil.dispimg("dictionary/You1.ppm")
    time.sleep(0.3)
    VWCoreUtil.dispimg("dictionary/You2.ppm")
    time.sleep(0.3)
    VWCoreUtil.dispimg("dictionary/You3.ppm")
    time.sleep(0.3)
    VWCoreUtil.dispimg("dictionary/You4.ppm")
    time.sleep(2.5)
    disp.clear()
    disp.display()

def no():
    VWCoreUtil.dispimg("dictionary/No1.ppm")
    time.sleep(0.3)
    VWCoreUtil.dispimg("dictionary/No1.ppm")
    time.sleep(2.5)
    disp.clear()
    disp.display()

def friend():
    VWCoreUtil.dispimg("dictionary/Friend1.ppm")
    time.sleep(0.3)
    VWCoreUtil.dispimg("dictionary/Friend1.ppm")
    time.sleep(2.5)
    disp.clear()
    disp.display()

def signRender(txt):
    if 'hello' in txt:
        hello()
    elif 'yes' in txt:
        yes()
    elif 'how' in txt:
        how()
    elif 'you' in txt:
        you()
    elif 'no' in txt:
        no()
    elif 'friend' in txt:
        friend()