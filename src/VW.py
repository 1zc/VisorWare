###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
#                                                                             #
#                              github.com/1zc                                 #
###############################################################################


# $$$$$$$$$$$$$$$$$$$$$$$$$ || VisorWare v1.00 || $$$$$$$$$$$$$$$$$$$$$$$$$$$ #

currversion = '1907201910'

#####################################################################################
#                                                                                   #
#    VW.py - Core software for VisorWare.                                           #
#    Copyright (C) 2019  Liam Z. Charles                                            #
#                                                                                   #
#    This program is free software: you can redistribute it and/or modify           #
#    it under the terms of the GNU Affero General Public License as published       #
#    by the Free Software Foundation, either version 3 of the License, or           #
#    (at your option) any later version.                                            #
#                                                                                   #
#    This program is distributed in the hope that it will be useful,                #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#    GNU Affero General Public License for more details.                            #
#                                                                                   #
#    You should have received a copy of the GNU Affero General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.         #
#                                                                                   #
#####################################################################################

import time
import RPi.GPIO as GPIO
import os
import subprocess
import requests
import math
import VWUtils
from termCol import *

print("Reading saved language settings...")
lang = 'cfg/langcfg.txt'
langfile = open(lang, 'r+')

if langfile.read(2) == 'ar':
    LanguageSet = 'ar'
    print("Saved Language = ar")
else:
    LanguageSet = "en"
    print("Saved Language = en")
langfile.close()

print("Reading configuration file...")
cfgp = 'cfg/cfg.txt'
cfgfile = open(cfgp, 'r+')

