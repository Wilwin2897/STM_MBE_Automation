# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:15:44 2022

@author: wilwin
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from Nanoscale_widgets import EuroGroup,HVPower_Voltage,HVPower_Current,Time_delay,Stabilization_set,Shutter_set

class buttons_set(QtWidgets.QWidget):
    def setupUi(self):
        #Change self.tab to self
        
        self._posEuro = -20;self.Euro_mod=[];self.Eurocount = 0
        self._posHVPV = -20;self.HVPV_mod=[];self.HVPVcount = 0
        self._posHVPA = -20;self.HVPA_mod=[];self.HVPAcount = 0
        self._posTime = -20;self.Time_mod=[];self.Timecount = 0
        self._posShut = -20;self.Shut_mod=[];self.Shutcount = 0
##################################################################
#####Put add and remove buttons function for the modules here#####
#######The module can be added in Nanoscale_widgets.py file#######
##################################################################
    def add_Euro(self):
        self._posEuro += 20
        self.Euro_mod.append(EuroGroup(self))
        self.Euro_mod[self.Eurocount].add_button.clicked.connect(self.add_Euro)
        self.Euro_mod[self.Eurocount].remove_button.clicked.connect(self.remove_Euro)
        self.Euro_mod[self.Eurocount].move(270+self._posEuro,self._posEuro)
        self.Euro_mod[self.Eurocount].show()
        self.Eurocount +=1
        
    def remove_Euro(self):
        self.Euro_mod.pop().deleteLater()
        self.Eurocount -=1
        
    def add_HPV(self):
        self._posHVPV += 20
        self.HVPV_mod.append(HVPower_Voltage(self))
        self.HVPV_mod[self.HVPVcount].add_button.clicked.connect(self.add_HPV)
        self.HVPV_mod[self.HVPVcount].remove_button.clicked.connect(self.remove_HPV)
        self.HVPV_mod[self.HVPVcount].move(270+self._posHVPV,180+self._posHVPV)
        self.HVPV_mod[self.HVPVcount].show()
        self.HVPVcount +=1
        
    def remove_HPV(self):
        self.HVPV_mod.pop().deleteLater()
        self.HVPVcount -=1
        
    def add_HPA(self):
        self._posHVPA += 20
        self.HVPA_mod.append(HVPower_Current(self))
        self.HVPA_mod[self.HVPAcount].add_button.clicked.connect(self.add_HPA)
        self.HVPA_mod[self.HVPAcount].remove_button.clicked.connect(self.remove_HPA)
        self.HVPA_mod[self.HVPAcount].move(270+self._posHVPA,340+self._posHVPA)
        self.HVPA_mod[self.HVPAcount].show()
        self.HVPAcount +=1
        
    def remove_HPA(self):
        self.HVPA_mod.pop().deleteLater()
        self.HVPAcount -=1
        
    def add_Time(self):
        self._posTime += 20
        self.Time_mod.append(Time_delay(self))
        self.Time_mod[self.Timecount].add_button.clicked.connect(self.add_Time)
        self.Time_mod[self.Timecount].remove_button.clicked.connect(self.remove_Time)
        self.Time_mod[self.Timecount].move(270+self._posTime,500+self._posTime)
        self.Time_mod[self.Timecount].show()
        self.Timecount +=1

    def remove_Time(self):
        self.Time_mod.pop().deleteLater()
        self.Timecount -=1
        
    def add_Shut(self):
        self._posShut += 20
        self.Shut_mod.append(Shutter_set(self))
        self.Shut_mod[self.Shutcount].add_button.clicked.connect(self.add_Shut)
        self.Shut_mod[self.Shutcount].remove_button.clicked.connect(self.remove_Shut)
        self.Shut_mod[self.Shutcount].move(540+self._posShut,10+self._posShut)
        self.Shut_mod[self.Shutcount].show()
        self.Shutcount +=1
    
    def remove_Shut(self):
        self.Shut_mod.pop().deleteLater()
        self.Shutcount -=1