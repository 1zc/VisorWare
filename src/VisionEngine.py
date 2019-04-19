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

from luma.core.render import *
from luma.core import cmdline, error

import sys
import logging
import time

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s - %(message)s'
)
logging.getLogger('PIL').setLevel(logging.ERROR)

def display_settings(args):
    """
    Display a short summary of the settings.
    :rtype: str
    """
    iface = ''
    display_types = cmdline.get_display_types()
    if args.display not in display_types['emulator']:
        iface = 'Interface: {}\n'.format(args.interface)

    lib_name = cmdline.get_library_for_display_type(args.display)
    if lib_name is not None:
        lib_version = cmdline.get_library_version(lib_name)
    else:
        lib_name = lib_version = 'unknown'

    import luma.core
    version = 'luma.{} {} (luma.core {})'.format(
        lib_name, lib_version, luma.core.__version__)

    return 'Version: {}\nDisplay: {}\n{}Dimensions: {} x {}\n{}'.format(
        version, args.display, iface, args.width, args.height, '-' * 60)

def get_device(actual_args=None):
    # Create device from command-line arguments and return it.
    if actual_args is None:
        actual_args = sys.argv[1:]
    parser = cmdline.create_parser(description='luma.examples arguments')
    args = parser.parse_args(actual_args)

    if args.config:
        # Load config from file
        config = cmdline.load_config(args.config)
        args = parser.parse_args(config + actual_args)

    print(display_settings(args))

    # Create device
    try:
        device = cmdline.create_device(args)
    except error.Error as e:
        parser.error(e)

    return device

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

def disptext(s1, s2, s3, s4, y1, y2, y3, y4, debugStatus, UTFDecode): 
    # s1,s2,s3,s4 are the strings to be printed. 
    # y1,y2,y3,y4 are the vertical offset distances between the strings. 
    # x1,x2,x3,x4 are the horizontal offset distances from the left-end of display. 
    # UTFDecode ('8' for UTF-8) decides the mode of string decode.
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
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
        
