# Crickit library demo - DC motor

import time
from adafruit_crickit.terminals import MOTOR1A, MOTOR1B
from adafruit_crickit.crickit import crickit

motor = crickit.dc_motor(MOTOR1A, MOTOR1B)
# Run motor forward at full speed and then backward at half speed.
while True:
    motor.throttle = 1.0
    time.sleep(1)
    motor.throttle = -0.5
    time.sleep(1)
