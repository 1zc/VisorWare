###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
###############################################################################


# $$$$$$$$$$$$$$$$$$$$$$$$$$ || VisorWare v1.0 || $$$$$$$$$$$$$$$$$$$$$$$$$$$ #

currversion = '1609201810'

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

import time
import RPi.GPIO as GPIO
import os
import subprocess
import requests
import math
from termCol import *
import VWUtils

print("Reading configuration file...")
cfgp = 'cfg/cfg.txt'
cfgfile = open(cfgp, 'r+')

if cfgfile.read(1) == '0':
    os.system("clear")
    print("First time VisorWare is being launched.")
    print(Base.WARNING,"Running first-time setup. THIS WILL TAKE A VERY LONG TIME!", Base.END)
    print("")
    print(Base.FAILRED,"Setup will start in 20 seconds. Please do not abort/interrupt the setup process. If you would like to cancel, please do it in these 15 seconds by hitting CTRL+C.", Base.END)
    print(Base.BOLD, "A WORKING INTERNET CONNECTION IS REQUIRED!", Base.END)
    time.sleep(20)
    if VWUtils.connCheck() == True:
        # Runs the RaspbianDebloater script to get rid of all bloatware.
        print('\n\nRemoving bloat...\n')
        os.system('sudo apt-get --yes remove --purge wolfram-engine sense-hat scratch nuscratch scratch2 sonic-pi minecraft-pi python-minecraftpi penguinspuzzle xpdf libreoffice libreoffice-base libreoffice-base-core libreoffice-base-drivers')
        os.system('sudo apt-get --yes remove --purge libreoffice-calc libreoffice-common libreoffice-core libreoffice-draw libreoffice-gtk libreoffice-impress libreoffice-math libreoffice-writer claws-mail')
        os.system('sudo apt-get --yes remove --purge geany-common geany greenfoot bluej nodered python3-thonny sense-emu-tools epiphany-browser-data epiphany-browser dillo')
        os.system('sudo apt-get autoremove -y && sudo apt-get autoclean -y')
        # Updates repositories and installs all updates available for currently installed software.
        print('\n\nUpdating...\n')
        os.system('sudo apt-get update')
        os.system('sudo apt-get --yes upgrade')
        # Installing VisorWare dependencies.
        print('\n\nInstalling VisorWare dependencies...\n')
        os.system('sudo apt-get --yes --force-yes install python-imaging python-smbus git')
        os.system('sudo sh conf/dispdriver.sh')
        # Installing screenfetch.
        print('\n\nConfiguring screenfetch.')
        os.system('sudo cp sf/screenfetch /usr/bin/screenfetch')
        os.system('sudo chmod 755 /usr/bin/screenfetch')
        # Configuring important interfaces.
        print('\n\nConfiguring Audio and Boot configs.')
        os.system('sudo rm /boot/config.txt -f && sudo cp conf/config.txt /boot/config.txt')
        os.system('sudo rm /home/pi/.asoundrc -f && sudo cp conf/.asoundrc /home/pi/')
        # Installing VW Update service files.
        print('\n\nConfiguring VWUD configs.')
        os.system('cd /home/pi/ && mkdir VWUD')
        os.system('sudo cp conf/VWCTRL.py /home/pi/VWUD/VWCTRL.py')
        os.system('sudo cp conf/UD.ppm /home/pi/VWUD/UD.ppm')
        os.system('sudo cp conf/cfg.txt /home/pi/VWUD/cfg.txt')

        cfgfile.close()
        cfgfile = open(cfgp, 'w')
        cfgfile.write('1')
        cfgfile.close()

        print(Base.OKGREEN,"SETUP HAS BEEN COMPLETE!", Base.END)
        print(Base.WARNING,"VisorWare will now reboot in 10 seconds!", Base.END)
        time.sleep(10)
        os.system('sudo reboot')
        exit()

    else:
        print(Base.FAILRED, '\nFIRST TIME SETUP FAILED. NO ACTIVE INTERNET CONNECTION DETECTED.', Base.END)
        print(Base.WARNING, 'Please set up your internet connection before running this program.', Base.END)
        exit()

else:
    print("CFG is good. Continuing with startup...")
    cfgfile.close()

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

print("Launching VisorWare...\n")
VWUtils.dispimg("img/splash.ppm")
time.sleep(5)

