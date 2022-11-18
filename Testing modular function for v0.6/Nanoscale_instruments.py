# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:39:00 2022

@author: wilwin
"""
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

    def get_op_loop1(self):
        """Return the manual output (OP) for loop1."""
        return self.read_register(3, 1)

    def get_sp_loop1(self):
        """Return the (working) setpoint (SP) for loop1."""
        return self.read_register(5, 1)
    
    def get_sp_loop1(self):
        """Return the  setpoint (SP) for loop1."""
        return self.read_register(2, 1)
    
    def set_sp_loop1(self, value):
        """Set the SP1 for loop1.

        Note that this is not necessarily the working setpoint.

        Args:
            value (float): Setpoint (most often in degrees)
        """
        self.write_register(24, value, 1)
    
    def set_op_loop1(self, value):
        """Set the OP1 for loop1.
            value (float): Setpoint (most often in degrees)
        """
        self.write_register(3, value, 1)
        
    def set_op_rate(self, value):
        """Set the increase rate of the op"""
        self.write_register(37, value,1)
    
    def get_PID_Proportional(self):
        self.write_register(6,1)
        
    def get_PID_Integral(self):
        self.write_register(8,1)
    
    def get_PID_Derivative(self):
        self.write_register(9,1)
    def set_PID_Proportional(self, value):
        self.write_register(6, value,1)
        
    def set_PID_Integral(self, value):
        self.write_register(8, value,1)
    
    def set_PID_Derivative(self, value):
        self.write_register(9, value,1)

class HPVP(minimalmodbus.Instrument):

    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)
    