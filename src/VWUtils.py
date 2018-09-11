# VWUtils - contains utility functions.
# Packaged with VisorWare, a project by Liam Z. Charles.

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

def dispappexit():
    image = Image.open('img/AppExit.ppm').convert('1')
    disp.image(image)
    disp.display()

def dispappstart():
    image = Image.open('img/AppLaunch.ppm').convert('1')
    disp.image(image)
    disp.display()

def dispimg(img):
    image = Image.open(img).convert('1')
    disp.image(image)
    disp.display()



