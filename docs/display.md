# [VisorWare Documentation](https://github.com/1zc/VisorWare/tree/master/docs)
### display.md || Displays, compatibility and interfacing

We're now going to take a detailed look at connecting OLED display modules to the Pi, and how VisorWare interacts and works with these displays.

## OLED Display Basics

OLED display modules come in many different forms, resolutions and configurations. It is important to know what driver your OLED uses, its resolution and its data configuration. You will know what driver your display uses when you get it, the most common drivers being SSD1306 and SH1106 drivers. To check if your display driver and resolution is compatible with VisorWare, check the [official SOLED GitHub page](https://github.com/1zc/SOLED). 

The Raspberry Pi uses the SPI or i2C bus to interact with display modules. Display modules are usually configured to use either of these buses to transfer data. You'll need to identify what your display module is configured to use before moving on with setting up the Raspberry Pi.

To identify what configuration you will be using, you'll need to look at the number of pins your display module uses. If your display module has 4 pins (VCC, GND, SCK, SDA), your display is configured to use the i2C interface. If your display has 7 pins (VCC, GND, RST/RES, CS, DC), your display is configured to use the SPI interface.

Now that you know what configuration you'll be using, we need to setup the Raspberry Pi before moving on to wiring up the display to the Pi.

## Configuring the Raspberry Pi

We'll need to enable the i2C or SPI interfaces (depending on which one you need) in Raspbian. This is fairly simple to do. Open a terminal and enter:

> sudo raspi-config

Next, head over to *INTERFACING OPTIONS*, select i2C or SPI and enable them. You can then use the RIGHT ARROW key to navigate the BACK button, then to the FINISH button. It may ask you to reboot, answer yes to that.

The Pi should now be able to communicate with our OLED display modules. Next, we'll take a look at how to connect the display modules to the Raspberry Pi's GPIO pins.

## Connecting the Display Module

The connections to the Pi's GPIO pins are few and simple. A good guide on connecting your display to the Pi is available [at Adafruit.](https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black/wiring)


**For i2C Displays, follow these pin connections:**

Display Module Pin | Raspberry Pi Pin
------------ | -------------
GND (Ground) | Any GND (Ground) pin on the Raspberry Pi
VCC or VIN | Raspberry Pi 3.3v pin (3v3 Pin)
SCL | Raspberry Pi SCL Pin (GPIO#8 Pin)
SDA | Raspberry Pi SDA Pin (GPIO#9 Pin)



**For SPI Displays, follow these pin connections:**

Display Module Pin | Raspberry Pi Pin
------------ | -------------
GND (Ground) | Any GND (Ground) pin on the Raspberry Pi
VCC or VIN | Raspberry Pi 3.3v pin (3v3 Pin)
RST | Raspberry Pi GPIO#24 Pin
CS | Raspberry Pi CE0 Pin (GPIO#10 Pin)
DC | Raspberry Pi GPIO#23 Pin
D0 or CLK | Raspberry Pi SCLK Pin (GPIO#14 Pin)
D1 or DATA | Raspberry Pi MOSI Pin (GPIO#12 Pin)

Check your connections and ensure everything is correct. From here, you can now finish setting up the rest of the hardware for VisorWare from the [docs/devsetup.md file in the VisorWare GitHub repository.](https://github.com/1zc/VisorWare/blob/master/docs/devsetup.md)


Further in this document, we will take an advanced dive into what software VisorWare uses to interact with these displays.

## The S.O.L.E.D Display Drivers

**This document will be expanded in the near future.**