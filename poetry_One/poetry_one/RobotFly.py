#!/usr/bin/python3

from pysabertooth import Sabertooth
from flask import Flask, render_template

from time import sleep

# on the beaglebone related boards, use a known, working UART port on the headers.

# For instance, attach P9_21 to S1 on the sabertooth 2 x 12 and attach GND on the sabertooth to GND on your BBB.
# "/dev/ttyS2" has changed in time. Check for changes...

saber = Sabertooth("/dev/ttyS2", baudrate=9600, address=128, timeout=0.1)

# start and enable a service, start a cron job, or make an executable .sh file for use when booting into this file.

app = Flask(__name__)
@app.route("/")
@app.route("/<state>")

while True:
    sleep(0.4)
    if state == "F":
        print ("Robot Moving Forward")
        saber.drive(1, 100)
        saber.drive(2, 100)

    if state == "R":
        print ("Robot Turning Right")
        saber.drive(1, 75)
        saber.drive(2, 25)

    if state == "L":
        print ("Robot Turning Left")
        saber.drive(1, 25)
        saber.drive(2, 75)

    if state == "S":
        print ("Robot Stopped")
        saber.drive(1, 0)
        saber.drive(2, 0)
        saber.stop()

    template_data = {
        "title" : state,
    }
    return render_template("Saber.html", **template_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
