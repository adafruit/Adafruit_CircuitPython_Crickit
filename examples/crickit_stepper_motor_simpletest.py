# Crickit library demo - stepper motor

import time

from adafruit_crickit import crickit
from adafruit_motor import stepper

# Step motor forward and then backward.
while True:
    crickit.stepper_motor.onestep(direction=stepper.FORWARD)
    time.sleep(1)
    crickit.stepper_motor.onestep(direction=stepper.BACKWARD)
    time.sleep(1)
