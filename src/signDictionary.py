# Sign-Dictionary module v1.0.
# Packaged with a demo version of VisorWare, a project by Liam Z. Charles.


print('Loading dictionary of signs...')

#####################################################################################
#                                                                                   #
#    SignDictionary.py - Module for rendering ASL Translations for VisorWare Demo.  #
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

import math
import time
import os

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import VisionEngine
from VisionEngine import *


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


EndDelay = 1.5
AlphaDelay = 0.5

# Special Chars ################################
def blankSpace():
    VisionEngine.clr()
    time.sleep(0.3)

# Alphabets ####################################
def letterA():
    VisionEngine.render("dictionary/A.ppm", False)
    time.sleep(AlphaDelay)

def letterB():
    VisionEngine.render("dictionary/B.ppm", False)
    time.sleep(AlphaDelay)

def letterC():
    VisionEngine.render("dictionary/C.ppm", False)
    time.sleep(AlphaDelay)

def letterD():
    VisionEngine.render("dictionary/D.ppm", False)
    time.sleep(AlphaDelay)

def letterE():
    VisionEngine.render("dictionary/E.ppm", False)
    time.sleep(AlphaDelay)

def letterF():
    VisionEngine.render("dictionary/F.ppm", False)
    time.sleep(AlphaDelay)

def letterG():
    VisionEngine.render("dictionary/G.ppm", False)
    time.sleep(AlphaDelay)

def letterH():
    VisionEngine.render("dictionary/H.ppm", False)
    time.sleep(AlphaDelay)

def letterI():
    VisionEngine.render("dictionary/I.ppm", False)
    time.sleep(AlphaDelay)

def letterJ():
    VisionEngine.render("dictionary/J.ppm", False)
    time.sleep(AlphaDelay)

def letterK():
    VisionEngine.render("dictionary/K.ppm", False)
    time.sleep(AlphaDelay)

def letterL():
    VisionEngine.render("dictionary/L.ppm", False)
    time.sleep(AlphaDelay)

def letterM():
    VisionEngine.render("dictionary/M.ppm", False)
    time.sleep(AlphaDelay)

def letterN():
    VisionEngine.render("dictionary/N.ppm", False)
    time.sleep(AlphaDelay)

def letterO():
    VisionEngine.render("dictionary/O.ppm", False)
    time.sleep(AlphaDelay)

def letterP():
    VisionEngine.render("dictionary/P.ppm", False)
    time.sleep(AlphaDelay)

def letterQ():
    VisionEngine.render("dictionary/Q.ppm", False)
    time.sleep(AlphaDelay)

def letterR():
    VisionEngine.render("dictionary/R.ppm", False)
    time.sleep(AlphaDelay)

def letterS():
    VisionEngine.render("dictionary/S.ppm", False)
    time.sleep(AlphaDelay)

def letterT():
    VisionEngine.render("dictionary/T.ppm", False)
    time.sleep(AlphaDelay)

def letterU():
    VisionEngine.render("dictionary/U.ppm", False)
    time.sleep(AlphaDelay)

def letterV():
    VisionEngine.render("dictionary/V.ppm", False)
    time.sleep(AlphaDelay)

def letterW():
    VisionEngine.render("dictionary/W.ppm", False)
    time.sleep(AlphaDelay)

def letterX():
    VisionEngine.render("dictionary/X.ppm", False)
    time.sleep(AlphaDelay)

def letterY():
    VisionEngine.render("dictionary/Y.ppm", False)
    time.sleep(AlphaDelay)

def letterZ():
    VisionEngine.render("dictionary/Z.ppm", False)
    time.sleep(AlphaDelay)
################################################

