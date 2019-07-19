#!/bin/sh
# launcher.sh

cd /home/pi
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306 && sudo python setup.py install && sudo python3 setup.py install
cd /home/pi
rm Adafruit_Python_SSD1306 -rf

cd /home/pi
git clone https://github.com/1zc/SOLED.git
cd SOLED && sudo python setup.py install && sudo python3 setup.py install
cd /home/pi 
rm SOLED -rf
