import time
import RPi.GPIO as GPIO
import os
import subprocess
import requests
import math
from termCol import *
import VWUtils
import VisionEngine

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

currversion = '1904201910'

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

def SettingsInterface(LanguageSet, ButtonPressDelay, debugStatus):
    global currversion
    setLang = LanguageSet
    ButtonPressDelay = 0.2
    SettingsItem1 = 1  # Update
    SettingsItem2 = 0  # System Stats
    SettingsItem3 = 0  # Language
    SettingsItem4 = 0  # Exit to menu
    SettingsItem5 = 0  # Version - UNDISPLAYED
    SettingsItem6 = 0  # BLANK AND UNALLOCATED
    SettingsExit = 0

    while SettingsExit == 0:
        if SettingsItem1 == 1:
            VisionEngine.render("img/"+setLang+"/SETTINGUpdate.ppm", debugStatus)

        elif SettingsItem2 == 1:
            VisionEngine.render("img/"+setLang+"/SETTINGStats.ppm", debugStatus)
     
        elif SettingsItem3 == 1:
            if setLang == "en":
                VisionEngine.render("img/en/SETTINGLanguage.ppm", debugStatus)
            elif setLang == "ar":
                VisionEngine.render("img/ar/SETTINGLanguage.ppm", debugStatus)

        elif SettingsItem4 == 1:
            VisionEngine.render("img/"+setLang+"/ExitToMenu.ppm", debugStatus)

        #elif SettingsItem5 == 1:
            #VisionEngine.dispimg("img/"+setLang+"/Version.ppm")

        if GPIO.input(leftb) == False:
            print('[INTERFACE] : Button-Press --> LEFT')
            if SettingsItem1 == 1:
                #SettingsItem5 = 1
                SettingsItem4 = 1
                SettingsItem3 = 0
                SettingsItem2 = 0
                SettingsItem1 = 0
            elif SettingsItem2 == 1:
                SettingsItem1 = 1
                SettingsItem3 = 0
                SettingsItem4 = 0
                #SettingsItem5 = 0
                SettingsItem2 = 0
            elif SettingsItem3 == 1:
                SettingsItem2 = 1
                SettingsItem1 = 0
                SettingsItem4 = 0
                #SettingsItem5 = 0
                SettingsItem3 = 0
            elif SettingsItem4 == 1:
                SettingsItem3 = 1
                SettingsItem2 = 0
                SettingsItem1 = 0
                #SettingsItem5 = 0
                SettingsItem4 = 0
            #elif SettingsItem5 == 1:
                #SettingsItem4 = 1
                #SettingsItem5 = 0
                #SettingsItem1 = 0
                #SettingsItem3 = 0
                #SettingsItem2 = 0
            time.sleep(ButtonPressDelay)

        elif GPIO.input(rightb) == False:
            print('[INTERFACE] : Button-Press --> RIGHT')
            if SettingsItem1 == 1:
                SettingsItem2 = 1
                SettingsItem4 = 0
                #SettingsItem5 = 0
                SettingsItem3 = 0
                SettingsItem1 = 0
            elif SettingsItem2 == 1:
                SettingsItem3 = 1
                SettingsItem1 = 0
                #SettingsItem5 = 0
                SettingsItem4 = 0
                SettingsItem2 = 0
            elif SettingsItem3 == 1:
                SettingsItem4 = 1
                SettingsItem1 = 0
                #SettingsItem5 = 0
                SettingsItem2 = 0
                SettingsItem3 = 0
            elif SettingsItem4 == 1:
                #SettingsItem5 = 1
                SettingsItem1 = 1
                SettingsItem2 = 0
                SettingsItem3 = 0
                SettingsItem4 = 0
            #elif SettingsItem5 == 1:
                #SettingsItem1 = 1
                #SettingsItem5 = 0
                #SettingsItem2 = 0
                #SettingsItem3 = 0
                #SettingsItem4 = 0
            time.sleep(ButtonPressDelay)

        elif GPIO.input(homeb) == False:
            print('[INTERFACE] : Button-Press --> HOME')
            if SettingsItem1 == 1:
                print(Base.WARNING, '[SETTINGS] : Commencing update process.', Base.END)
                print(Base.WARNING, '[SYSTEM] : DO NOT TURN OFF THE POWER OR ATTEMPT TO INTERRUPT THE UPDATE PROCESS.', Base.END)
                VisionEngine.render("img/"+setLang+"/SETTINGUpdating.ppm", debugStatus)
                if VWUtils.connCheck() == True:
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
                        VisionEngine.render("img/"+setLang+"/SETTINGCompUpdate.ppm", debugStatus)
                    else:
                        vmarkfile.close() 
                        print(Base.WARNING, '[SYSTEM] : A new version of the VisorWare software is available.', Base.END)
                        time.sleep(0.2)
                        uddb = 1
                        udcn = 1
                        udcy = 0
                        while uddb == 1:   
                            if udcn == 1:
                                VisionEngine.render("img/"+LanguageSet+"/udcn.ppm", debugStatus)
                            elif udcy == 1:
                                VisionEngine.render("img/"+LanguageSet+"/udcy.ppm", debugStatus)

                            if GPIO.input(leftb) == False:
                                if udcn == 1:
                                    udcy = 1
                                    udcn = 0
                                elif udcy == 1:
                                    udcn = 1
                                    udcy = 0
                                time.sleep(ButtonPressDelay)

                            elif GPIO.input(rightb) == False:
                                if udcn == 1:
                                    udcy = 1
                                    udcn = 0
                                elif udcy == 1:
                                    udcn = 1
                                    udcy = 0
                                time.sleep(ButtonPressDelay)

                            elif GPIO.input(homeb) == False:
                                if udcn == 1:
                                    uddb = 0
                                elif udcy == 1:
                                    print(Base.WARNING, "[SYSTEM] : UPDATING...", Base.END)
                                    try:
                                        print("Shutting down VisorWare for updates.")
                                        VisionEngine.render("img/"+LanguageSet+"/SETTINGUpdating.ppm", debugStatus)
                                        exit()
                                    finally:
                                        os.system('cd /home/pi/VWUD && python3 VWCTRL.py')

                        print("[SYSTEM] : Update dialog box closed.")
                            
                elif VWUtils.connCheck() == False:
                    print("Failed to connect to the internet. Aborting...")
                    VisionEngine.render("img/"+setLang+"/NoConn.ppm", debugStatus)
                    time.sleep(2)

                time.sleep(3)

            elif SettingsItem2 == 1:
                VisionEngine.appStart(setLang, debugStatus)
                print(Base.WARNING, '[SETTINGS] : Showing system stats.', Base.END)
                time.sleep(0.5)
                while GPIO.input(homeb) == True:                    
                    cmd = "hostname -I | cut -d\' \' -f1"
                    IP = subprocess.check_output(cmd, shell = True)
                    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
                    CPU = subprocess.check_output(cmd, shell = True )
                    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
                    MemUsage = subprocess.check_output(cmd, shell = True )
                    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
                    Disk = subprocess.check_output(cmd, shell = True )

                    VisionEngine.disptext(IP,CPU,MemUsage,Disk,0,15,27,39,debugStatus,'8')
                    time.sleep(.03)
                print(Base.WARNING, '[SETTINGS] : Exiting system stats.', Base.END)
                VisionEngine.appExit(setLang, debugStatus)
                time.sleep(0.5)

            elif SettingsItem3 == 1:
                VisionEngine.appStart(setLang, debugStatus)
                time.sleep(0.5)
                if LanguageSet == "en":
                    print("Changing language to Arabic.")
                    setLang = "ar"
                    
                elif LanguageSet == "ar":
                    print("Changing language to English.")
                    setLang = "en"
                    

            elif SettingsItem4 == 1:
                SettingsExit = 1

            elif SettingsItem5 == 1:
                print("Version -> ", currversion)

            time.sleep(ButtonPressDelay)

    return setLang