# OLEDclock.py

# This program interfaces with one of Adafruit's OLED displays and a Raspberry Pi (over SPI). It displays the current 
# date (Day, Month, Year) and then scrolls to the current time. The program waits for 2 seconds between scrolls.

# Example code from the py-gaugette library... Commented by The Raspberry Pi Guy

# Imports the necessary modules
import Adafruit_SSD1306
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import sys

RST = 24

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
width = disp.width
height = disp.height
disp.clear()
disp.display()
image = Image.new('1', (width, height))
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

offset = 0 # flips between 0 and 32 for double buffering

# While loop has bulk of the code in it!

while True:

    # write the current time to the display on every other cycle
    if offset == 0:
        text = time.strftime("%A")
        draw.text((0,0), time.strftime("%A"), font=font, fill=255)
        text = time.strftime("%e %b %Y")
        #led.draw_text2(0,16,text,2)
        draw.text((0,16), time.strftime("%e %b %Y"), font=font, fill=255)
        text = time.strftime("%X")
        #led.draw_text2(0,32+4,text,3)
        draw.text((0,32+4), time.strftime("%X"), font=font, fill=255)
        disp.display()
        time.sleep(1)
    else:
        time.sleep(1)

    # vertically scroll to switch between buffers
    #for i in range(0,32):
        #offset = (offset + 1) % 64
        #led.command(led.SET_START_LINE | offset)
        #time.sleep(0.01)