if cfgfile.read(1) == '0':
    cfgfile.close()
    os.system("clear")
    print(Base.FAILRED,'____   ____.__                    __      __                        ', Base.END)
    print(Base.FAILRED,'\   \ /   /|__| _________________/  \    /  \_____ _______   ____   ', Base.END)
    print(Base.FAILRED,' \   Y   / |  |/  ___/  _ \_  __ \   \/\/   /\__  \\_  __ \_/ __ \  ', Base.END)
    print(Base.FAILRED,'  \     /  |  |\___ (  <_> )  | \/\        /  / __ \|  | \/\  ___/  ', Base.END)
    print(Base.FAILRED,'   \___/   |__/____  >____/|__|    \__/\  /  (____  /__|    \___  > ', Base.END)
    print(Base.FAILRED,'                   \/                   \/        \/            \/  ', Base.END)
    print("")
    print("First time VisorWare is being launched.")
    print(Base.WARNING,"Running first-time setup. THIS WILL TAKE A VERY LONG TIME!", Base.END)
    print("")
    print(Base.FAILRED,"Setup will start in 20 seconds. Please do not abort/interrupt the setup process. If you would like to cancel, please do it in these 20 seconds by using CTRL+C.", Base.END)
    print(Base.BOLD, "A WORKING INTERNET CONNECTION IS REQUIRED!", Base.END)
    time.sleep(20)
    if VWUtils.connCheck() == True:
        # Runs the RaspbianDebloater script to get rid of all bloatware.
        print('\n\nRemoving bloat...\n')
        os.system('sudo apt-get --yes remove --purge wolfram-engine sense-hat scratch nuscratch scratch2 sonic-pi minecraft-pi python-minecraftpi xpdf libreoffice libreoffice-base libreoffice-base-core libreoffice-base-drivers')
        os.system('sudo apt-get --yes remove --purge libreoffice-calc libreoffice-common libreoffice-core libreoffice-draw libreoffice-gtk libreoffice-impress libreoffice-math libreoffice-writer claws-mail')
        os.system('sudo apt-get --yes remove --purge geany-common geany greenfoot bluej nodered python3-thonny sense-emu-tools epiphany-browser-data epiphany-browser dillo')
        os.system('sudo apt-get autoremove -y && sudo apt-get autoclean -y')
        os.system('sudo apt autoremove -y && sudo apt autoclean -y')
        print(ANSI.Color(120), "\nDONE.", ANSI.END)
        # Updates repositories and installs all updates available for currently installed software.
        print('\n\nUpdating...\n')
        os.system('sudo apt-get update')
        os.system('sudo apt-get --yes upgrade')
        print(ANSI.Color(120), "\nDONE.", ANSI.END)
        # Installing VisorWare dependencies.
        print('\n\nInstalling VisorWare dependencies...\n')
        os.system('sudo apt-get --yes --force-yes install python3-dev python-imaging python-smbus git')
        os.system('sudo apt-get --yes --force-yes install libfreetype6-dev libjpeg-dev build-essential')
        os.system('sudo apt-get --yes --force-yes install git')
        os.system('sudo apt-get --yes --force-yes install bluetooth libbluetooth-dev bluez python-bluetooth python-bluez')
        os.system('sudo dpkg -i conf/deb/libusb-dev_0.1.12-30_armhf.deb')
        os.system('sudo dpkg -i conf/deb/libopenobex1_1.5-2.1_armhf.deb')
        os.system('sudo dpkg -i conf/deb/libopenobex1-dev_1.5-2.1_armhf.deb')
        os.system('sudo sh conf/dispdriver.sh')
        print(ANSI.Color(120), "\nDONE.", ANSI.END)
        # Installing screenfetch.
        print('\n\nConfiguring screenfetch...')
        os.system('sudo cp sf/screenfetch /usr/bin/screenfetch')
        os.system('sudo chmod 755 /usr/bin/screenfetch')
        print(ANSI.Color(120), "\nDONE.", ANSI.END)
        # Configuring important interfaces.
        print('\n\nConfiguring Audio and Boot configs...')
        os.system('sudo rm /boot/config.txt -f && sudo cp conf/config.txt /boot/config.txt')
        # os.system('sudo rm /home/pi/.asoundrc -f && sudo cp conf/.asoundrc /home/pi/')
        print(ANSI.Color(120), "\nDONE.", ANSI.END)
        # Installing VW Update service files.
        print('\n\nConfiguring VWUD configs...')
        os.system('cd /home/pi/ && mkdir VWUD')
        os.system('cd /home/pi/VWUD && mkdir temp')
        os.system('sudo cp conf/VWCTRL.py /home/pi/VWUD/VWCTRL.py')
        os.system('sudo cp conf/cfg.txt /home/pi/VWUD/cfg.txt')
        print(ANSI.Color(120), "\nDONE.", ANSI.END)
        # Configuring start-up interfaces.
        print('\n\nConfiguring Start-Up Interfaces...\n')
        os.system('sudo chmod u+x /home/pi/VisorWare/launcher.sh')
        os.system('sudo cp conf/lzc_visorware.service /etc/systemd/system/lzc_visorware.service')
        os.system('sudo systemctl daemon-reload')
        os.system('sudo systemctl enable lzc_visorware.service')
        os.system('sudo systemctl start lzc_visorware.service')
        os.system('sudo systemctl disable apt-daily.service')
        os.system('sudo systemctl disable apt-daily-upgrade.service')
        print(ANSI.Color(120), "\nDONE.", ANSI.END)
        
        cfgfile = open(cfgp, 'w')
        cfgfile.write('1')
        cfgfile.close()

        print(Base.OKGREEN,"SETUP HAS BEEN COMPLETE!", Base.END)
        print(Base.WARNING,"VisorWare will now reboot in 10 seconds!", Base.END)
        time.sleep(10)
        os.system('sudo reboot')
        exit()

    else:
        cfgfile.close()
        print(Base.FAILRED, '\nFIRST TIME SETUP FAILED. NO ACTIVE INTERNET CONNECTION DETECTED.', Base.END)
        print(Base.WARNING, 'Please set up your internet connection before running this program.', Base.END)
        exit()

else:
    print("CFG is good. Continuing with startup...")
    cfgfile.close()

