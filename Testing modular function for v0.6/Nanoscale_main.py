# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:31:55 2022

@author: wilwin
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Nanoscale_GUI import Ui_MainWindow
from Nanoscale_widgets import EuroGroup,HVPower_Voltage,HVPower_Current,Time_delay,Stabilization_set,Shutter_set

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.setAcceptDrops(True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.module_sets()
        self.show()
        
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
#####Get the Widgets for modular function#####
##################################################################
    def module_sets(self): #Put a new module here
        self._posEuro = -20;self.ui.Euro_mod=[];self.ui.Eurocount = 0
        self._posHVPV = -20;self.ui.HVPV_mod=[];self.ui.HVPVcount = 0
        self._posHVPA = -20;self.ui.HVPA_mod=[];self.ui.HVPAcount = 0
        self._posTime = -20;self.ui.Time_mod=[];self.ui.Timecount = 0
        self._posShut = -20;self.ui.Shut_mod=[];self.ui.Shutcount = 0
        
        self.ui.mbe_savegrowthtimeline_2.clicked.connect(self.add_module)
        self.ui.mbe_savegrowthtimeline_15.clicked.connect(self.remove_module)
        self.ui.mbe_savegrowthtimeline_16.clicked.connect(self.save_module)
        self.ui.mbe_savegrowthtimeline_17.clicked.connect(self.load_module)

        #self.add_Euro()
        #self.add_HPV()
        #self.add_HPA()
        #self.add_Time()
        #self.add_Shut()
        self.ui.Stabilizationset = Stabilization_set(self.ui.tab_2)
        self.ui.Stabilizationset.move(270, 600)

    def add_module(self):
        module_dict = {'Eurotherm controller': self.add_Euro, 'HV Power Supply (Voltage)': self.add_HVPV,\
                       'HV Power Supply (Current)':self.add_HVPA, 'Shutter module':self.add_Shut,\
                       'Time Delay controller':self.add_Time}
        s=[]
        s+=[self.ui.comboBox_2.currentText(),self.ui.comboBox_5.currentText(),self.ui.comboBox_17.currentText(),\
            self.ui.comboBox_16.currentText(),self.ui.comboBox_18.currentText()]
        for box in s:
            if box!= 'None selected': 
                f = module_dict[box] ; f()
        
    def remove_module(self):
        module_dict = {'Eurotherm controller': self.remove_Euro, 'HV Power Supply (Voltage)':self.remove_HVPV,\
                       'HV Power Supply (Current)':self.remove_HVPA, 'Shutter module':self.remove_Shut,\
                       'Time Delay controller':self.remove_Time}
        s=[]
        s+=[self.ui.comboBox_2.currentText(),self.ui.comboBox_5.currentText(),self.ui.comboBox_17.currentText(),\
            self.ui.comboBox_16.currentText(),self.ui.comboBox_18.currentText()]
        for box in s:
            if box!= 'None selected': 
                f = module_dict[box] ; f()
              
######################################################################
#####Saving and loading widgets and position for modular function#####
######################################################################
    def save_module(self):
        text = self.ui.comboBox_2.currentText()
        self.settings = QtCore.QSettings( 'User', text )
        self.settings.setValue( "Eurocount", self.ui.Eurocount)
        self.settings.setValue( "HVPVcount", self.ui.HVPVcount)
        self.settings.setValue( "HVPAcount", self.ui.HVPAcount)
        self.settings.setValue( "Timecount", self.ui.Timecount)
        self.settings.setValue( "Shutcount", self.ui.Shutcount)
        for i in range(self.ui.Eurocount):
            self.settings.setValue( "Euro_pos"+str(i), self.ui.Euro_mod[i].pos())
        for i in range(self.ui.HVPVcount):
            self.settings.setValue( "HVPV_pos"+str(i), self.ui.HVPV_mod[i].pos())
        for i in range(self.ui.HVPAcount):
            self.settings.setValue( "HVPA_pos"+str(i), self.ui.HVPA_mod[i].pos())
        for i in range(self.ui.Timecount):
            self.settings.setValue( "Time_pos"+str(i), self.ui.Time_mod[i].pos())
        for i in range(self.ui.Shutcount):
            self.settings.setValue( "Shut_pos"+str(i), self.ui.Shut_mod[i].pos())
            
    def load_module(self):
        text = self.ui.comboBox_2.currentText()
        self.settings = QtCore.QSettings( 'User', text )
        for i in range(self.settings.value("Eurocount")):
            self.add_Euro()
            self.ui.Euro_mod[i].move(self.settings.value("Euro_pos"+str(i)))
        for i in range(self.settings.value("HVPVcount")):
            self.add_HVPV()
            self.ui.HVPV_mod[i].move(self.settings.value("HVPV_pos"+str(i)))
        for i in range(self.settings.value("HVPAcount")):
            self.add_HVPA()
            self.ui.HVPA_mod[i].move(self.settings.value("HVPA_pos"+str(i)))
        for i in range(self.settings.value("Timecount")):
            self.add_Time()
            self.ui.Time_mod[i].move(self.settings.value("Time_pos"+str(i)))
        for i in range(self.settings.value("Shutcount")):
            self.add_Shut()
            self.ui.Shut_mod[i].move(self.settings.value("Shut_pos"+str(i)))
        
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
        self.ui.Euro_mod[self.ui.Eurocount].spinBox.setValue(self.ui.Eurocount)
        self.ui.Euro_mod[self.ui.Eurocount].show()
        self.ui.Eurocount +=1
        
    def remove_Euro(self):
        self.ui.Euro_mod.pop().deleteLater()
        self.ui.Eurocount -=1
        
    def add_HVPV(self):
        self._posHVPV += 20
        self.ui.HVPV_mod.append(HVPower_Voltage(self.ui.tab_2))
        self.ui.HVPV_mod[self.ui.HVPVcount].add_button.clicked.connect(self.add_HVPV)
        self.ui.HVPV_mod[self.ui.HVPVcount].remove_button.clicked.connect(self.remove_HVPV)
        self.ui.HVPV_mod[self.ui.HVPVcount].move(270+self._posHVPV,180+self._posHVPV)
        self.ui.HVPV_mod[self.ui.HVPVcount].spinBox_2.setValue(self.ui.HVPVcount)
        self.ui.HVPV_mod[self.ui.HVPVcount].show()
        self.ui.HVPVcount +=1
        
    def remove_HVPV(self):
        self.ui.HVPV_mod.pop().deleteLater()
        self.ui.HVPVcount -=1
        
    def add_HVPA(self):
        self._posHVPA += 20
        self.ui.HVPA_mod.append(HVPower_Current(self.ui.tab_2))
        self.ui.HVPA_mod[self.ui.HVPAcount].add_button.clicked.connect(self.add_HVPA)
        self.ui.HVPA_mod[self.ui.HVPAcount].remove_button.clicked.connect(self.remove_HVPA)
        self.ui.HVPA_mod[self.ui.HVPAcount].move(270+self._posHVPA,340+self._posHVPA)
        self.ui.HVPA_mod[self.ui.HVPAcount].spinBox_3.setValue(self.ui.HVPAcount)
        self.ui.HVPA_mod[self.ui.HVPAcount].show()
        self.ui.HVPAcount +=1
        
    def remove_HVPA(self):
        self.ui.HVPA_mod.pop().deleteLater()
        self.ui.HVPAcount -=1
        
    def add_Time(self):
        self._posTime += 20
        self.ui.Time_mod.append(Time_delay(self.ui.tab_2))
        self.ui.Time_mod[self.ui.Timecount].add_button.clicked.connect(self.add_Time)
        self.ui.Time_mod[self.ui.Timecount].remove_button.clicked.connect(self.remove_Time)
        self.ui.Time_mod[self.ui.Timecount].move(270+self._posTime,500+self._posTime)
        self.ui.Time_mod[self.ui.Timecount].spinBox_2.setValue(self.ui.Timecount)
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
        self.ui.Shut_mod[self.ui.Shutcount].spinBox.setValue(self.ui.Shutcount)
        self.ui.Shut_mod[self.ui.Shutcount].show()
        self.ui.Shutcount +=1
    
    def remove_Shut(self):
        self.ui.Shut_mod.pop().deleteLater()
        self.ui.Shutcount -=1


        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    