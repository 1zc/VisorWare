###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
###############################################################################


#                     VisorWare BETA || Built for Visor2.0                    #


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
from termCol import *

print("Reading configuration file...")
cfgp = 'cfg.txt'
cfgfile = open(cfgp, 'r+')

if cfgfile.read(1) == '0':
    os.system("clear")
    print("First time VisorWare is being launched.")
    print(Base.WARNING,"Running first-time setup. THIS WILL TAKE A VERY LONG TIME!", Base.END)
    print("")
    print(Base.FAILRED,"Setup will start in 15 seconds. Please do not abort/interrupt the setup process. If you would like to cancel, please do it in these 15 seconds by hitting CTRL+C.", Base.END)
    time.sleep(15)

    # Runs the RaspbianDebloater script to get rid of all bloatware.
    os.system('sudo apt-get --yes remove --purge wolfram-engine sense-hat scratch nuscratch scratch2 sonic-pi minecraft-pi python-minecraftpi penguinspuzzle xpdf libreoffice libreoffice-base libreoffice-base-core libreoffice-base-drivers')
    os.system('sudo apt-get --yes remove --purge libreoffice-calc libreoffice-common libreoffice-core libreoffice-draw libreoffice-gtk libreoffice-impress libreoffice-math libreoffice-writer claws-mail')
    os.system('sudo apt-get --yes remove --purge geany-common geany greenfoot bluej nodered python3-thonny sense-emu-tools epiphany-browser-data epiphany-browser dillo')
    os.system('sudo apt-get autoremove -y && sudo apt-get autoclean -y')
    # Updates repositories and installs all updates available for currently installed software.
    os.system('sudo apt-get update')
    os.system('sudo apt-get --yes upgrade')
    # Installing VisorWare dependencies.
    os.system('sudo apt-get --yes --force-yes install python-imaging python-smbus git')
    os.system('git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git')
    os.system('cd Adafruit_Python_SSD1306 && sudo python3 setup.py install')
    os.system('rm Adafruit_Python_SSD1306 -r -f')
    # Installing screenfetch.
    os.system('sudo cp sf/screenfetch /usr/bin/screenfetch')
    os.system('sudo chmod 755 /usr/bin/screenfetch')
    # Configuring sound interfaces.
    #
    #   TO DO:
    #       > Update ~./asoundrc
    #       > Update /boot/config.txt

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
    print("cfgfile good. Continuing...")
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
image = Image.open('img/splash.ppm').convert('1')
disp.image(image)
disp.display()

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

print ("\n\n\nVisorWare Beta.\n\n")

print (Base.FAILRED,"THIS IS AN BETA VERSION. BEWARE OF BUGS.", Base.END)
print (Base.WARNING,"Proper functionality cannot be guaranteed in a BETA build of VisorWare. Please install a stable version of VisorWare for stable and proper functionality.\n\n", Base.END)


print ("[VOICE-ENGINE] : VOICE RECOGNITION TESTING LIVE!")
print("[INTERFACE] : To enter button-interface testing, hold the Home Button until the Voice-Engine exits.")

MenuItem1 = 0  # Voice-Engine.
MenuItem2 = 0  # Settings.
MenuItem3 = 0  # Power.
MenuItem4 = 0  # BLANK AND UNUSED.
MenuItem5 = 0  # BLANK AND UNUSED.

ButtonPressDelay = 0.2

