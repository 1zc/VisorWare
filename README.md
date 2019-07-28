# [VisorWare](https://github.com/1zc/VisorWare)
VisorWare is a Linux-based system software designed to run on wearable devices with a glasses/spectacles form-factor. Being compatible with small OLED and TFT displays, VisorWare is capable of providing a comfortable user experience with its simple user-interface and **planned** functional application installation/management systems.

### Pre-requisites / device setup
To use and develop VisorWare, we will need to setup a proper base environment with the required hardware. You will need:

• A Raspberry Pi with the latest Raspbian installed on a minimum 4GB SD card. All Pi models work.

• A small, monochrome OLED display. (Currently only supports 'SSD1306 128x64' OLED displays. More displays will be added)

• Four buttons, wired up to 'GPIO4', 'GPIO17', 'GPIO27', and 'GPIO22'. These buttons will be used to navigate through menus and interact with software. (GPIO17 serves as the left button, GPIO27 middle and GPIO22 right | the button at GPIO4 is not necessary.)


Refer to the [docs/devsetup.md](https://github.com/1zc/VisorWare/tree/master/docs/devsetup.md) file in the documentation directory of this GitHub repository for detailed information regarding setting up your device requirements.


### Installation
Let's get down to installing VisorWare. To make things easier, VisorWare has its own simple first-time setup and configuration. You will need your Pi to be connected to a working internet connection. **The first-time setup removes a lot of pre-installed software from the standard Raspbian image, so it's best to install VisorWare on a clean image to prevent any loss of data**


#### Step One: Cloning VisorWare from the official GitHub.
The first thing we need to do is to clone VisorWare from the GitHub repository. This can be done simply by entering the following command into the terminal:
> git clone https://github.com/1zc/VisorWare


#### Step Two: Entering the VisorWare src directory.
Now that we've cloned the repository, lets enter our newly-created local directory.
> cd VisorWare

We need to go deeper to access the main source file, 'VW.py', which is located in the src directory.

> cd src


#### Step Three: Starting the first-time setup.
When we start 'VW.py' with 'sudo' rights, the terminal will be cleared and first-time setup's dialog will be displayed. The setup begins about 20 seconds after the dialog is shown, and takes a *very long time* to complete. Once setup is complete, the Pi will reboot and VisorWare should start displaying on the connected OLED display.

You can start the setup by entering:
> sudo python3 VW.py

**MAKE SURE ITS RUN WITH 'sudo python3' AND NOT WITH 'python'!**

Now, find a good game to play or a nice video on YouTube to watch. Maybe even get yourself a cup of coffee. This process can take a long time!

### Usage

If setup has completed without any fatal errors and VisorWare is running on your OLED display, we've completed installation!

VisorWare is meant to be as simple as possible to use. Use the three main buttons (the ones we wired up to GPIO17,27,22 earlier) to navigate the menus and open applications/sub-menus. You can shut-down or reboot the device through the Power settings on the main menu, and check out core system-stats and even do a software update from the Settings app!

The dedicated apps currently available with VisorWare (such as the Weather app and Clock screen) are not yet configurable from VisorWare directly. This will be added in future updates as VisorWare is being developed. For further details on using VisorWare, refer to the [docs/usage.md](https://github.com/1zc/VisorWare/tree/master/docs/usage.md) file in the documentation directory.

# Questions/Issues

> Thank you for checking out VisorWare! I'm currently working on this alone, so I apologize if development and documentation is not always fast/detailed. I will be adding information on how contributions can be done in the near future, after documentation on individual core components of the software have been fully released. If you'd like to ask me questions or point out issues, you can use the [issues section](https://github.com/1zc/VisorWare/issues) of the GitHub repository or contact me on twitter @LiamZCharles or on reddit /u/Infranix!
