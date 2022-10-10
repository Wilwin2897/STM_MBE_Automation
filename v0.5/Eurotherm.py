# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:51:15 2022

@author: wilwin
"""
#!/usr/bin/env python
import minimalmodbus

class Eurotherm3508(minimalmodbus.Instrument):
    """Instrument class for Eurotherm 3500 process controller.

    Args:
        * portname (str): port name
        * slaveaddress (int): slave address in the range 1 to 247
    """
    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)

    def get_pv_loop1(self):
        """Return the process value (PV) for loop1."""
        return self.read_register(289, 1)

    def is_manual_loop1(self):
        """Return True if loop1 is in manual mode."""
        return self.read_register(273, 1) > 0

    def get_sptarget_loop1(self):
        """Return the setpoint (SP) target for loop1."""
        return self.read_register(2, 1)

    def get_sp_loop1(self):
        """Return the (working) setpoint (SP) for loop1."""
        return self.read_register(5, 1)

    def set_sp_loop1(self, value):
        """Set the SP1 for loop1.

        Note that this is not necessarily the working setpoint.

        Args:
            value (float): Setpoint (most often in degrees)
        """
        self.write_register(3, value, 1)

eurotherm3508a = Eurotherm3508('COM1', 1) # port name, slave address (in decimal)

try:
    temperature = eurotherm3508a.get_pv_loop1()
    print(temperature)
    print(eurotherm3508a.is_manual_loop1())
    print(eurotherm3508a.get_sptarget_loop1())
    print(eurotherm3508a.get_sp_loop1())
    print(eurotherm3508a.set_sp_loop1(0.0))
except IOError:
    print("Failed to read from instrument")
 # Registernumber, number of decimals
eurotherm3508a.serial.close()