# APPLICATIONS: #####################################################
def APPPower(): # Application function that allows options for power control.
    PowerItem1 = 1 # Shutdown
    PowerItem2 = 0 # Reboot
    PowerItem3 = 0 # Force quit VisorWare
    PowerItem4 = 0 # Exit to menu
    PowerExit = 0
    while PowerExit == 0:
        if PowerItem1 == 1:
            image = Image.open('img/POWERReboot.ppm').convert('1')
            disp.image(image)
            disp.display()

        elif PowerItem2 == 1:
            image = Image.open('img/POWERShutdown.ppm').convert('1')
            disp.image(image)
            disp.display()

        elif PowerItem3 == 1:
            image=Image.open('img/POWERQuit.ppm').convert('1')
            disp.image(image)
            disp.display()

        elif PowerItem4 == 1:
            image = Image.open('img/ExitToMenu.ppm').convert('1')
            disp.image(image)
            disp.display()

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
                image = Image.open('img/splash.ppm').convert('1')
                disp.image(image)
                disp.display()
                time.sleep(3)
                disp.clear()
                disp.display()
                os.system('sudo reboot')
                exit()
            elif PowerItem2 == 1:
                print(Base.WARNING, '[POWER] : SHUTTING DOWN', Base.END)
                image = Image.open('img/splash.ppm').convert('1')
                disp.image(image)
                disp.display()
                time.sleep(3)
                disp.clear()
                disp.display()
                os.system('sudo halt')
                exit()
            elif PowerItem3 == 1:
                print(Base.FAILRED, '[POWER] : Quitting VisorWare.', Base.END)
                image = Image.open('img/splash.ppm').convert('1')
                disp.image(image)
                disp.display()
                time.sleep(3)
                image = Image.open('img/POWERQuitConsequence.ppm').convert('1')
                disp.image(image)
                disp.display()
                exit()
            elif PowerItem4 == 1:
                PowerExit = 1
            time.sleep(ButtonPressDelay)

    print('[POWER] : Exiting Power options and returning to menu.')
    image = Image.open('img/AppExit.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.5)

def APPSettings(): # Application function that controls settings.
    SettingsItem1 = 1  # Update
    SettingsItem2 = 0  # System Stats
    SettingsItem3 = 0  # Exit to menu
    SettingsItem4 = 0  # BLANK AND UNUSED.
    SettingsExit = 0

    while SettingsExit == 0:
        if SettingsItem1 == 1:
            image = Image.open('img/SETTINGUpdate.ppm').convert('1')
            disp.image(image)
            disp.display()

        elif SettingsItem2 == 1:
            image = Image.open('img/SETTINGStats.ppm').convert('1')
            disp.image(image)
            disp.display()

        elif SettingsItem3 == 1:
            image = Image.open('img/ExitToMenu.ppm').convert('1')
            disp.image(image)
            disp.display()

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
                image = Image.open('img/SETTINGUpdating.ppm').convert('1')
                disp.image(image)
                disp.display()
                os.system('sudo apt-get update')
                # !!! TO DO: ADD VisorWare update system. !!! 
                print(Base.WARNING, '[SETTINGS] : Completed Update process.', Base.END)
                image = Image.open('img/SETTINGCompUpdate.ppm').convert('1')
                disp.image(image)
                disp.display()
                time.sleep(3)

            elif SettingsItem2 == 1:
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
                    time.sleep(.1)

            elif SettingsItem3 == 1:
                SettingsExit = 1
            time.sleep(ButtonPressDelay)

    print('[SETTINGS] : Exiting Settings and returning to menu.')
    image = Image.open('img/AppExit.ppm').convert('1')
    disp.image(image)
    disp.display()
    time.sleep(0.5)

def VoiceEngine(): # Application function for the AcoustiVisor app.
    import aiy.audio
    import aiy.cloudspeech
    import aiy.voicehat
    import signDictionary
    recognizer = aiy.cloudspeech.get_recognizer()
    aiy.audio.get_recorder().start()

    while GPIO.input(homeb) == True:
        print('[VOICE-ENGINE] : Listening!')
        image = Image.open('img/VEListening.ppm').convert('1')
        disp.image(image)
        disp.display()
        text = recognizer.recognize()
        image = Image.open('img/VEIdle.ppm').convert('1')
        disp.image(image)
        disp.display()
        if text is None:
                print('[VOICE-ENGINE] : Input was unrecognizable.')
        else:
            print(Base.WARNING, '[VOICE-ENGINE] : Recognized << "', text, '" >>', Base.END)
            signDictionary.signRender(text)

    image = Image.open('img/AppExit.ppm').convert('1')
    disp.image(image)
    disp.display()
    print("[VOICE-ENGINE] : Quitting Voice-Engine.")
    time.sleep(0.5)

#####################################################################

print("[INTERFACE] : Main Menu is live.")
MenuItem1 = 1

while True:
    if MenuItem1 == 1:
        image = Image.open('img/Acoustivisor.ppm').convert('1')
        disp.image(image)
        disp.display()

    elif MenuItem2 == 1:
        image = Image.open('img/Settings.ppm').convert('1')
        disp.image(image)
        disp.display()

    elif MenuItem3 == 1:
        image = Image.open('img/Power.ppm').convert('1')
        disp.image(image)
        disp.display()


    if GPIO.input(leftb) == False:
        print('[INTERFACE] : Button-Press --> LEFT')
        if MenuItem1 == 1:
            MenuItem3 = 1
            MenuItem2 = 0
            MenuItem1 = 0
        elif MenuItem2 == 1:
            MenuItem1 = 1
            MenuItem3 = 0
            MenuItem2 = 0
        elif MenuItem3 == 1:
            MenuItem2 = 1
            MenuItem1 = 0
            MenuItem3 = 0
        time.sleep(ButtonPressDelay)

    elif GPIO.input(rightb) == False:
        print('[INTERFACE] : Button-Press --> RIGHT')
        if MenuItem1 == 1:
            MenuItem2 = 1
            MenuItem3 = 0
            MenuItem1 = 0
        elif MenuItem2 == 1:
            MenuItem3 = 1
            MenuItem1 = 0
            MenuItem2 = 0
        elif MenuItem3 == 1:
            MenuItem1 = 1
            MenuItem2 = 0
            MenuItem3 = 0
        time.sleep(ButtonPressDelay)

    elif GPIO.input(homeb) == False:
        print('[INTERFACE] : Button-Press --> HOME')
        if MenuItem1 == 1:
            print(Base.WARNING, "[INTERFACE] : Launching Acoustivisor.", Base.END)
            image = Image.open('img/AppLaunch.ppm').convert('1')
            disp.image(image)
            disp.display()
            time.sleep(0.5)  
            VoiceEngine()
        elif MenuItem2 == 1:
            print(Base.WARNING, "[INTERFACE] : Launching Settings.", Base.END)
            image = Image.open('img/AppLaunch.ppm').convert('1')
            disp.image(image)
            disp.display()
            time.sleep(0.5)
            APPSettings()
        elif MenuItem3 == 1:
            print(Base.WARNING, "[INTERFACE] : Launching PowerSettings.", Base.END)
            image = Image.open('img/AppLaunch.ppm').convert('1')
            disp.image(image)
            disp.display()
            time.sleep(0.5)
            APPPower()
        time.sleep(ButtonPressDelay)
