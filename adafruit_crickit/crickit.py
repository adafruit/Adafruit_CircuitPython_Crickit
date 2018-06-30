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
`adafruit_crickit.crickit`
==========================

Convenience library for using the Adafruit Crickit robotics boards.

* Author(s): Dan Halbert

Implementation Notes
--------------------

**Hardware:**

   `Adafruit Crickit for Circuit Playground Express <https://www.adafruit.com/3093>`_
   `Adafruit Crickit FeatherWing <https://www.adafruit.com/3343>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""

import sys

import board
import busio

#pylint: disable=wrong-import-position
sys.path.insert(0, ".frozen")   # Prefer frozen modules over local.

from adafruit_seesaw.seesaw import Seesaw
# This is very common so import it in advance.
# Takes less memory to import PWMOut once than have multiple import statements.
# Each import statement is about 60 bytes.
from adafruit_seesaw.pwmout import PWMOut

from adafruit_crickit.terminals import (NEOPIXEL, _SIGNAL_SET,
                                        _MOTOR1_SET, _MOTOR2_SET, _MOTOR_SET,
                                        _DRIVE_SET, _PWM_SET, _TOUCH_SET)

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Crickit.git"

# Exception strings
_TERMINALS_IN_USE = "Terminal(s) already in use"
_TERMINALS_NOT_VALID = "Terminal(s) can't be used for this kind of device"

#pylint: disable=too-few-public-methods

class CrickitTouchIn:
    """Imitate touchio.TouchIn."""
    def __init__(self, seesaw, pin):
        self._seesaw = seesaw
        self._pin = pin
        self.threshold = self.raw_value + 100

    @property
    def raw_value(self):
        """The raw touch measurement as an `int`. (read-only)"""
        return self._seesaw.touch_read(self._pin)

    @property
    def value(self):
        """Whether the touch pad is being touched or not. (read-only)"""
        return self.raw_value > self.threshold


class Crickit:
    """Represents a Crickit board."""
    def __init__(self, seesaw):
        self._seesaw = seesaw

    @property
    def seesaw(self):
        """The Seesaw object that talks to the Crickit. Use this object to manipulate the
        signal pins that correspond to Crickit terminals.

        .. code-block:: python

          from adafruit_crickit.terminals import SIGNAL4
          from adafruit_crickit.crickit import crickit

          ss = crickit.seesaw
          ss.pin_mode(SIGNAL4, ss.OUTPUT)
          ss.digital_write(SIGNAL4], True)
        """

        return self._seesaw

    def servo(self, terminal, *, actuation_range=180, min_pulse=750, max_pulse=2250):
        """Create an ``adafruit_motor.servo.Servo object``.

       :param terminal
       :param int actuation_range: The physical range of motion of the servo in degrees, \
           for the given ``min_pulse`` and ``max_pulse`` values.
       :param int min_pulse: The minimum pulse width of the servo in microseconds.
       :param int max_pulse: The maximum pulse width of the servo in microseconds.

       The specified pulse width range of a servo has historically been 1000-2000us,
       for a 90 degree range of motion. But nearly all modern servos have a 170-180
       degree range, and the pulse widths can go well out of the range to achieve this
       extended motion. The default values here of ``750`` and ``2250`` typically give
       135 degrees of motion. You can set ``actuation_range`` to correspond to the
       actual range of motion you observe with your given ``min_pulse`` and ``max_pulse``
       values.

       .. warning:: You can extend the pulse width above and below these limits to
         get a wider range of movement. But if you go too low or too high,
         the servo mechanism may hit the end stops, buzz, and draw extra current as it stalls.
         Test carefully to find the safe minimum and maximum.

        .. code-block:: python

          import time
          from adafruit_crickit.terminals import SERVO1
          from adafruit_crickit.crickit import crickit

          servo1 = crickit.servo(SERVO1)
          # Set to 90 degrees.
          servo1.angle = 90

          # Set all the way one way, then the other.
          servo1.fraction = 0.0
          time.sleep(1.0)
          servo.fraction  = 1.0
        """
        if terminal not in _PWM_SET:
            raise ValueError(_TERMINALS_NOT_VALID)

        from adafruit_motor.servo import Servo

        pwm = PWMOut(self._seesaw, terminal)
        pwm.frequency = 50
        return Servo(pwm, actuation_range=actuation_range, min_pulse=min_pulse, max_pulse=max_pulse)

    def continuous_servo(self, terminal, *, min_pulse=750, max_pulse=2250):
        """Create an ``adafruit_motor.servo.ContinuousServo`` object

        .. code-block:: python

          from adafruit_crickit.terminals import SERVO1
          from adafruit_crickit.crickit import crickit

          continuous_servo1 = crickit.continuous_servo1(SERVO1)
          # Start spinning backwards at half speed.
          servo1.throttle = -0.5
        """
        if terminal not in _PWM_SET:
            raise ValueError(_TERMINALS_NOT_VALID)

        from adafruit_motor.servo import ContinuousServo

        pwm = PWMOut(self._seesaw, terminal)
        pwm.frequency = 50
        return ContinuousServo(pwm, min_pulse=min_pulse, max_pulse=max_pulse)

    def dc_motor(self, terminal1, terminal2):
        """Create an ``adafruit_motor.motor.DCMotor`` object.

        .. code-block:: python

          from adafruit_crickit.terminals import MOTOR1A, MOTOR1B, MOTOR2A, MOTOR2B
          from adafruit_crickit.crickit import crickit

          # Create dc_motor objects.
          motor1 = crickit.dc_motor(MOTOR1A, MOTOR1B)
          motor2 = crickit.dc_motor(MOTOR2A, MOTOR2B)

          # Run both motors at half-speed.
          motor1.throttle = 0.5
          motor2.throttle = 0.5
        """

        # Make sure pins are valid and both are either MOTOR1 or MOTOR2.
        # Use set comparison to ignore order.
        if set((terminal1, terminal2)) not in (_MOTOR1_SET, _MOTOR2_SET):
            raise ValueError(_TERMINALS_NOT_VALID)

        from adafruit_motor.motor import DCMotor

        return DCMotor(PWMOut(self._seesaw, terminal1),
                       PWMOut(self._seesaw, terminal2))

    def stepper_motor(self, terminal1, terminal2, terminal3, terminal4):
        """Create an ``adafruit_motor.motor.StepperMotor`` object.
        The four Motor or four Drive terminals are used all together
        to drive a single StepperMotor.

        .. code-block:: python

          from adafruit_crickit.terminals import DRIVE1, DRIVE2, DRIVE3, DRIVE4
          from adafruit_crickit.terminals import MOTOR1A, MOTOR1B, MOTOR2A, MOTOR2B
          from adafruit_crickit.crickit import crickit

          stepper_d = crickit.stepper_motor(DRIVE1, DRIVE2, DRIVE3, DRIVE4)
          stepper_d.onestep(direction=stepper.FORWARD)
          stepper_m = crickit.stepper_motor(MOTOR1A, MOTOR1B, MOTOR2A, MOTOR2B)
          stepper_m.onestep(direction=stepper.BACKWARD)

        """
        terminals = (terminal1, terminal2, terminal3, terminal4)
        if set(terminals) not in (_DRIVE_SET, _MOTOR_SET):
            raise ValueError(_TERMINALS_NOT_VALID)

        from adafruit_motor.stepper import StepperMotor
        return StepperMotor(*(PWMOut(self._seesaw, terminal) for terminal in terminals))

    def pwm_out(self, terminal, duty_cycle=0, frequency=1000):
        """Create an ``adafruit_seesaw.pwmout.PWMOut`` object.

        Note that the default ``frequency`` is 1000, not 500, which is the default
        for `pulseio.PWMOut`. 1000 is a better default for the Drive terminals.

        .. code-block:: python

          from adafruit_crickit.terminals import CPX_DRIVE2
          from adafruit_crickit.crickit import crickit

          # Create general PWM on CPX_DRIVE2 terminal.
          drive2 = crickit.pwm_out(CPX_DRIVE2)

          # Turn on 50% duty cycle for CPX_DRIVE2
          drive2.fraction = 0.5
        """
        if terminal not in _PWM_SET:
            raise ValueError(_TERMINALS_NOT_VALID)

        pwm = PWMOut(self._seesaw, terminal)
        pwm.duty_cycle = duty_cycle
        pwm.frequency = frequency
        return pwm

    def touch(self, terminal):
        """Create a `CrickitTouchIn` object. Used for the four Capacitive Touch terminals
        and also for Signal terminals that have touch capability (`SIGNAL1` through `SIGNAL4`).

        .. code-block:: python

          from adafruit_crickit.terminals import TOUCH1
          from adafruit_crickit.crickit import crickit

          touch1 = crickit.touch(TOUCH1)
          if touch1.value:
              print("Touch 1 touched")
        """
        if terminal not in _TOUCH_SET:
            raise ValueError(_TERMINALS_NOT_VALID)
        return CrickitTouchIn(self._seesaw, terminal)

    def neopixel(self, terminal, n, *, bpp=3, brightness=1.0, auto_write=True, pixel_order=None):
        """Create a seesaw.NeoPixel object for the given terminal.

        .. note:: On the CPX Crickit board, the NeoPixel terminal is by default
          controlled by CPX pin A1, and is not controlled by seesaw. So this object
          will not be usable. Instead, use the regular NeoPixel library
          and specify ``board.A1`` as the pin.

        You can change the jumper connection on the bottom of the CPX Crickit board
        to move control of the NeoPixel terminal to seesaw pin #20 (terminal.NEOPIXEL).
        In addition, the Crickit FeatherWing always uses seesaw pin #20.
        In either of those cases, this object will work.

        .. code-block:: python

          from adafruit_crickit.terminals import NEOPIXEL
          from adafruit_crickit.crickit import crickit

          neopixels = crickit.neopixel(NEOPIXEL, 24)

          neopixels.fill((100, 0, 0))
        """
        from adafruit_seesaw.neopixel import NeoPixel

        if terminal not in _SIGNAL_SET and terminal != NEOPIXEL:
            raise ValueError(_TERMINALS_NOT_VALID)
        return NeoPixel(self._seesaw, terminal, n, bpp=bpp,
                        brightness=brightness, auto_write=auto_write,
                        pixel_order=pixel_order)

    def reset(self):
        """Reset the whole Crickit board."""
        self._seesaw.sw_reset()

crickit = None # pylint: disable=invalid-name
"""A singleton instance to control a single Crickit board, controlled by the default I2C pins."""

# Sphinx's board is missing real pins so skip the constructor in that case.
if "SCL" in dir(board):
    crickit = Crickit(Seesaw(busio.I2C(board.SCL, board.SDA))) # pylint: disable=invalid-name
