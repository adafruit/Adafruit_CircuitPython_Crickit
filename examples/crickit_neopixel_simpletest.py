# Crickit library demo - NeoPixel terminal
# Note: On CPX Crickit, NeoPixel pin is normally connected to A1, not to seesaw,
# so this demo would not control the NeoPixel terminal.
# On the Crickit FeatherWing, the NeoPixel terminal is controlled by seesaw.

import time
from adafruit_crickit import crickit

# Strip or ring of 8 NeoPixels
crickit.init_neopixel(8)

while True:
    crickit.neopixel.fill(0)
    time.sleep(1)
    crickit.neopixel[0] = (100, 0, 0)
    crickit.neopixel[1] = (0, 100, 0)
    crickit.neopixel[2] = (0, 0, 100)
    time.sleep(1)
    crickit.neopixel.fill(100, 100, 100)
    time.sleep(1)
