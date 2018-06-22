# Crickit library demo - stepper motor

import time
from adafruit_crickit.terminals import MOTOR1A, MOTOR1B, MOTOR2A, MOTOR2B
from adafruit_crickit.crickit import crickit

# A single stepper motor uses up all the motor terminals.

stepper = crickit.stepper_motor(MOTOR1A, MOTOR1B, MOTOR2A, MOTOR2B)

# Step motor forward and then backward.
while True:
    stepper.onestep(direction=stepper.FORWARD)
    time.sleep(1)
    stepper.onestep(direction=stepper.BACKWARD)
    time.sleep(1)
