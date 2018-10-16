import time
import RPi.GPIO as GPIO
import os
import subprocess
import requests
import math
from termCol import *
import VWUtils

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

currversion = '1610201810'

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

##################################################
# Button input board initialization. DO NOT ALTER!
GPIO.setmode(GPIO.BCM)
leftb = 17
homeb = 27
rightb = 22
GPIO.setup(leftb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(homeb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
##################################################

def SettingsInterface(LanguageSet):
    global currversion
    setLang = LanguageSet
    ButtonPressDelay = 0.2
    SettingsItem1 = 1  # Update
    SettingsItem2 = 0  # System Stats
    SettingsItem3 = 0  # Language
    SettingsItem4 = 0  # Exit to menu
    SettingsItem5 = 0  # BLANK AND UNUSED.
    SettingsExit = 0

    while SettingsExit == 0:
        if SettingsItem1 == 1:
            VWUtils.dispimg("img/"+setLang+"/SETTINGUpdate.ppm")

        elif SettingsItem2 == 1:
            VWUtils.dispimg("img/"+setLang+"/SETTINGStats.ppm")
     
        elif SettingsItem3 == 1:
            if setLang == "en":
                VWUtils.dispimg("img/en/SETTINGLanguage.ppm")
            elif setLang == "ar":
                VWUtils.dispimg("img/ar/SETTINGLanguage.ppm")

        elif SettingsItem4 == 1:
            VWUtils.dispimg("img/"+setLang+"/ExitToMenu.ppm")

        if GPIO.input(leftb) == False:
            print('[INTERFACE] : Button-Press --> LEFT')
            if SettingsItem1 == 1:
                SettingsItem4 = 1
                SettingsItem3 = 0
                SettingsItem2 = 0
                SettingsItem1 = 0
            elif SettingsItem2 == 1:
                SettingsItem1 = 1
                SettingsItem3 = 0
                SettingsItem4 = 0
                SettingsItem2 = 0
            elif SettingsItem3 == 1:
                SettingsItem2 = 1
                SettingsItem1 = 0
                SettingsItem4 = 0
                SettingsItem3 = 0
            elif SettingsItem4 == 1:
                SettingsItem3 = 1
                SettingsItem2 = 0
                SettingsItem1 = 0
                SettingsItem4 = 0
            time.sleep(ButtonPressDelay)

        elif GPIO.input(rightb) == False:
            print('[INTERFACE] : Button-Press --> RIGHT')
            if SettingsItem1 == 1:
                SettingsItem2 = 1
                SettingsItem4 = 0
                SettingsItem3 = 0
                SettingsItem1 = 0
            elif SettingsItem2 == 1:
                SettingsItem3 = 1
                SettingsItem1 = 0
                SettingsItem4 = 0
                SettingsItem2 = 0
            elif SettingsItem3 == 1:
                SettingsItem4 = 1
                SettingsItem1 = 0
                SettingsItem2 = 0
                SettingsItem3 = 0
            elif SettingsItem4 == 1:
                SettingsItem1 = 1
                SettingsItem2 = 0
                SettingsItem3 = 0
                SettingsItem4 = 0
            time.sleep(ButtonPressDelay)

        elif GPIO.input(homeb) == False:
            print('[INTERFACE] : Button-Press --> HOME')
            if SettingsItem1 == 1:
                print(Base.WARNING, '[SETTINGS] : Commencing update process.', Base.END)
                print(Base.WARNING, '[SYSTEM] : DO NOT TURN OFF THE POWER OR ATTEMPT TO INTERRUPT THE UPDATE PROCESS.', Base.END)
                VWUtils.dispimg("img/"+setLang+"/SETTINGUpdating.ppm")
                if VWUtils.connCheck() == True:
                    print('\n[SYSTEM] : Updating package repositories...\n')
                    os.system('sudo apt-get update')
                    print('\n[SYSTEM] : Installing new packages...\n')
                    os.system('sudo apt-get --yes upgrade')
                    #
                    # vmark.txt uses the following format: DDMMYYYYxy
                    #       where, DD = Date (01, 11, 31,)
                    #              MM = Month (01, 12)
                    #              YYYY = Year (2018)
                    #              xy = Version No. (v1.2, where x=1,y=2.)
                    #
                    print('\n\n[SYSTEM] : Removing old vmark file...')
                    os.system('sudo rm cfg/vmark.txt -f')
                    print('\n[SYSTEM] : Getting new vmark file...')
                    os.system('cd cfg && wget https://raw.githubusercontent.com/LiamZC/VisorWare/master/src/cfg/vmark.txt')
                    print("\n[SYSTEM] : Reading new vmark file...")
                    vmark = 'cfg/vmark.txt'
                    vmarkfile = open(vmark, 'r+')
                    if vmarkfile.read(10) == currversion:
                        vmarkfile.close()
                        print(Base.OKGREEN, '[SYSTEM] : VisorWare software is up to date.', Base.END)
                        VWUtils.dispimg("img/"+setLang+"/SETTINGCompUpdate.ppm")
                    else:
                        vmarkfile.close() 
                        print(Base.WARNING, '[SYSTEM] : A new version of the VisorWare software is available. Updating...', Base.END)
                        try:
                            print('Shutting down VisorWare for updates.')         
                            exit()
                        finally:
                            os.system('cd /home/pi/VWUD && python3 VWCTRL.py') 
                            
                elif VWUtils.connCheck() == False:
                    print("Failed to connect to the internet. Aborting...")
                    VWUtils.dispimg("img/"+setLang+"/NoConn.ppm")
                    time.sleep(2)

                print(Base.WARNING, '[SETTINGS] : Finished Update process. Returning to menu.', Base.END)
                time.sleep(3)

            elif SettingsItem2 == 1:
                VWUtils.dispappstart()
                time.sleep(0.5)
                print(Base.WARNING, '[SETTINGS] : Showing system stats.', Base.END)
                image = Image.new('1', (128, 64))
                draw = ImageDraw.Draw(image)
                draw.rectangle((0,0,128,64), outline=0, fill=0)
                time.sleep(0.5)
                while GPIO.input(homeb) == True:
                    draw.rectangle((0,0,128,64), outline=0, fill=0)
                    cmd = "hostname -I | cut -d\' \' -f1"
                    IP = subprocess.check_output(cmd, shell = True )
                    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
                    CPU = subprocess.check_output(cmd, shell = True )
                    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
                    MemUsage = subprocess.check_output(cmd, shell = True )
                    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
                    Disk = subprocess.check_output(cmd, shell = True )

                    draw.text((x, top),       "IP: " + (IP.decode('utf-8')),  font=font, fill=255)
                    draw.text((x, top+8),     (CPU.decode('utf-8')), font=font, fill=255)
                    draw.text((x, top+16),    (MemUsage.decode('utf-8')),  font=font, fill=255)
                    draw.text((x, top+25),    (Disk.decode('utf-8')),  font=font, fill=255)

                    disp.image(image)
                    disp.display()
                    time.sleep(.03)
                print(Base.WARNING, '[SETTINGS] : Finished Update process. Returning to menu.', Base.END)
                VWUtils.dispappexit()
                time.sleep(0.5)

            elif SettingsItem3 == 1:
                VWUtils.dispappstart()
                time.sleep(0.5)
                if LanguageSet == "en":
                    print("Changing language to Arabic.")
                    setLang = "ar"
                    
                elif LanguageSet == "ar":
                    print("Changing language to English.")
                    setLang = "en"
                    

            elif SettingsItem4 == 1:
                SettingsExit = 1
            time.sleep(ButtonPressDelay)

    return setLang