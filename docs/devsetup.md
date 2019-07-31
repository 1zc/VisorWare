# [VisorWare Documentation](https://github.com/1zc/VisorWare/tree/master/docs)
## devsetup.md || Pre-requisites and device setup

Let's take a good look at how to set up the required base environment to run VisorWare. First, let's take a look at the Raspberry Pi and how to configure it for the rest of the requirements.

### Setting up the Raspberry Pi

• Let's start with the basics - the operating system. We highly recommend Raspbian Stretch, as VisorWare is currently being officially tested on it. You can download the latest Raspbian from [the official Raspberry Pi website.](https://www.raspberrypi.org/downloads/raspbian/) Use a software like [Etcher](http://etcher.io) to flash Raspbian onto an SD card of **MINIMUM** 4GB.

• Hook up your newly-flashed SD card to your Raspberry Pi. Once you've booted in, the first thing you need to do is connect to a working internet connection. The internet connection is **ESSENTIAL** for VisorWare's setup to run.

• To interact with OLED displays, the Raspberry Pi uses either the i2C bus or SPI bus - depending on what your display module is configured to use. Refer to [/docs/display.md](https://github.com/1zc/VisorWare/blob/master/docs/display.md) for information on how to correctly identify, setup and work with your display module.

With this much done, the Pi will be ready for the next steps.

### Wiring up the required components

VisorWare does not require much in terms of electronic components. All it needs is an SSD1306 OLED display and 4 buttons.

• For a detailed guide on wiring up the SSD1306 OLED display, [refer to the /docs/display.md documentation file.](https://github.com/1zc/VisorWare/blob/master/docs/display.md) Keep in mind, VisorWare will not be able to launch if a display is not connected correctly.

• Let's take a look at the four buttons we need. Wire up three buttons to GPIO17, GPIO27 and GPIO22 respectively. The button connected to GPIO17 is the LEFT button, GPIO27 acts as the middle ENTER/SELECT button, and GPIO22 is the RIGHT button. The fourth button isn't totally required, but serves a useful purpose and can be wired to the GPIO4 pin. This fourth button acts as a display off button, used to insantly hide the display from vision when the user needs to concentrate/needs no distractions.

With the display and buttons wired up, we now have our setup complete! *It is alright to add any more components you'd like, as long as they do not use the same GPIO pins used by the display and buttons!*

