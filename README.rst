Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-crickit/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/crickit/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.org/adafruit/Adafruit_CircuitPython_Crickit.svg?branch=master
    :target: https://travis-ci.org/adafruit/Adafruit_CircuitPython_Crickit
    :alt: Build Status

This convenience library makes coding for the Crickit robotics boards simpler and shorter.

Dependencies
=============
This driver depends on:

* `Adafruit seesaw library <https://github.com/adafruit/Adafruit_Circuitpython_seesaw>`_
* `Adafruit Motor library <https://github.com/adafruit/Adafruit_Circuitpython_Motor>`_


Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

This examples shows how to control all the devices supported by the library.
In most cases you just need a couple of imports.

.. code-block :: python

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


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_Crickit/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-crickit --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
