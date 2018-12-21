Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-crickit/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/crickit/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_Crickit.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_Crickit
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

  from adafruit_crickit import crickit

  # Add this import if using stepper motors.
  # It will expose constants saying how to step: stepper.FORWARD, stepper.BACKWARD, etc.
  from adafruit_motor import stepper

  # Set servo 1 to 90 degrees
  crickit.servo_1.angle = 90

  # Change servo settings.
  crickit.servo_1.actuation_range = 135
  crickit.servo_1.set_pulse_width_range(min_pulse=850, max_pulse=2100)

  # You can assign a device to a variable to get a shorter name.
  servo_2 = crickit.servo_2
  servo_2.throttle = 0

  # Run a continous servo on Servo 2 backwards at half speed.
  crickit.continuous_servo_2.throttle = -0.5

  # Run the motor on Motor 1 terminals at half speed.
  crickit.dc_motor_1.throttle = 0.5

  # Set Drive 1 terminal to 3/4 strength.
  crickit.drive_1.fraction = 0.75

  if crickit.touch_1.value:
      print("Touched terminal Touch 1")

  # A single stepper motor uses up all the motor terminals.
  crickit.stepper_motor.onestep(direction=stepper.FORWARD)

  # You can also use the Drive terminals for a stepper motor
  crickit.drive_stepper_motor.onestep(direction=stepper.BACKWARD)

  # Note: On CPX Crickit, NeoPixel pin is normally connected to A1, not to seesaw,
  # so this part of the demo cannot control the NeoPixel terminal.
  # Strip or ring of 8 NeoPixels
  crickit.init_neopixel(8)
  crickit.neopixel.fill((100, 100, 100))


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
