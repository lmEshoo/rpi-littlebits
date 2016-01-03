# rpi-littlebits
this module is to have a raspberry pi connect to littlebits hardware

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

###ssh to the pi. 
* `pi@<IP>` it will prompt you say yes then type the password


###index.html
* change the index.html file to the correct IP address 

###to run
`sudo python Desktop/server.py 3030`
