import math
import time
import datetime
from PIL import ImageFont
from luma.core.render import canvas
from VisionEngine import *

font = ImageFont.truetype("fonts/roboto.ttf", 12)
device = get_device()

##################################################
# Button input board initialization. DO NOT ALTER!
GPIO.setmode(GPIO.BCM)
ButtonPressDelay = 0.2 # Latency of registering button presses.
leftb = 17
homeb = 27
rightb = 22
screenb = 4
GPIO.setup(leftb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(homeb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(screenb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
##################################################

def posn(angle, arm_length):
    dx = int(math.cos(math.radians(angle)) * arm_length)
    dy = int(math.sin(math.radians(angle)) * arm_length)
    return (dx, dy)

def clckscrn():
    today_last_time = "Unknown"
    if screenOff == False:
        while (GPIO.input(leftb) == True) and (GPIO.input(rightb) == True):
            if GPIO.input(screenb) == False:
                screenOff = True
            now = datetime.datetime.now()
            today_date = now.strftime("%d %b %y")
            today_time = now.strftime("%H:%M:%S")
            if today_time != today_last_time:
                today_last_time = today_time
                with canvas(device) as draw:
                    now = datetime.datetime.now()
                    today_date = now.strftime("%d %b %y")

                    margin = 4

                    cx = 30
                    cy = min(device.height, 64) / 2

                    left = cx - cy
                    right = cx + cy

                    hrs_angle = 270 + (30 * (now.hour + (now.minute / 60.0)))
                    hrs = posn(hrs_angle, cy - margin - 7)

                    min_angle = 270 + (6 * now.minute)
                    mins = posn(min_angle, cy - margin - 2)

                    sec_angle = 270 + (6 * now.second)
                    secs = posn(sec_angle, cy - margin - 2)

                    draw.ellipse((left + margin, margin, right - margin, min(device.height, 64) - margin), outline="white")
                    draw.line((cx, cy, cx + hrs[0], cy + hrs[1]), fill="white")
                    draw.line((cx, cy, cx + mins[0], cy + mins[1]), fill="white")
                    draw.line((cx, cy, cx + secs[0], cy + secs[1]), fill="red")
                    draw.ellipse((cx - 2, cy - 2, cx + 2, cy + 2), fill="white", outline="white")
                    draw.text((2 * (cx + margin), cy - 8), today_date, font=font, fill="yellow")
                    draw.text((2 * (cx + margin), cy + 8), today_time, font=font, fill="yellow")

            time.sleep(0.1)

    if screenOff == True:
        VisionEngine.sspnd()  
        while screenOff == True:
            if GPIO.input(screenb) == False:
                screenOff = False
                print("[VISIONENGINE] : Exited suspended state.")
                time.sleep(ButtonPressDelay) 