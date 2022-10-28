# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 23:40:46 2022

@author: wilwin
"""

class default_parameters():
    def default(self):
        self.heating_rate = [12, 8, 6, 4, 3, 2]
        self.cooling_rate = [12, 8, 6, 4, 3, 2]
        self.substrate_rate = [100, 0.2]
        self.substrate_set = [1004.2, 3.80]
        self.standby_temp = [800, 800, 1100, 1100]
        self.opening_temp = [1060.2, 1050, 1430, 1430]
        self.opening_time = [30, 15, 30, 30]
        self.delay_time = [0, 90, 0, 0]
        self.anneal_para = [1004.2, 3.80, 720]
        self.T_fixed_points = [200, 300, 250, 250, 250, 250]
        self.pres_thres = 2.e-9
        
        
