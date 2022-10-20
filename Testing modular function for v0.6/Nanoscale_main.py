# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:31:55 2022

@author: wilwin
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Nanoscale_GUI import Ui_MainWindow
from Nanoscale_widgets import EuroGroup,HVPower_Voltage,HVPower_Current,Time_delay,Stabilization_set,Shutter_set
from Nanoscale_buttons import Today finish until here
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.setAcceptDrops(True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.module_sets()
        self.show()
        
    def module_sets(self): #Put a new module here
        self._posEuro = -20;self.ui.Euro_mod=[];self.ui.Eurocount = 0
        self._posHVPV = -20;self.ui.HVPV_mod=[];self.ui.HVPVcount = 0
        self._posHVPA = -20;self.ui.HVPA_mod=[];self.ui.HVPAcount = 0
        self._posTime = -20;self.ui.Time_mod=[];self.ui.Timecount = 0
        self._posShut = -20;self.ui.Shut_mod=[];self.ui.Shutcount = 0
        self.add_Euro()
        self.add_HPV()
        self.add_HPA()
        self.add_Time()
        self.add_Shut()
        self.ui.Stabilizationset = Stabilization_set(self.ui.tab_2)
        self.ui.Stabilizationset.move(270, 600)
        
    def dragEnterEvent(self, e):
        e.accept()
        
    def dropEvent(self, e):
        pos = e.pos()
        #How to make both buttons can move independently?
        e.source().move(pos+QtCore.QPoint(8, -40))
        print(pos)
        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
        
##################################################################
#####Put add and remove buttons function for the modules here#####
#######The module can be added in Nanoscale_widgets.py file#######
##################################################################
    def add_Euro(self):
        self._posEuro += 20
        self.ui.Euro_mod.append(EuroGroup(self.ui.tab_2))
        self.ui.Euro_mod[self.ui.Eurocount].add_button.clicked.connect(self.add_Euro)
        self.ui.Euro_mod[self.ui.Eurocount].remove_button.clicked.connect(self.remove_Euro)
        self.ui.Euro_mod[self.ui.Eurocount].move(270+self._posEuro,self._posEuro)
        self.ui.Euro_mod[self.ui.Eurocount].show()
        self.ui.Eurocount +=1
        
    def remove_Euro(self):
        self.ui.Euro_mod.pop().deleteLater()
        self.ui.Eurocount -=1
        
    def add_HPV(self):
        self._posHVPV += 20
        self.ui.HVPV_mod.append(HVPower_Voltage(self.ui.tab_2))
        self.ui.HVPV_mod[self.ui.HVPVcount].add_button.clicked.connect(self.add_HPV)
        self.ui.HVPV_mod[self.ui.HVPVcount].remove_button.clicked.connect(self.remove_HPV)
        self.ui.HVPV_mod[self.ui.HVPVcount].move(270+self._posHVPV,180+self._posHVPV)
        self.ui.HVPV_mod[self.ui.HVPVcount].show()
        self.ui.HVPVcount +=1
        
    def remove_HPV(self):
        self.ui.HVPV_mod.pop().deleteLater()
        self.ui.HVPVcount -=1
        
    def add_HPA(self):
        self._posHVPA += 20
        self.ui.HVPA_mod.append(HVPower_Current(self.ui.tab_2))
        self.ui.HVPA_mod[self.ui.HVPAcount].add_button.clicked.connect(self.add_HPA)
        self.ui.HVPA_mod[self.ui.HVPAcount].remove_button.clicked.connect(self.remove_HPA)
        self.ui.HVPA_mod[self.ui.HVPAcount].move(270+self._posHVPA,340+self._posHVPA)
        self.ui.HVPA_mod[self.ui.HVPAcount].show()
        self.ui.HVPAcount +=1
        
    def remove_HPA(self):
        self.ui.HVPA_mod.pop().deleteLater()
        self.ui.HVPAcount -=1
        
    def add_Time(self):
        self._posTime += 20
        self.ui.Time_mod.append(Time_delay(self.ui.tab_2))
        self.ui.Time_mod[self.ui.Timecount].add_button.clicked.connect(self.add_Time)
        self.ui.Time_mod[self.ui.Timecount].remove_button.clicked.connect(self.remove_Time)
        self.ui.Time_mod[self.ui.Timecount].move(270+self._posTime,500+self._posTime)
        self.ui.Time_mod[self.ui.Timecount].show()
        self.ui.Timecount +=1

    def remove_Time(self):
        self.ui.Time_mod.pop().deleteLater()
        self.ui.Timecount -=1
        
    def add_Shut(self):
        self._posShut += 20
        self.ui.Shut_mod.append(Shutter_set(self.ui.tab_2))
        self.ui.Shut_mod[self.ui.Shutcount].add_button.clicked.connect(self.add_Shut)
        self.ui.Shut_mod[self.ui.Shutcount].remove_button.clicked.connect(self.remove_Shut)
        self.ui.Shut_mod[self.ui.Shutcount].move(540+self._posShut,10+self._posShut)
        self.ui.Shut_mod[self.ui.Shutcount].show()
        self.ui.Shutcount +=1
    
    def remove_Shut(self):
        self.ui.Shut_mod.pop().deleteLater()
        self.ui.Shutcount -=1

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    