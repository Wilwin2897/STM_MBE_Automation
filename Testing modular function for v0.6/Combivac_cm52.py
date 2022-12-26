# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:05:13 2022

@author: wilwin
"""

import pyvisa
from pyvisa import constants
rm = pyvisa.ResourceManager()
res = rm.list_resources()
print(res)
combivac = rm.open_resource('ASRL4::INSTR',baud_rate = 19200,read_termination='\r',write_termination='\r')
rm.visalib.set_buffer(combivac.session, constants.VI_IO_IN_BUF, 50)
rm.visalib.set_buffer(combivac.session, constants.VI_IO_OUT_BUF, 50)
P1 = combivac.query("RPV2")
print(P1)
P2 = combivac.query("RPV3")
print(P2)
combivac.close()