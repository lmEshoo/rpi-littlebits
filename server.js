#!/usr/bin/env python

import web
import RPi.GPIO as GPIO

#no warnings
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

urls = ('/','root')
app = web.application(urls,globals())

class root:

	def __init__(self):
		self.hello = "piweee welcome!"

	def GET(self):
		getInput = web.input(turn="")
		kommando = str(getInput.turn)
		if kommando == "on":
			# set RPi board pins high
			GPIO.output(7, GPIO.HIGH)
			GPIO.output(11, GPIO.HIGH)
			return "Lights on"
		if kommando == "off":
			# set RPi board pins low
			GPIO.output(7, GPIO.LOW)
			GPIO.output(11, GPIO.LOW)
			return "Lights off"

if __name__ == "__main__":
	app.run()
