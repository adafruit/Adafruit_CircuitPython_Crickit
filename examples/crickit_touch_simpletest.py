# Crickit library demo - Capacitive touch

import time
from adafruit_crickit import crickit

# Turn on Drive 1 for 1 second
while True:
 for i in (1, 2, 3, 4):
     if crickit.touch[i]:
         print("Pad", i, "touched")
time.sleep(0.25)
