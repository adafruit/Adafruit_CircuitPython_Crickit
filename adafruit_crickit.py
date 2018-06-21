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
`Adafruit_Crickit`
====================================================

.. todo:: Convenience library for using the Adafruit Crickit robotics boards.

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

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Crickit.git"

#pylint: disable=too-few-public-methods

class _DeviceList:
    """Common class for dynamically creating instances of device objects."""
    def __init__(self, pin_list, seesaw):
        self._list = pin_list
        self._seesaw = seesaw

    def __getitem__(self, terminal):
        if not 1 <= terminal <= len(self._list):
            raise IndexError("Terminal must be in range 1-{}".format(len(self._list) - 1))
        item = self._list[terminal]
        if isinstance(item, (int, tuple)):
            self._list[terminal] = item = self._create_device(item)
        return item

    def _create_device(self, pin_or_pins):
        raise NotImplementedError

class _ServoList(_DeviceList):
    def _create_device(self, pin_or_pins):
        # To save space, import only when needed.
        from adafruit_seesaw.pwmout import PWMOut
        from adafruit_motor.servo import Servo
        pwm = PWMOut(self._seesaw, pin_or_pins)
        pwm.frequency = 50
        return Servo(pwm)

class _DCMotorList(_DeviceList):
    def _create_device(self, pin_or_pins):
        # To save space, import only when needed.
        from adafruit_seesaw.pwmout import PWMOut
        from adafruit_motor.motor import DCMotor
        # Replace pin numbers tuple in slot with an instance of DCMotor on those pins.
        return DCMotor(*(PWMOut(self._seesaw, pin) for pin in pin_or_pins))

class _StepperMotorList(_DeviceList):
    def _create_device(self, pin_or_pins):
        # To save space, import only when needed.
        from adafruit_seesaw.pwmout import PWMOut
        from adafruit_motor.motor import StepperMotor
        # Replace pin numbers tuple in slot with an instance of StepperMotor on those pins.
        return StepperMotor(*(PWMOut(self._seesaw, pin) for pin in pin_or_pins))

class _DriveList(_DeviceList):
    def _create_device(self, pin_or_pins):
        # To save space, import only when needed.
        from adafruit_seesaw.pwmout import PWMOut
        drive = PWMOut(self._seesaw, pin_or_pins)
        drive.frequency = 1000
        return drive

class CrickitTouchIn:
    """Imitate touchio.TouchIn."""
    def __init__(self, pin, seesaw):
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

class _TouchList(_DeviceList):
    def _create_device(self, pin_or_pins):
        return CrickitTouchIn(pin_or_pins, self._seesaw)

class _SignalTerminalList:
    def __init__(self, seesaw_pins):
        self._pins = seesaw_pins

    def __getitem__(self, terminal):
        """The seesaw pin number for this Signal terminal."""
        if not 1 <= terminal <= len(self._pins):
            raise IndexError("Terminal must be in range 1-{}".format(len(self._pins) - 1))
        return self._pins[terminal]