# Core Variable Initialization ######################################
MenuItem1 = 0  # AcoustiVisor
MenuItem2 = 0  # Settings.
MenuItem3 = 0  # Power.
MenuItem4 = 0  # Weather App.
MenuItem5 = 0  # Clock Screen.
MenuItem6 = 0  # BLANK AND UNUSED

debugStatus = True
screenOff = False
MenuItem1 = 1
#####################################################################

import VisionEngine
import errorHandle

print("Launching VisorWare...\n")
VisionEngine.render("img/"+LanguageSet+"/crsplash.ppm", debugStatus)
time.sleep(2)
VisionEngine.render("img/"+LanguageSet+"/splash.ppm", debugStatus)
time.sleep(3)

###################################
# APPLICATION-SPECIFIC DEPENDENCIES AND SETUP:
#import aiy.audio
#import aiy.cloudspeech
#import aiy.voicehat
#import signDictionary
#recognizer = aiy.cloudspeech.get_recognizer()
#aiy.audio.get_recorder().start()
###################################

###################################
# CORE APPLICATION IMPORTS:
import vwapps.common.VWSet as VWSet
import vwapps.pkgs.VWWeather as VWWeather
#import vwapps.pkgs.VWClck as VWClck
###################################

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

os.system('clear')
print("VisorWare | Copyright (C) 2019  Liam Z. Charles")
print("Unauthorized modification, redistribution of this software")
print("is NOT permitted.\n\n")
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
print (Base.FAILRED,"This is a development version of VisorWare.", Base.END)

