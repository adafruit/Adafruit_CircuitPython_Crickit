# Crickit library demo - servos

import time
from adafruit_crickit.terminals import SERVO1
from adafruit_crickit.crickit import crickit

servo1 = crickit.servo(SERVO1)

# Move servo back and forth 180 degrees.
while True:
    servo1.angle = 0
    time.sleep(1)
    servo1.angle = 180
    time.sleep(1)
