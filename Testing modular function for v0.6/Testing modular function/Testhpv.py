# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 15:06:03 2022

@author: wilwin
"""
class HPVP(minimalmodbus.Instrument):

    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)
