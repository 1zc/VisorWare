# VisorWare Documentation 
## devsetup.md || Pre-requisites and device setup

Let's take a good look at how to set up the required base environment to run VisorWare. First, let's take a look at the Raspberry Pi and how to configure it for the rest of the requirements.

### Setting up the Raspberry Pi

• Let's start with the basics - the operating system. We highly recommend Raspbian Stretch, as VisorWare is currently being officially tested on it. You can download the latest Raspbian from [the official Raspberry Pi website.](https://www.raspberrypi.org/downloads/raspbian/) Use a software like [Etcher](http://etcher.io) to flash Raspbian onto an SD card of **MINIMUM** 4GB.

• Hook up your newly-flashed SD card to your Raspberry Pi. Once you've booted in, the first thing you need to do is connect to a working internet connection. The internet connection is **ESSENTIAL** for VisorWare's setup to run. *Optionally, you can then enable SSH from the Raspberry Pi settings or through 'sudo raspi-config' in the terminal. 

• To interact with OLED displays, the Raspberry Pi uses either the i2C bus or SPI bus - depending on what the display module is configured to use. You can find whether your OLED display is i2C or SPI by looking for info from where you bought it, or by looking at the number of pins. Typically, OLED displays using the i2C bus use 4 pins, and OLED displays using the SPI bus use 6-8 pins.

• Once you know for sure whether your display is an i2C or SPI display, you will need to go into your Raspberry Pi settings (or 'sudo raspi-config' in terminal) and enable i2C or SPI respectively in the INTERFACES category. After this, it'd be good to reboot the Pi.

With this much done, the Pi will be ready for the next steps.

### Wiring up the required components

VisorWare does not require much in terms of electronic components. All it needs is an SSD1306 OLED display and 4 buttons.

• For a detailed guide on wiring up the SSD1306 OLED display, check out [this section of a guide courtesy of Adafruit.](https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black/wiring) Keep in mind, VisorWare will not be able to launch if a display is not connected correctly.

• Let's take a look at the four buttons we need. Wire up three buttons to GPIO17, GPIO27 and GPIO22 respectively. The button connected to GPIO17 is the LEFT button, GPIO27 acts as the middle ENTER/SELECT button, and GPIO22 is the RIGHT button. The fourth button isn't totally required and can be wired to the GPIO4 pin. This fourth button acts as a display off button, used to insantly hide the display from vision when the user needs to concentrate/needs no distractions.

With the display and buttons wired up, we now have all required electronic components covered. *It is alright to add any more components you'd like, as long as they do not use the same GPIO pins used by the display and buttons!*