###################################
# APPLICATION-SPECIFIC DEPENDENCIES AND SETUP:
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import signDictionary
recognizer = aiy.cloudspeech.get_recognizer()
aiy.audio.get_recorder().start()
###################################

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

os.system('clear')
print ("                     -----------------------------------")
print (ANSI.Color(120),"                         L I A M  Z.  C H A R L E S", ANSI.END)                          
print ("                     -----------------------------------") 

print(Base.OKGREEN,'____   ____.__                    __      __                        ', Base.END)
print(Base.OKGREEN,'\   \ /   /|__| _________________/  \    /  \_____ _______   ____   ', Base.END)
print(Base.OKGREEN,' \   Y   / |  |/  ___/  _ \_  __ \   \/\/   /\__  \\_  __ \_/ __ \  ', Base.END)
print(Base.OKGREEN,'  \     /  |  |\___ (  <_> )  | \/\        /  / __ \|  | \/\  ___/  ', Base.END)
print(Base.OKGREEN,'   \___/   |__/____  >____/|__|    \__/\  /  (____  /__|    \___  > ', Base.END)
print(Base.OKGREEN,'                   \/                   \/        \/            \/  ', Base.END)

print (Base.OKGREEN,"\nVersion 1.0 | Build ",currversion , Base.END)
print (Base.FAILRED,"This is a special demo version of VisorWare. Updates can break build, please proceed with caution.", Base.END)

# Core Variables ####################################################
MenuItem1 = 0  # Voice-Engine.
MenuItem2 = 0  # Settings.
MenuItem3 = 0  # Power.
MenuItem4 = 0  # Weather App.
MenuItem5 = 0  # BLANK AND UNUSED.
MenuItem6 = 0  # BLANK AND UNUSED

ButtonPressDelay = 0.2 # Latency of registering button presses.
#####################################################################

# APPLICATIONS: #####################################################
def APPPower(): # Application function that allows options for power control.
    PowerItem1 = 1 # Shutdown
    PowerItem2 = 0 # Reboot
    PowerItem3 = 0 # Force quit VisorWare
    PowerItem4 = 0 # Exit to menu
    PowerExit = 0
    while PowerExit == 0:
        if PowerItem1 == 1:
            VWUtils.dispimg("img/POWERReboot.ppm")

        elif PowerItem2 == 1:
            VWUtils.dispimg("img/POWERShutdown.ppm")

        elif PowerItem3 == 1:
            VWUtils.dispimg("img/POWERQuit.ppm")

        elif PowerItem4 == 1:
            VWUtils.dispimg("img/ExitToMenu.ppm")

        if GPIO.input(leftb) == False:
            print('[INTERFACE] : Button-Press --> LEFT')
            if PowerItem1 == 1:
                PowerItem4 = 1
                PowerItem3 = 0
                PowerItem2 = 0
                PowerItem1 = 0
            elif PowerItem2 == 1:
                PowerItem1 = 1
                PowerItem3 = 0
                PowerItem4 = 0
                PowerItem2 = 0
            elif PowerItem3 == 1:
                PowerItem2 = 1
                PowerItem1 = 0
                PowerItem4 = 0
                PowerItem3 = 0
            elif PowerItem4 == 1:
                PowerItem3 = 1
                PowerItem2 = 0
                PowerItem1 = 0
                PowerItem4 = 0
            time.sleep(ButtonPressDelay)

        elif GPIO.input(rightb) == False:
            print('[INTERFACE] : Button-Press --> RIGHT')
            if PowerItem1 == 1:
                PowerItem2 = 1
                PowerItem3 = 0
                PowerItem4 = 0
                PowerItem1 = 0
            elif PowerItem2 == 1:
                PowerItem3 = 1
                PowerItem1 = 0
                PowerItem4 = 0
                PowerItem2 = 0
            elif PowerItem3 == 1:
                PowerItem4 = 1
                PowerItem1 = 0
                PowerItem2 = 0
                PowerItem3 = 0
            elif PowerItem4 == 1:
                PowerItem1 = 1
                PowerItem2 = 0
                PowerItem3 = 0
                PowerItem4 = 0
            time.sleep(ButtonPressDelay)

        elif GPIO.input(homeb) == False:
            print('[INTERFACE] : Button-Press --> HOME')
            if PowerItem1 == 1:
                print(Base.WARNING, '[POWER] : REBOOTING', Base.END)
                VWUtils.dispimg("img/splash.ppm")
                time.sleep(3)
                VWUtils.dispclear()
                os.system('sudo reboot')
                exit()
            elif PowerItem2 == 1:
                print(Base.WARNING, '[POWER] : SHUTTING DOWN', Base.END)
                VWUtils.dispimg("img/splash.ppm")
                time.sleep(3)
                VWUtils.dispclear()
                os.system('sudo halt')
                exit()
            elif PowerItem3 == 1:
                print(Base.FAILRED, '[POWER] : Quitting VisorWare.', Base.END)
                VWUtils.dispimg("img/splash.ppm")
                time.sleep(3)
                VWUtils.dispimg("img/POWERQuitConsequence.ppm")
                exit()
            elif PowerItem4 == 1:
                PowerExit = 1
            time.sleep(ButtonPressDelay)

    print('[POWER] : Exiting Power options and returning to menu.')
    VWUtils.dispappexit()
    time.sleep(0.5)