def hello():
    VisionEngine.render("dictionary/Hello1.ppm", False)
    time.sleep(0.05)
    VisionEngine.render("dictionary/Hello2.ppm", False)
    time.sleep(0.05)
    VisionEngine.render("dictionary/Hello3.ppm", False)
    time.sleep(0.05)
    VisionEngine.render("dictionary/Hello4.ppm", False)
    time.sleep(0.05)
    VisionEngine.render("dictionary/Hello5.ppm", False)
    time.sleep(0.05)
    VisionEngine.render("dictionary/Hello6.ppm", False)
    time.sleep(0.05)
    VisionEngine.render("dictionary/Hello7.ppm", False)
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def yes():
    VisionEngine.render("dictionary/Yes1.ppm", False)
    time.sleep(0.3)
    VisionEngine.render("dictionary/Yes2.ppm", False)
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def how():
    VisionEngine.render("dictionary/How1.ppm", False)
    time.sleep(0.3)
    VisionEngine.render("dictionary/How1.ppm", False)
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def you():
    VisionEngine.render("dictionary/You1.ppm", False)
    time.sleep(0.05)
    VisionEngine.render("dictionary/You2.ppm", False)
    time.sleep(0.05)
    VisionEngine.render("dictionary/You3.ppm", False)
    time.sleep(0.05)
    VisionEngine.render("dictionary/You4.ppm", False)
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def no():
    VisionEngine.render("dictionary/No1.ppm", False)
    time.sleep(0.3)
    VisionEngine.render("dictionary/No1.ppm", False)
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def friend():
    VisionEngine.render("dictionary/Friend1.ppm", False)
    time.sleep(0.3)
    VisionEngine.render("dictionary/Friend1.ppm", False)
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def signRender(txt):
    data = txt.split()
    for temp in data:
        WordRec = 0  # Variable that keeps track of whether a word has been recognized.
        if 'hello' in temp:
            WordRec = 1
            hello()
        elif 'yes' in temp:
            WordRec = 1
            yes()
        elif 'how' in temp:
            WordRec = 1
            how()
        elif 'you' in temp:
            WordRec = 1
            you()
        elif 'no' in temp:
            WordRec = 1
            no()
        elif 'friend' in temp:
            WordRec = 1
            friend()

        if WordRec == 0:           
            for letter in temp:
                if (letter == 'a') or (letter == 'A'):
                    letterA()
                elif (letter == 'b') or (letter == 'B'):
                    letterB()
                elif (letter == 'c') or (letter == 'C'):
                    letterC()
                elif (letter == 'd') or (letter == 'D'):
                    letterD()
                elif (letter == 'e') or (letter == 'E'):
                    letterE()
                elif (letter == 'f') or (letter == 'F'):
                    letterF()
                elif (letter == 'g') or (letter == 'G'):
                    letterG()
                elif (letter == 'h') or (letter == 'H'):
                    letterH()
                elif (letter == 'i') or (letter == 'I'):
                    letterI()
                elif (letter == 'j') or (letter == 'J'):
                    letterJ()
                elif (letter == 'k') or (letter == 'K'):
                    letterK()
                elif (letter == 'l') or (letter == 'L'):
                    letterL()
                elif (letter == 'm') or (letter == 'M'):
                    letterM()
                elif (letter == 'n') or (letter == 'N'):
                    letterN()
                elif (letter == 'o') or (letter == 'O'):
                    letterO()
                elif (letter == 'p') or (letter == 'P'):
                    letterP()
                elif (letter == 'q') or (letter == 'Q'):
                    letterQ()
                elif (letter == 'r') or (letter == 'R'):
                    letterR()
                elif (letter == 's') or (letter == 'S'):
                    letterS()
                elif (letter == 't') or (letter == 'T'):
                    letterT()
                elif (letter == 'u') or (letter == 'U'):
                    letterU()
                elif (letter == 'v') or (letter == 'V'):
                    letterV()
                elif (letter == 'w') or (letter == 'W'):
                    letterW()
                elif (letter == 'x') or (letter == 'X'):
                    letterX()
                elif (letter == 'y') or (letter == 'Y'):
                    letterY()
                elif (letter == 'z') or (letter == 'Z'):
                    letterZ()
            blankSpace()
                    
