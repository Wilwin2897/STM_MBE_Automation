# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 13:32:28 2022

@author: wilwin
"""

#TO CONNECT PLEASE START THE ETHERNET CONFIGURATION TOOL THEN ASSIGN A COM PORT
import pyvisa
from pyvisa import constants
rm = pyvisa.ResourceManager()
res = rm.list_resources()
inficon = rm.open_resource('ASRL8::INSTR',read_termination='',write_termination='')
rm.visalib.set_buffer(inficon.session, constants.VI_IO_IN_BUF, 32)
rm.visalib.set_buffer(inficon.session, constants.VI_IO_OUT_BUF, 32)
inficon.query("PR1\r\n")
PLL = inficon.query("\05")
print(float(PLL[3:]))
inficon.close()
