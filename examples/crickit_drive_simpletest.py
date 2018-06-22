# Crickit library demo - Drive terminals

import time
from adafruit_crickit.terminals import DRIVE1
from adafruit_crickit.crickit import crickit

drive1 = crickit.digital_out(DRIVE1)
# Turn on Drive 1 for 1 second and then off for 1 second
while True:
    drive1.value = True
    time.sleep(1)
    drive1.value = False
    time.sleep(1)