def APPSettings(): # Application function that controls settings.
    SettingsItem1 = 1  # Update
    SettingsItem2 = 0  # System Stats
    SettingsItem3 = 0  # Exit to menu
    SettingsItem4 = 0  # BLANK AND UNUSED.
    SettingsExit = 0

    while SettingsExit == 0:
        if SettingsItem1 == 1:
            VWUtils.dispimg("img/SETTINGUpdate.ppm")

        elif SettingsItem2 == 1:
            VWUtils.dispimg("img/SETTINGStats.ppm")

        elif SettingsItem3 == 1:
            VWUtils.dispimg("img/ExitToMenu.ppm")

        if GPIO.input(leftb) == False:
            print('[INTERFACE] : Button-Press --> LEFT')
            if SettingsItem1 == 1:
                SettingsItem3 = 1
                SettingsItem2 = 0
                SettingsItem1 = 0
            elif SettingsItem2 == 1:
                SettingsItem1 = 1
                SettingsItem3 = 0
                SettingsItem2 = 0
            elif SettingsItem3 == 1:
                SettingsItem2 = 1
                SettingsItem1 = 0
                SettingsItem3 = 0
            time.sleep(ButtonPressDelay)

        elif GPIO.input(rightb) == False:
            print('[INTERFACE] : Button-Press --> RIGHT')
            if SettingsItem1 == 1:
                SettingsItem2 = 1
                SettingsItem1 = 0
            elif SettingsItem2 == 1:
                SettingsItem3 = 1
                SettingsItem1 = 0
                SettingsItem2 = 0
            elif SettingsItem3 == 1:
                SettingsItem1 = 1
                SettingsItem2 = 0
                SettingsItem3 = 0
            time.sleep(ButtonPressDelay)

        elif GPIO.input(homeb) == False:
            print('[INTERFACE] : Button-Press --> HOME')
            if SettingsItem1 == 1:
                print(Base.WARNING, '[SETTINGS] : Commencing update process.', Base.END)
                print(Base.WARNING, '[SYSTEM] : DO NOT TURN OFF THE POWER OR ATTEMPT TO INTERRUPT THE UPDATE PROCESS.', Base.END)
                VWUtils.dispimg("img/SETTINGUpdating.ppm")
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
                else:
                    vmarkfile.close() 
                    print(Base.WARNING, '[SYSTEM] : A new version of the VisorWare software is available. Updating...', Base.END)
                    try:
                        print('Shutting down VisorWare for updates.')         
                        exit()
                    finally:
                        os.system('cd /home/pi/VWUD && python3 VWCTRL.py')  

                print(Base.WARNING, '[SETTINGS] : Completed Update process. Returning to menu.', Base.END)
                VWUtils.dispimg("img/SETTINGCompUpdate.ppm")
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
                VWUtils.dispappexit()
                time.sleep(0.5)

            elif SettingsItem3 == 1:
                SettingsExit = 1
            time.sleep(ButtonPressDelay)

    print('[SETTINGS] : Exiting Settings and returning to menu.')
    VWUtils.dispappexit()
    time.sleep(0.5)

