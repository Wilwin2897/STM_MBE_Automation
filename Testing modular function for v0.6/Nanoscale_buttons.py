# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:15:44 2022

@author: wilwin
"""

class buttons_set(QtWidgets.QWidget):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Change self.tab to self
        self.groupBox = QtWidgets.QGroupBox(self)