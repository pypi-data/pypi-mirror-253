============
SxIP drivers
============

Overview
========

This module is a Python driver for PHOXENE's SxIP flash devices

It is intended to be use by software developpers in order to speed-up the integration
of PHOXENE's flash devices by our customers.

It is realeased under a free software licence,
see the LICENSE file for more details

MIT License Copyright (c) 2024 PHOXENE


Features
========
* Allow to instanciate a SxIP communication objects
* Implements general functions
    * Read multiple registers
    * Write a single register
    * Write multiple registers
    * Write a single coil
* Implements SxIP dedicated functions
* The files in this package are 100% pure Python.

Requirements
============
* Pyhton 3.7 or newer
* Windows 7 or newer
* Debian 10 or newer

Installation
============
sxip-drivers can be installed from PyPI:

.. code-block:: console

    pip install sxip-drivers

Developers also may be interested to get the source archive, because it contains examples, tests and this documentation.
