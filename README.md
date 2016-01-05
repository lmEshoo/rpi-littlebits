# rpi-littlebits
this module is to have a raspberry pi connect to littlebits hardware
![](https://cloud.githubusercontent.com/assets/3256544/12077773/edfdbada-b1a9-11e5-9300-5922bfbbf3fc.JPG)

![capture2](https://cloud.githubusercontent.com/assets/3256544/12077781/37ad95f6-b1aa-11e5-9948-76ff116a495e.PNG)

###python
```
sudo apt-get install python-webpy
```

## to run:
###connect the pi to internet.
* the pi already has a wifi module connected to it.
* connect the pi to an hdmi display and sign in when prompt
* Username: `pi` password `raspberry`
* after from top right click and select wifi like picture attached ![](http://kll.engineering-news.org/kllfusion01/downloads/RPI_dhcpcd_conf.png)
* make sure in the terminal get the ip of the pi `ifconfig`
* once connected, you can unplug the monitor 

###edit index.html
* change the index.html file to the correct IP address 


###ssh to the pi. 
* `pi@<IP>` it will prompt you say yes then type the password


###edit index.html
* change the index.html file to the correct IP address 

###to run
the pi runs the following command automatically when it boots

`sudo python Desktop/server.py 3030`
