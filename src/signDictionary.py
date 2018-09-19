# Sign-Dictionary module v1.0.
# Packaged with a demo version of VisorWare, a project by Liam Z. Charles.


print('Loading dictionary of signs...')

#####################################################################################
#                                                                                   #
#    SignDictionary.py - Module for rendering ASL Translations for VisorWare Demo.  #
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

import math
import time
import os

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import VWUtils


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

# Alphabets ####################################
def letterA():
    VWUtils.dispimg("dictionary/A.ppm")
    time.sleep(AlphaDelay)

def letterB():
    VWUtils.dispimg("dictionary/B.ppm")
    time.sleep(AlphaDelay)

def letterC():
    VWUtils.dispimg("dictionary/C.ppm")
    time.sleep(AlphaDelay)

def letterD():
    VWUtils.dispimg("dictionary/D.ppm")
    time.sleep(AlphaDelay)

def letterE():
    VWUtils.dispimg("dictionary/E.ppm")
    time.sleep(AlphaDelay)

def letterF():
    VWUtils.dispimg("dictionary/F.ppm")
    time.sleep(AlphaDelay)

def letterG():
    VWUtils.dispimg("dictionary/G.ppm")
    time.sleep(AlphaDelay)

def letterH():
    VWUtils.dispimg("dictionary/H.ppm")
    time.sleep(AlphaDelay)

def letterI():
    VWUtils.dispimg("dictionary/I.ppm")
    time.sleep(AlphaDelay)

def letterJ():
    VWUtils.dispimg("dictionary/J.ppm")
    time.sleep(AlphaDelay)

def letterK():
    VWUtils.dispimg("dictionary/K.ppm")
    time.sleep(AlphaDelay)

def letterL():
    VWUtils.dispimg("dictionary/L.ppm")
    time.sleep(AlphaDelay)

def letterM():
    VWUtils.dispimg("dictionary/M.ppm")
    time.sleep(AlphaDelay)

def letterN():
    VWUtils.dispimg("dictionary/N.ppm")
    time.sleep(AlphaDelay)

def letterO():
    VWUtils.dispimg("dictionary/O.ppm")
    time.sleep(AlphaDelay)

def letterP():
    VWUtils.dispimg("dictionary/P.ppm")
    time.sleep(AlphaDelay)

def letterQ():
    VWUtils.dispimg("dictionary/Q.ppm")
    time.sleep(AlphaDelay)

def letterR():
    VWUtils.dispimg("dictionary/R.ppm")
    time.sleep(AlphaDelay)

def letterS():
    VWUtils.dispimg("dictionary/S.ppm")
    time.sleep(AlphaDelay)

def letterT():
    VWUtils.dispimg("dictionary/T.ppm")
    time.sleep(AlphaDelay)

def letterU():
    VWUtils.dispimg("dictionary/U.ppm")
    time.sleep(AlphaDelay)

def letterV():
    VWUtils.dispimg("dictionary/V.ppm")
    time.sleep(AlphaDelay)

def letterW():
    VWUtils.dispimg("dictionary/W.ppm")
    time.sleep(AlphaDelay)

def letterX():
    VWUtils.dispimg("dictionary/X.ppm")
    time.sleep(AlphaDelay)

def letterY():
    VWUtils.dispimg("dictionary/Y.ppm")
    time.sleep(AlphaDelay)

def letterZ():
    VWUtils.dispimg("dictionary/Z.ppm")
    time.sleep(AlphaDelay)
################################################

def hello():
    VWUtils.dispimg("dictionary/Hello1.ppm")
    time.sleep(0.05)
    VWUtils.dispimg("dictionary/Hello2.ppm")
    time.sleep(0.05)
    VWUtils.dispimg("dictionary/Hello3.ppm")
    time.sleep(0.05)
    VWUtils.dispimg("dictionary/Hello4.ppm")
    time.sleep(0.05)
    VWUtils.dispimg("dictionary/Hello5.ppm")
    time.sleep(0.05)
    VWUtils.dispimg("dictionary/Hello6.ppm")
    time.sleep(0.05)
    VWUtils.dispimg("dictionary/Hello7.ppm")
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def yes():
    VWUtils.dispimg("dictionary/Yes1.ppm")
    time.sleep(0.3)
    VWUtils.dispimg("dictionary/Yes2.ppm")
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def how():
    VWUtils.dispimg("dictionary/How1.ppm")
    time.sleep(0.3)
    VWUtils.dispimg("dictionary/How1.ppm")
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def you():
    VWUtils.dispimg("dictionary/You1.ppm")
    time.sleep(0.05)
    VWUtils.dispimg("dictionary/You2.ppm")
    time.sleep(0.05)
    VWUtils.dispimg("dictionary/You3.ppm")
    time.sleep(0.05)
    VWUtils.dispimg("dictionary/You4.ppm")
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def no():
    VWUtils.dispimg("dictionary/No1.ppm")
    time.sleep(0.3)
    VWUtils.dispimg("dictionary/No1.ppm")
    time.sleep(EndDelay)
    disp.clear()
    disp.display()

def friend():
    VWUtils.dispimg("dictionary/Friend1.ppm")
    time.sleep(0.3)
    VWUtils.dispimg("dictionary/Friend1.ppm")
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