# APPLICATIONS: #####################################################
def APPPower(): # Application function that allows options for power control.
    PowerItem1 = 1 # Shutdown
    PowerItem2 = 0 # Reboot
    PowerItem3 = 0 # Force quit VisorWare
    PowerItem4 = 0 # Exit to menu
    PowerExit = 0
    screenOff = False
    while PowerExit == 0:
        if screenOff == False:
            if PowerItem1 == 1:
                VisionEngine.render("img/"+LanguageSet+"/POWERReboot.ppm", debugStatus)

            elif PowerItem2 == 1:
                VisionEngine.render("img/"+LanguageSet+"/POWERShutdown.ppm", debugStatus)

            elif PowerItem3 == 1:
                VisionEngine.render("img/"+LanguageSet+"/POWERQuit.ppm", debugStatus)

            elif PowerItem4 == 1:
                VisionEngine.render("img/"+LanguageSet+"/ExitToMenu.ppm", debugStatus)

            if GPIO.input(screenb) == False:
                screenOff = True

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
                    time.sleep(0.2)
                    print("[POWER] : Reboot dialog box opened.")
                    rbdb = 1
                    rbcn = 1
                    rbcy = 0
                    while rbdb == 1:   
                        if rbcn == 1:
                            VisionEngine.render("img/"+LanguageSet+"/rbcn.ppm", debugStatus)
                        elif rbcy == 1:
                            VisionEngine.render("img/"+LanguageSet+"/rbcy.ppm", debugStatus)

                        if GPIO.input(leftb) == False:
                            if rbcn == 1:
                                rbcy = 1
                                rbcn = 0
                            elif rbcy == 1:
                                rbcn = 1
                                rbcy = 0
                            time.sleep(ButtonPressDelay)

                        elif GPIO.input(rightb) == False:
                            if rbcn == 1:
                                rbcy = 1
                                rbcn = 0
                            elif rbcy == 1:
                                rbcn = 1
                                rbcy = 0
                            time.sleep(ButtonPressDelay)

                        elif GPIO.input(homeb) == False:
                            if rbcn == 1:
                                rbdb = 0
                            elif rbcy == 1:
                                print(Base.WARNING, '[POWER] : REBOOTING', Base.END)
                                VisionEngine.render("img/"+LanguageSet+"/splash.ppm", debugStatus)
                                time.sleep(3)
                                VisionEngine.clr()
                                os.system('sudo reboot')
                                exit()
                            time.sleep(ButtonPressDelay)
                    print("[POWER] : Reboot dialog box closed.")
                
                elif PowerItem2 == 1:
                    time.sleep(0.2)
                    print("[POWER] : Shutdown dialog box opened.")
                    sddb = 1
                    sdcn = 1
                    sdcy = 0
                    while sddb == 1:   
                        if sdcn == 1:
                            VisionEngine.render("img/"+LanguageSet+"/sdcn.ppm", debugStatus)
                        elif sdcy == 1:
                            VisionEngine.render("img/"+LanguageSet+"/sdcy.ppm", debugStatus)

                        if GPIO.input(leftb) == False:
                            if sdcn == 1:
                                sdcy = 1
                                sdcn = 0
                            elif sdcy == 1:
                                sdcn = 1
                                sdcy = 0
                            time.sleep(ButtonPressDelay)

                        elif GPIO.input(rightb) == False:
                            if sdcn == 1:
                                sdcy = 1
                                sdcn = 0
                            elif sdcy == 1:
                                sdcn = 1
                                sdcy = 0
                            time.sleep(ButtonPressDelay)

                        elif GPIO.input(homeb) == False:
                            if sdcn == 1:
                                sddb = 0
                            elif sdcy == 1:
                                print(Base.WARNING, "[POWER] : SHUTTING DOWN.", Base.END)
                                VisionEngine.render("img/"+LanguageSet+"/splash.ppm", debugStatus)
                                time.sleep(3)
                                VisionEngine.clr()
                                os.system('sudo halt')
                                exit()
                            time.sleep(ButtonPressDelay)

                    print("[POWER] : Shutdown dialog box closed.")

                
                elif PowerItem3 == 1:
                    print(Base.FAILRED, "[POWER] : Quitting VisorWare.", Base.END)
                    VisionEngine.render("img/"+LanguageSet+"/splash.ppm", debugStatus)
                    time.sleep(3)
                    VisionEngine.render("img/"+LanguageSet+"/POWERQuitConsequence.ppm", debugStatus)
                    exit()
                elif PowerItem4 == 1:
                    PowerExit = 1
                time.sleep(ButtonPressDelay)
        
        if screenOff == True:
            VisionEngine.sspnd()
            while screenOff == True:
                if GPIO.input(screenb) == False:
                    screenOff = False
                    print("[VISIONENGINE] : Exited suspended state.")
                    time.sleep(ButtonPressDelay) 

    print('[POWER] : Exiting Power options and returning to menu.')
    VisionEngine.appExit(LanguageSet, debugStatus)
    time.sleep(0.5)

def APPSettings(): # Application function that controls settings.
    global LanguageSet   
    LanguageSet = VWSet.SettingsInterface(LanguageSet, ButtonPressDelay, debugStatus)
    print("Saving language setting to registry.")
    langfile = open(lang, 'w')
    langfile.write(LanguageSet)
    langfile.close()

    print('[SETTINGS] : Exiting Settings and returning to the main menu.')
    VisionEngine.appExit(LanguageSet, debugStatus)
    time.sleep(0.5)

def APPWeather(): # By Nanda Gopal.
    if VWUtils.connCheck() == True:
        VWWeather.weather(debugStatus)
    elif VWUtils.connCheck() == False:
        print("Failed to connect to the internet. Aborting...")
        VisionEngine.render("img/"+LanguageSet+"/NoConn.ppm", debugStatus)
        time.sleep(2)

    print("[WEATHER] : Exiting the Weather app and returning to the main menu.")
    VisionEngine.appExit(LanguageSet, debugStatus)
    time.sleep(0.5)

def ClckScrn():
    VWClck.clckscrn(debugStatus)

