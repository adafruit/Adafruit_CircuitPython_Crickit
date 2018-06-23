# Crickit library demo - Drive terminals

import time

from adafruit_crickit.terminals import CPX_DRIVE1
from adafruit_crickit.crickit import crickit

# Create general PWM on CPX_DRIVE1 terminal.
drive1 = crickit.pwm_out(CPX_DRIVE1)

# Turn on Drive 1 for 1 second and then off for 1 second
while True:
    drive1.fraction = 1.0
    time.sleep(1)
    drive1.fraction = 0.0
    time.sleep(1)
