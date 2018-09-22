###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
###############################################################################


# $$$$$$$$$$$$$$$$$$$$$$$$$$ || VisorWare v1.0 || $$$$$$$$$$$$$$$$$$$$$$$$$$$ #

currversion = '2209201810'

#####################################################################################
#                                                                                   #
#    VW.py - Core VisorWare source file. (https://github.com/LiamZC/VisorWare)      #
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

###################################
# APPLICATION IMPORTS:
import vwapps.common.VWSet
import vwapps.pkgs.VWWeather
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
print("VisorWare  Copyright (C) 2018  Liam Z. Charles")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions\n\n")
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
MenuItem1 = 0  # AcoustiVisor
MenuItem2 = 0  # Settings.
MenuItem3 = 0  # Power.
MenuItem4 = 0  # Weather App.
MenuItem5 = 0  # BLANK AND UNUSED.
MenuItem6 = 0  # BLANK AND UNUSED

ButtonPressDelay = 0.2 # Latency of registering button presses.
MenuItem1 = 1
LanguageSet = 'EN'
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
    global LanguageSet
    vwapps.common.VWSet.SettingsInterface(currversion, LanguageSet)

    print('[SETTINGS] : Exiting Settings and returning to the main menu.')
    VWUtils.dispappexit()
    time.sleep(0.5)

def APPWeather(): # By Nanda Gopal.
    vwapps.pkgs.VWWeather.weather()

    print("[WEATHER] : Exiting the Weather app and returning to the main menu.")
    VWUtils.dispappexit()
    time.sleep(0.5)

def AcoustiVisor(): # Application function for the AcoustiVisor Demo app.
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

    print("[ACOUSTIVISOR] : Quitting AcoustiVisor and returning to the main menu.")
    VWUtils.dispappexit()
    time.sleep(0.5)

#####################################################################

print("[INTERFACE] : Main Menu is live.")

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
            print(Base.WARNING, "[INTERFACE] : Starting AcoustiVisor Demo App.", Base.END)
            VWUtils.dispappstart()
            time.sleep(0.5)  
            AcoustiVisor()
        elif MenuItem2 == 1:
            print(Base.WARNING, "[INTERFACE] : Starting the Settings App.", Base.END)
            VWUtils.dispappstart()
            time.sleep(0.5)
            APPSettings()
        elif MenuItem3 == 1:
            print(Base.WARNING, "[INTERFACE] : Starting the Power options interface.", Base.END)
            VWUtils.dispappstart()
            time.sleep(0.5)
            APPPower()
        elif MenuItem4 == 1:
            print(Base.WARNING, "[INTERFACE] : Starting Weather App.", Base.END)
            VWUtils.dispappstart()
            time.sleep(0.5)
            APPWeather()
        time.sleep(ButtonPressDelay)
