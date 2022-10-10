# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:19:27 2022

@author: wilwin
pip install lakeshore
Connect to the first available Model 336 temperature controller over Ethernet
with static IP address 169.254.125.29 port 23
"""
import pyvisa as visa

rm = visa.ResourceManager()
print(rm.list_resources())
my_instrument = rm.open_resource('ASRL1::INSTR')
print(my_instrument.query('*IDN?'))