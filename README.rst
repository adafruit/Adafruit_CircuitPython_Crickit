Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-crickit/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/crickit/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_Crickit/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_Crickit/actions/
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

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-crickit/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-crickit

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-crickit

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-crickit

Usage Example
=============

This examples shows how to control all the devices supported by the library.
In most cases you just need a couple of imports.

.. code-block:: python

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

  # Set the Crickit's on-board NeoPixel to a dim purple.
  crickit.onboard_pixel.brightness = 0.01
  crickit.onboard_pixel[0] = (255, 24, 255)
  # or
  crickit.onboard_pixel.fill((255, 24, 255))

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/crickit/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_Crickit/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
