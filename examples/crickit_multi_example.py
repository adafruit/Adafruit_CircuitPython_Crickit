# This is a mock example showing typical usage of the library for each kind of device.

# crickit is a singleton object
from adafruit_crickit.crickit import crickit

# Terminals have simple names like SIGNAL1, SERVO2, TOUCH3, MOTOR1A, NEOPIXEL,
# CPX_DRIVE1, and FEATHER_DRIVE2.
# Because the Drive terminals are numbered in reverse on the CPX Crickit vs the FeatherWing Crickit,
# there are separate DRIVE names for CPX and FeatherWing Drive terminals.
from adafruit_crickit.terminals import (SERVO1,
                                        MOTOR1A, MOTOR1B, MOTOR2A, MOTOR2B,
                                        CPX_DRIVE1, NEOPIXEL, SIGNAL1, SIGNAL2, TOUCH1)

# Add this import if using stepper motors.
# It will expose constants saying how to step: stepper.FORWARD, stepper.BACKWARD, etc.
from adafruit_motor import stepper

servo1 = crickit.servo(SERVO1)
servo1.angle = 90

cservo1 = crickit.continuous_servo(SERVO1)
cservo1.throttle = -0.5

motor = crickit.dc_motor(MOTOR1A, MOTOR1B)
motor.throttle = 0.5

drive1 = crickit.pwm_out(CPX_DRIVE1)
drive1.fraction = 1.0

# Note: On CPX Crickit, NeoPixel pin is normally connected to A1, not to seesaw,
# so this demo would not control the NeoPixel terminal.

# Strip or ring of 8 NeoPixels
neopixels = crickit.neopixel(NEOPIXEL, 8)
neopixels.fill((100, 100, 100))

# Write Signal terminal 1 and read Signal terminal 2.
ss = crickit.seesaw
ss.pin_mode(SIGNAL1, ss.OUTPUT)
ss.pin_mode(SIGNAL2, ss.INPUT)
ss.digital_write(SIGNAL1, True)
print(ss.digital_read(SIGNAL2))

# A single stepper motor uses up all the motor terminals.
stepper_motor = crickit.stepper_motor(MOTOR1A, MOTOR1B, MOTOR2A, MOTOR2B)
stepper_motor.onestep(direction=stepper.FORWARD)

touch1 = crickit.touch(TOUCH1)
if touch1.value:
    print("Touched terminal Touch 1")
