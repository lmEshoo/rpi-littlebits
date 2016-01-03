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
                self.hello = "snakes on a pie!"

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
                if kommando == "off":
                        # set RPi board pins low
                        GPIO.output(7, GPIO.LOW)
                        GPIO.output(11, GPIO.LOW)
                        return """<html>
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
                                    Stop!
                                    </body>
                                    </html>
                            """
                if kommando == "right":
                    GPIO.PWM(7, 1000).start(50)
                    GPIO.output(11, GPIO.HIGH)
                    return """<html>
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
                                    right!
                                    </body>
                                    </html>
                            """
                if kommando == "left":
                    GPIO.PWM(11, 1000).start(50)
                    GPIO.output(7, GPIO.HIGH)
                    return """<html>
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
                                    left!
                                    </body>
                                    </html>
                            """
#7 is right 11 is left

if __name__ == "__main__":
        app.run()
