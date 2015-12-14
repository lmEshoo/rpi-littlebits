# rpi-littlebits
this module is to have a raspberry pi connect to littlebits hardware

###installation
```install:

sudo apt-get update && sudo apt-get upgrade
sudo apt-get install nodejs npm
git clone git://github.com/quick2wire/quick2wire-gpio-admin.git
cd quick2wire-gpio-admin
make
sudo make install
sudo adduser $USER gpio
npm config set registry http://registry.npmjs.org```
