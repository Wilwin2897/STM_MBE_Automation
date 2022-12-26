# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:48:39 2022

@author: wilwin
"""
from scipy.interpolate import interp1d
import numpy as np

class Calibration_OP_PV():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Please put the value for Temp and OP for the Eurotherm controller
        UPDATE accordingly, this will be taken as references so the temperature gap before
        stabillization process is lower
        [[OP0 (%), Temp0 (Degree Celcius)],[OP1,Temp1],....]
        """
        self.Te = [[0.0,10],
                   [5.7,100],
                   [50.0, 1000],
                   [80,1500]]
        self.Fe = [[0.0,10], 
                   [10.1,250],
                   [14.5, 388],
                   [59.1,1241],
                   [80,1500]]
        self.Co = [[0.0,10], 
                   [5.0,50],
                   [50.0, 1000],
                   [80,1500]]
        self.BaF2 = [[0.0,10],
                     [5,50],
                   [50.0, 1000],
                   [80,1500]]
        self.Sn = [[0.0,10], 
                   [3.4,73],
                   [5.7,100],
                   [12.8, 320.5],
                   [50.2,955],
                   [80,1500]]
        self.Dy = [[0.0,10], 
                   [5,50],
                   [50.0, 1000],
                   [80,1500]]
        
    def interpolation(self,value,SP):
        calibration = {'Te': self.Te, 'Fe' : self.Fe, 'Co' : self.Co, 'BaF2' : self.BaF2, 'Sn' : self.Sn, 'Dy' : self.Dy}
        a = calibration[value]
        a = np.array(a)
        f = interp1d(a[:,1], a[:,0])
        OP = float(f(SP))
        return round(OP, 1)

    def time_rate(self,value,Temp,SP,rate):
        total_time = abs(SP-Temp)/rate*60 #time in seconds
        OP_final = self.interpolation(value,SP)
        OP_now = self.interpolation(value,Temp)
        numstep = abs((OP_final-OP_now)*10)
        step_time = total_time/numstep
        return round(step_time, 2), int(numstep) #in seconds
        
        


        
    