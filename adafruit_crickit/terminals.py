# The MIT License (MIT)
#
# Copyright (c) 2018 Dan Halbert for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_crickit.terminals`
============================

Mapping of terminal names on an Adafruit Crickit board to their seesaw pin numbers.

* Author(s): Dan Halbert
"""

from micropython import const

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Crickit.git"

SIGNAL1 = const(2)
"""Signal 1 terminal"""
SIGNAL2 = const(3)
"""Signal 2 terminal"""
SIGNAL3 = const(40)
"""Signal 3 terminal"""
SIGNAL4 = const(41)
"""Signal 4 terminal"""
SIGNAL5 = const(11)
"""Signal 5 terminal"""
SIGNAL6 = const(10)
"""Signal 6 terminal"""
SIGNAL7 = const(9)
"""Signal 7 terminal"""
SIGNAL8 = const(8)
"""Signal 8 terminal"""

_SIGNAL_SET = set((SIGNAL1, SIGNAL2, SIGNAL3, SIGNAL4, SIGNAL5, SIGNAL6, SIGNAL7, SIGNAL8))

SERVO1 = const(17)
"""Servo 1 terminal"""
SERVO2 = const(16)
"""Servo 2 terminal"""
SERVO3 = const(15)
"""Servo 3 terminal"""
SERVO4 = const(14)
"""Servo 4 terminal"""

_SERVO_SET = set((SERVO1, SERVO2, SERVO3, SERVO4))

MOTOR1A = const(22)
"""Motor 1 terminal A (The A and B terminals are not differentiated on the board)"""
MOTOR1B = const(23)
"""Motor 1 terminal B (The A and B terminals are not differentiated on the board)"""
MOTOR2A = const(19)
"""Motor 2 terminal A (The A and B terminals are not differentiated on the board)"""
MOTOR2B = const(18)
"""Motor 2 terminal B (The A and B terminals are not differentiated on the board)"""

_MOTOR1_SET = set((MOTOR1A, MOTOR1B))
_MOTOR2_SET = set((MOTOR2A, MOTOR2B))
_MOTOR_SET = _MOTOR1_SET | _MOTOR2_SET

#  Drive terminal numbers on the FeatherWing Crickit are the reverse of those on the CPX Crickit.

CPX_DRIVE1 = const(42)
"""Drive 1 terminal on CPX Crickit (CPX and FeatherWing are different)"""
CPX_DRIVE2 = const(43)
"""Drive 2 terminal on CPX Crickit"""
CPX_DRIVE3 = const(12)
"""Drive 3 terminal on CPX Crickit"""
CPX_DRIVE4 = const(13)
"""Drive 4 terminal on CPX Crickit"""

FEATHER_DRIVE1 = const(13)
"""Drive 1 terminal on Crickit FeatherWing (CPX and FeatherWing are different)"""
FEATHER_DRIVE2 = const(12)
"""Drive 2 terminal on Crickit FeatherWing"""
FEATHER_DRIVE3 = const(43)
"""Drive 3 terminal on Crickit FeatherWing"""
FEATHER_DRIVE4 = const(42)
"""Drive 4 terminal on Crickit FeatherWing"""

_DRIVE_SET = set((CPX_DRIVE1, CPX_DRIVE2, CPX_DRIVE3, CPX_DRIVE4))

_PWM_SET = _MOTOR_SET | _SERVO_SET | _DRIVE_SET

TOUCH1 = const(4)
"""Capacitive Touch 1 terminal"""
TOUCH2 = const(5)
"""Capacitive Touch 2 terminal"""
TOUCH3 = const(6)
"""Capacitive Touch 3 terminal"""
TOUCH4 = const(7)
"""Capacitive Touch 4 terminal"""

_TOUCH_SET = set((TOUCH1, TOUCH2, TOUCH3, TOUCH4))

NEOPIXEL = 20
"""NeoPixel terminal.
On the CPX Crickit board, the NeoPixel terminal is by default controlled by CPX pin A1,
and is not controllable by this library. (There is a jumper to override this.)
Instead, use the regular NeoPixel library and specify ``board.A1`` as the pin.
On the Crickit FeatherWing, the NeoPixel terminal is set up to be controlled by
the Crickit board.
"""
