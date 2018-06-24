# Crickit library demo - Capacitive touch

import time
from adafruit_crickit.terminals import TOUCH1
from adafruit_crickit.crickit import crickit

# Create touch object.
touch1 = crickit.touch(TOUCH1)

while True:
    if touch1.value:
        print("Touched terminal Touch 1")
    time.sleep(0.25)
