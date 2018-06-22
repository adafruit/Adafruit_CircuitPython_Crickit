# Crickit library demo - Signal terminals

import time
from adafruit_crickit.terminals import SIGNAL1, SIGNAL2
from adafruit_crickit.crickit import crickit
from adafruit_crickit import crickit

# Write Signal terminal 1 and read Signal terminal 2.

crickit.seesaw.pin_mode(SIGNAL1, crickit.seesaw.OUTPUT)
crickit.seesaw.pin_mode(SIGNAL2, crickit.seesaw.INPUT)

crickit.seesaw.digital_write(SIGNAL1)
print(crickit.seesaw.digital_read(SIGNAL2))
