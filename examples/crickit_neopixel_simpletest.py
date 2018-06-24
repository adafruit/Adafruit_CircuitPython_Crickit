# Crickit library demo - NeoPixel terminal
# Note: On CPX Crickit, NeoPixel pin is normally connected to A1, not to seesaw,
# so this demo would not control the NeoPixel terminal.
# On the Crickit FeatherWing, the NeoPixel terminal is controlled by seesaw.

import time
from adafruit_crickit.terminals import NEOPIXEL
from adafruit_crickit.crickit import crickit

# Strip or ring of 8 NeoPixels
neopixels = crickit.neopixel(NEOPIXEL, 8)

while True:
    neopixels.fill(0)
    time.sleep(1)
    neopixels[0] = (100, 0, 0)
    neopixels[1] = (0, 100, 0)
    neopixels[2] = (0, 0, 100)
    time.sleep(1)
    neopixels.fill((100, 100, 100))
    time.sleep(1)