def APPWeather():
    print("Starting live weather stream...")
    while GPIO.input(homeb) == True:
        font = ImageFont.load_default()        
        url = "http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=6d711345f94972e7ac62fc8f43cc648c&lat=24.19&lon=55.76"
        fetched_data = requests.get(url)
        fetched_data_json = fetched_data.json()
        main_data = fetched_data_json.get('main')
        current_tempK = main_data.get('temp')
        current_humidity = main_data.get('humidity')
        current_temp = round(current_tempK - 273, 1)
        image = Image.new('1', (128, 64))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,128,64), outline=0, fill=0)
        draw.text((x, top),       "Current Temp: ",  font=font, fill=255)
        draw.text((x, top+8),     (str(current_temp)),  font=font, fill=255)
        draw.text((x, top+16),    "Humidity: ",  font=font, fill=255)
        draw.text((x, top+25),    (str(current_humidity)),  font=font, fill=255)
        disp.image(image)
        disp.display()

    print("[WEATHER] : Quitting Weather and returning to the main menu.")
    VWUtils.dispappexit()
    time.sleep(0.5)

def VoiceEngine(): # Application function for the AcoustiVisor app.
    while GPIO.input(homeb) == True:
        print('[VOICE-ENGINE] : Listening!')
        VWUtils.dispimg("img/VEListening.ppm")
        text = recognizer.recognize()
        VWUtils.dispimg("img/VEIdle.ppm")
        if text is None:
                print('[VOICE-ENGINE] : Input was unrecognizable.')
        else:
            print(Base.WARNING, '[VOICE-ENGINE] : Recognized << "', text, '" >>', Base.END)
            signDictionary.signRender(text)

    print("[VOICE-ENGINE] : Quitting AcoustiVisor and returning to the main menu.")
    VWUtils.dispappexit()
    time.sleep(0.5)

#####################################################################

print("[INTERFACE] : Main Menu is live.")
MenuItem1 = 1

while True:
    if MenuItem1 == 1:
        VWUtils.dispimg("img/Acoustivisor.ppm")

    elif MenuItem2 == 1:
        VWUtils.dispimg("img/Settings.ppm")

    elif MenuItem3 == 1:
        VWUtils.dispimg("img/Power.ppm")

    elif MenuItem4 == 1:
        VWUtils.dispimg("img/Weather.ppm")


    if GPIO.input(leftb) == False:
        print('[INTERFACE] : Button-Press --> LEFT')
        if MenuItem1 == 1:
            MenuItem4 = 1
            MenuItem3 = 0
            MenuItem2 = 0
            MenuItem1 = 0            
        elif MenuItem2 == 1:
            MenuItem1 = 1
            MenuItem3 = 0
            MenuItem4 = 0
            MenuItem2 = 0            
        elif MenuItem3 == 1:
            MenuItem2 = 1
            MenuItem1 = 0
            MenuItem4 = 0
            MenuItem3 = 0            
        elif MenuItem4 == 1:
            MenuItem3 = 1
            MenuItem2 = 0
            MenuItem1 = 0
            MenuItem4 = 0
        time.sleep(ButtonPressDelay)

    elif GPIO.input(rightb) == False:
        print('[INTERFACE] : Button-Press --> RIGHT')
        if MenuItem1 == 1:
            MenuItem2 = 1
            MenuItem3 = 0
            MenuItem4 = 0
            MenuItem1 = 0
        elif MenuItem2 == 1:
            MenuItem3 = 1
            MenuItem1 = 0
            MenuItem4 = 0
            MenuItem2 = 0
        elif MenuItem3 == 1:
            MenuItem4 = 1
            MenuItem1 = 0
            MenuItem2 = 0
            MenuItem3 = 0
        elif MenuItem4 == 1:
            MenuItem1 = 1
            MenuItem2 = 0
            MenuItem3 = 0
            MenuItem4 = 0
        time.sleep(ButtonPressDelay)

    elif GPIO.input(homeb) == False:
        print('[INTERFACE] : Button-Press --> HOME')
        if MenuItem1 == 1:
            print(Base.WARNING, "[INTERFACE] : Launching Acoustivisor.", Base.END)
            VWUtils.dispappstart()
            time.sleep(0.5)  
            VoiceEngine()
        elif MenuItem2 == 1:
            print(Base.WARNING, "[INTERFACE] : Launching Settings.", Base.END)
            VWUtils.dispappstart()
            time.sleep(0.5)
            APPSettings()
        elif MenuItem3 == 1:
            print(Base.WARNING, "[INTERFACE] : Launching PowerSettings.", Base.END)
            VWUtils.dispappstart()
            time.sleep(0.5)
            APPPower()
        elif MenuItem4 == 1:
            print(Base.WARNING, "[INTERFACE] : Launching Weather.", Base.END)
            VWUtils.dispappstart()
            time.sleep(0.5)
            APPWeather()
        time.sleep(ButtonPressDelay)
