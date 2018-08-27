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


RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
width = disp.width
height = disp.height
GPIO.setmode(GPIO.BCM)

def hello():
    image = Image.open('dictionary/Hello1.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/Hello2.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/Hello3.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/Hello4.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/Hello5.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/Hello6.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/Hello7.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(2.5)
    disp.clear()
    disp.display()

def yes():
    image = Image.open('dictionary/Yes1.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(1)
    image = Image.open('dictionary/Yes2.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(2.5)
    disp.clear()
    disp.display()

def how():
    image = Image.open('dictionary/How1.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/How2.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(2.5)
    disp.clear()
    disp.display()

def you():
    image = Image.open('dictionary/You1.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/You2.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/You3.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/You4.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(2.5)
    disp.clear()
    disp.display()

def no():
    image = Image.open('dictionary/No1.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/No2.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(2.5)
    disp.clear()
    disp.display()

def friend():
    image = Image.open('dictionary/Friend1.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.3)
    image = Image.open('dictionary/Friend2.ppm').convert('1')
    disp.image(image)
    disp.display()
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