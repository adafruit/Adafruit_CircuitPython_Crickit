# Crickit library demo - Continuous servo

from adafruit_crickit.terminals import SERVO1
from adafruit_crickit.crickit import crickit

cservo1 = crickit.continuous_servo(SERVO1)

# Start spinning backwards at half speed.
cservo1.throttle = -0.5
