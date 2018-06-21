# Crickit library demo - Drive terminals

import time
from adafruit_crickit import crickit

# Turn on Drive 1 for 1 second
while True:
    crickit.drive[1].duty_cycle = 65535
    time.sleep(1)
    crickit.drive[1].duty_cycle = 0
    time.sleep(1)
