# Crickit library demo - Signal terminals

from adafruit_crickit.terminals import SIGNAL1, SIGNAL2
from adafruit_crickit.crickit import crickit

# Write Signal terminal 1 and read Signal terminal 2.

ss = crickit.seesaw

ss.pin_mode(SIGNAL1, ss.OUTPUT)
ss.pin_mode(SIGNAL2, ss.INPUT)

ss.digital_write(SIGNAL1, True)
print(ss.digital_read(SIGNAL2))
