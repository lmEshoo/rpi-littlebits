#!/usr/bin/env python
#littleBits car

import web

import RPi.GPIO as GPIO

#dont bug me with warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

urls = ('/','root')
app = web.application(urls,globals())

class root:

        def __init__(self):
                self.hello = "Ready for HackPoly?"

        def GET(self):
                getInput = web.input(turn="")
                kommando = str(getInput.turn)
                if kommando == "on":
                        # set RPi board pins high
                        GPIO.output(7, GPIO.HIGH)
                        GPIO.output(11, GPIO.HIGH)
                        return """
                                <html>
                                <head>
                                <script>
                                function loaded()
                                {
                                    window.setTimeout(CloseMe, 5);
                                }

                                function CloseMe()
                                {
                                    window.close();
                                }
                                </script>
                                </head>
                                <body onLoad="loaded()">
                                Forward!
                                </body>
                                </html>
                                """
               
#7 is right 11 is left

if __name__ == "__main__":
        app.run()
