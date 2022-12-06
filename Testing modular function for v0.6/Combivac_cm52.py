# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:05:13 2022

@author: wilwin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:52:03 2022

@author: wilwin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:05:13 2022

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
        
        
E = Eurotherm3508('COM9',1)

E.serial.close()