# -*- coding: utf-8 -*-
# Copyright (c) 2023 PHOXENE
# MIT License: 
# https://opensource.org/license/mit/
#
""" Test for sxip_driver module

"""
__authors__ = ("Aurélien PLANTIN")
__contact__ = ("a.plantin@phoxene.com")
__copyright__ = "MIT"
__date__ = "2023-10-10"

import unittest                   # The test framework
import sxip                       # The module to be tested
import modbus
from modbus import ModbusError
from serial import PortNotOpenError

def terminal_output(**kwargs):
    '''This function output everything passed as
        key arguments to the terminal.
    '''
    for k, v in kwargs.items():
        print(f"{k}: {v}")



    #flash_device.modbus_addr = 1
    '''
    try: 
        print(flash_device.read_registers(reg_addr = 1))
        print(f'Serial: {flash_device.get_serial()}')
        year, week = flash_device.get_date()
    '''

#class Test_crc(unittest.TestCase):
#    def test_crc(self) -> None:
#        # Simple crc computation result test
#        self.assertEqual(modbus._crc16([1, 6, 0, 49, 0, 2]), 50265)

class Test_with_port_not_open(unittest.TestCase):
    def setUp(self):
        modbus_link = modbus.Modbus()
        self.device = sxip.Sxip(modbus_link, modbus_addr = 1)

    def test_port_not_open_error(self) -> None:
        with self.assertRaises(PortNotOpenError):
            self.device.get_serial()

class Test_with_port_open(unittest.TestCase):
    def setUp(self):
        self.modbus_link = modbus.Modbus(port = "COM3")
        self.device = sxip.Sxip(self.modbus_link, modbus_addr = 1)

    def tearDown(self):
        self.device.modbus_addr = 1
        self.modbus_link.close()

    def test_modbus_addr_param(self) -> None:
        self.device.modbus_addr = 2
        self.assertEqual(self.device.modbus_addr, 2)
        self.device.modbus_addr = 1
    '''
    def test_set_get_functions(self) -> None:
        # Write sync shift register
        self.device.set_sync_shift(140)
        # Read sync shift register
        self.assertEqual(self.device.get_sync_shift, 140)
    '''

    def test_not_allowed_broadcast(self) -> None:
        self.device.modbus_addr = 0
        with self.assertRaises(ValueError): #Ajouter la vérification du text
            self.device.get_serial()
        self.device.modbus_addr = 1

class Test_fast_mode(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()