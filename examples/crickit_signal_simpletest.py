# Crickit library demo - Signal terminals

import time
from adafruit_crickit import crickit

# Write pin 1 and read pin 2.

signal1 = crickit.signal_pin[1]
signal2 = crickit.signal_pin[2]

crickit.seesaw.pin_mode(signal1, crickit.seesaw.OUTPUT)
crickit.seesaw.pin_mode(signal2, crickit.seesaw.INPUT)

crickit.seesaw.digital_write(signal1)
print(crickit.seesaw.digital_read(signal2)