class Crickit:
    """Represents a Crickit board."""
    def __init__(self, seesaw):
        self._seesaw = seesaw
        self._servo = _ServoList([None, 17, 16, 15, 14], self.seesaw)
        self._dc_motor = _DCMotorList([None, (22, 23), (19, 18)], self.seesaw)
        self._stepper_motor = _StepperMotorList([None, (22, 23, 19, 18)], self.seesaw)
        self._drive = _DriveList([None, 13, 12, 43, 42], self.seesaw)
        self._touch = _TouchList([None, 4, 5, 6, 7], self.seesaw)
        self._signal_pin = _SignalTerminalList((None, 2, 3, 40, 41, 11, 10, 9, 8))
        self._neopixel = None

    @property
    def seesaw(self):
        """The Seesaw object that talks to the Crickit. Use this object to manipulate signal pins.

        .. code-block:: python

        from adafruit_crickit import crickit

        crickit.seesaw.pin_mode(crickit.signal_pin[4], ss.OUTPUT)
        crickit.seesaw.digital_write(crickit.signal_pin[4], True)
"""

        return self._seesaw

    @property
    def servo(self):
        """adafruit_motor.servo.Servo objects for the Servo terminals 1 through 4.

        .. code-block:: python

        from adafruit_crickit import crickit

        # Set servos 1 and 4 to 90 degrees.
        crickit.servo[1].angle = 90
        crickit.servo[4].angle = 90
        """
        return self._servo

    @property
    def dc_motor(self):
        """adafruit_motor.motor.DCMotor objects for the Motor terminals 1 and 2

        .. code-block:: python

        from adafruit_crickit import crickit

        crickit.dc_motor[1].throttle = 0.5    # Run both motors at half-speed.
        crickit.dc_motor[2].throttle = 0.5    # Run both motors at half-speed.
        """
        return self._dc_motor

    @property
    def stepper_motor(self):
        """adafruit_motor.motor.StepperMotor object. The four Motor terminals are used
        all together to drive a single StepperMotor.

        .. code-block:: python

        from adafruit_crickit import crickit
        from adafruit_motor import stepper

        crickit.stepper_motor.onestep(direction=stepper.FORWARD)
        """
        return self._stepper_motor

    @property
    def drive(self):
        """seesaw.pwmout.PWMout objects for the four Drive terminals.
        Each PWMOut.frequency is initialized to 1000.


        .. code-block:: python

        import time
        from adafruit_crickit import crickit

        # Turn on Drive 2 for 1 second.
        crickit.drive[2].duty_cycle = 65535
        time.sleep(1)
        crickit.drive[2].duty_cycle = 0
        """
        return self._drive

    @property
    def touch(self):
        """CrickitTouchIn objects for the four Capacitive Touch terminals.

        .. code-block:: python

        from adafruit_crickit import crickit

        for i in (1, 2, 3, 4):
            if crickit.touch[i]:
                print("Pad", i, "touched")
        """
        return self._touch

    @property
    def signal_pin(self):
        """The seesaw signal pin number for the corresponding Signal terminal.
        For example, Signal terminal 3 maps to seesaw pin 40.

        from adafruit_crickit import crickit

        signal8 = crickit.signal_pin[8]
        crickit.seesaw.pin_mode(signal8, crickit.seesaw.INPUT)
        print(crickit.seesaw.analog_read(crickit.analog_read(signal8))
        """
        return self._signal_pin

    @property
    def neopixel(self):
        """A seesaw.NeoPixel object for the NeoPixel pin.
        `Crickit.init_neopixel()` must be called before this property is used.

        .. note:: On the CPX Crickit board, the NeoPixel terminal is by default
        controlled by CPX pin A1, and is not controlled by seesaw. So this property
        will not be usable. Instead, use the regular NeoPixel library
        and specify `board.A1` as the pin.

        You can change the jumper connection on the bottom of the CPX Crickit board
        to move control of the NeoPixel terminal to seesaw pin #20. In addition,
        the Crickit FeatherWing always uses seesaw pin #20. In either of those cases,
        use this property to control the NexoPixel terminal.
        """
        if not self._neopixel:
            raise ValueError("init_neopixel() has not been called")
        return self._neopixel

    def init_neopixel(self, n, *, bpp=3, brightness=1.0, auto_write=True, pixel_order=None):
        """Initialize crickit.neopixel with the given parameters."""
        if not self._neopixel:
            from adafruit_seesaw.neopixel import NeoPixel
            # Crickit Neopixel terminal is seesaw pin 20.
            self._neopixel = NeoPixel(self._seesaw, 20, n,
                                      bpp=bpp,
                                      brightness=brightness,
                                      auto_write=auto_write,
                                      pixel_order=pixel_order)


crickit = Crickit(Seesaw(busio.I2C(board.SCL, board.SDA))) # pylint: disable=invalid-name
"""A singleton instance to control a single Crickit board, controlled by the default I2C pins."""