def AcoustiVisor(): # Core Application function for the Speech-to-ASL Demo app.
    #if VWUtils.connCheck() == True:
        #while GPIO.input(homeb) == True:
            #print('[VOICE-ENGINE] : Listening!')
            #VisionEngine.render("img/"+LanguageSet+"/VEListening.ppm", debugStatus)
            #text = recognizer.recognize()
            #VisionEngine.render("img/"+LanguageSet+"/VEIdle.ppm", debugStatus)
            #if text is None:
                    #print('[VOICE-ENGINE] : Input was unrecognizable.')
            #else:
                #print(Base.WARNING, '[VOICE-ENGINE] : Recognized << "', text, '" >>', Base.END)
                #signDictionary.signRender(text)

    #else:
        #print("Failed to connect to the internet. Aborting...")
        #VisionEngine.render("img/"+LanguageSet+"/NoConn.ppm", debugStatus)
        #time.sleep(2)
    
    errorCode = 'LOCK999'
    errorHandle.errCode(LanguageSet, errorCode, debugStatus)
    print("[ACOUSTIVISOR] : Quitting AcoustiVisor and returning to the main menu.")
    VisionEngine.appExit(LanguageSet, debugStatus)
    time.sleep(0.5)

#####################################################################

print("[INTERFACE] : Main Menu is live.")

while True:
    if screenOff == False:
        if MenuItem1 == 1:
            VisionEngine.render("img/"+LanguageSet+"/Settings.ppm", debugStatus)
            
        elif MenuItem2 == 1:
            #ClckScrn()  
            print("yeet")         

        elif MenuItem3 == 1:
            VisionEngine.render("img/"+LanguageSet+"/Power.ppm", debugStatus)

        elif MenuItem4 == 1:
            VisionEngine.render("img/"+LanguageSet+"/Weather.ppm", debugStatus)

        elif MenuItem5 == 1:
            VisionEngine.render("img/"+LanguageSet+"/Acoustivisor.ppm", debugStatus)

        if GPIO.input(screenb) == False:
            screenOff = True

        if GPIO.input(leftb) == False:
            print('[INTERFACE] : Button-Press --> LEFT')
            if MenuItem1 == 1:
                MenuItem5 = 1
                MenuItem4 = 0
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
            elif MenuItem5 == 1:
                MenuItem4 = 1
                MenuItem3 = 0
                MenuItem2 = 0
                MenuItem1 = 0
                MenuItem5 = 0
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
                MenuItem5 = 1
                MenuItem1 = 0
                MenuItem2 = 0
                MenuItem3 = 0
                MenuItem4 = 0
            elif MenuItem5 == 1:
                MenuItem1 = 1
                MenuItem5 = 0
                MenuItem2 = 0
                MenuItem3 = 0
                MenuItem4 = 0
            time.sleep(ButtonPressDelay)

        elif GPIO.input(homeb) == False:
            print('[INTERFACE] : Button-Press --> HOME')
            if MenuItem1 == 1:
                print(Base.WARNING, "[INTERFACE] : Starting the Settings App.", Base.END)
                VisionEngine.appStart(LanguageSet, debugStatus)
                time.sleep(0.5)
                APPSettings()
                
            elif MenuItem5 == 1:
                print(Base.WARNING, "[INTERFACE] : Starting AcoustiVisor Demo App.", Base.END)
                VisionEngine.appStart(LanguageSet, debugStatus)
                time.sleep(0.5)  
                AcoustiVisor()

            elif MenuItem3 == 1:
                print(Base.WARNING, "[INTERFACE] : Starting the Power options interface.", Base.END)
                VisionEngine.appStart(LanguageSet, debugStatus)
                time.sleep(0.5)
                APPPower()

            elif MenuItem4 == 1:
                print(Base.WARNING, "[INTERFACE] : Starting Weather App.", Base.END)
                VisionEngine.appStart(LanguageSet, debugStatus)
                time.sleep(0.5)
                APPWeather()
            time.sleep(ButtonPressDelay)

    if screenOff == True:
        VisionEngine.sspnd()  
        while screenOff == True:
            if GPIO.input(screenb) == False:
                screenOff = False
                print("[VISIONENGINE] : Exited suspended state.")
                time.sleep(ButtonPressDelay) 