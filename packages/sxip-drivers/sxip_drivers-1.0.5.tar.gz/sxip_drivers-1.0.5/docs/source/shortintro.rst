==================
Short introduction
==================

preliminaries
=============
.. code-block:: python

    import sxip
    import modbus
    from modbus import ModbusError

SxIP device instantiation
=========================
Modbus_link instantiation.

Refers to phox-modbus documentation:
https://phox-modbus.readthedocs.io/en/main/

.. code-block:: python
    
    modbus_link = modbus.Modbus(port = "COM3")

SxIP flash device instantiation:

Device is affected to the modbus_link with modbus slave address 1

.. code-block:: python
    
    device = sxip.Sxip(modbus_link = modbus_link, modbus_addr = 1)

Associating with a Modbus link later
====================================
Device is instantiated with default parameters (No modbus_link and slave address = 1).

.. code-block:: python
    
    device = sxip.Sxip()

Associating a modbus link

.. code-block:: python
    
    modbus_link = modbus.Modbus(port = "COM3")
    device.modbus_link = modbus_link


Changing the device slave address

.. code-block:: python
    
    device.modbus_address = 2

Using dedicated functions
=========================
Functions that involve Modbus communication should be executed in try loops
to catch ModbusError exceptions

Get serial number function example
----------------------------------
.. code-block:: python
    
    try: 
        print(f'Serial: {device.get_serial()}')
    except ModbusError as exc:
        print(f'Modbus error: {exc}')

Set energy levels example
-------------------------
.. code-block:: python
    
    try: 
        device.set_energy_levels(prim_energy_level = 9, alt_energy_level = 8)
    except ModbusError as exc:
        print(f'Modbus error: {exc}')

Save settings example
---------------------
.. code-block:: python
    
    try: 
        device.save_settings()
    except ModbusError as exc:
        print(f'Modbus error: {exc}')