# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:31:55 2022

@author: wilwin
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Nanoscale_GUI import Ui_MainWindow
from Nanoscale_widgets import Functions,EuroGroup,HVPower_Voltage,HVPower_Current,Time_delay,Stabilization_set,Shutter_set
from Nanoscale_default import default_parameters
from Nanoscale_instruments import Eurotherm3508
import datetime
import time

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.setAcceptDrops(True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.module_sets()
        self.ui.mbe_savegrowthtimeline_13.clicked.connect(self.run_processes)
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
        
    def closeEvent(self, event):
        print("Stopping all timer, return to manual control")
##################################################################
########################Process Control###########################
##################################################################  
    def run_processes(self):    
        #Run every process with the same IDs with some specified delay
        #Will detect active modules and assign a process by each active module
        self.process_Euro3508()
        
    def process_Euro3508(self):
        self.Euro3508_init()
        self.Euro3508_check()
        if self.ui.Euro_mod !=[]:
            for i in range(len(self.ui.Euro_mod)):
                if self.ui.Euro_mod[i].mv_checkBox.checkState() == QtCore.Qt.Checked:
                    print('PID control activated, using PID instead of fitted temperature data')
                    P_value = self.ui.Euro_mod[i].doubleP.value()
                    I_value = self.ui.Euro_mod[i].doubleI.value()
                    D_value = self.ui.Euro_mod[i].doubleD.value()
                    SP_value = self.ui.Euro_mod[i].doubleSpinBox .value()
                    print('P = %.2f, I = %.2f, D = %.2f, SP = %.2f C' %(P_value,I_value,D_value,SP_value))
                    self.Euro3508_send_PID(P_value,I_value,D_value,SP_value)
                    self.timer1 = QtCore.QTimer()
                    self.timer1.timeout.connect(self.Euro3508_check)
                    self.timer1.start(5000)
                    self.Treach_count = 0
                    if abs(self._eurotemp_0-SP_value) < self.ui.Stabilizationset.doubleSpinBox_1.value():
                        self.timer2 = QtCore.QTimer()
                        self.timer2.timeout.connect(self.stabilization_T(SP_value))
                        self.timer2.start(20000)
                        
                else:
                    print('Using fitted temperature and output power data')
                self.timer2.stop()
        else:
            print("No Eurotherm module detected, please add the widget before continuing")
            
    def stabilization_T(self,SP_value):
        if abs(self._eurotemp_0-SP_value) < self.ui.Stabilizationset.doubleSpinBox_1.value():
            self.Treach_count += 1
            if self.Treach_count >= 6:
                print("Temperature is stable at the Set Point ", SP_value)
                self.timer2.stop()
                self.timer1.stop()
            else:
                print("Temperature is not stable, please adjust the stabillization set or tune manually\n")
        
        

            
                
        #self.Euro3508_send('Increase(%)')
##################################################################
#####Communication with the instruments modular function#####
##################################################################    
    def Euro3508_init(self):
        port_dict = {'Te': 'COM1', 'Sn': 'COM2',\
                     'BaF2': 'COM3', 'Co': 'COM4',\
                     'Fe': 'COM5', 'Dy': 'COM6'}
        try:
            self.eurotherm3508_0 = Eurotherm3508('COM1', 1) # port name, slave address (in decimal)
            self._eurocount_0 = self.eurotherm3508_0.get_op_loop1()
            self._eurotemp_0 = self.eurotherm3508_0.get_pv_loop1()
            print("Connected to Eurotherm with OP counter = ", self._eurocount_0," %")
            print("Connected to Eurotherm with Temperature = ", self._eurotemp_0," C")
        except IOError:
            print("Initialization failed to read from instrument, please check the Port, slave, and connection")
        except self.eurotherm3508_0.serial.SerialException:
            print("Serial Exception: Please check the Port, slave, and connection")
        finally:
            try:
                self.eurotherm3508_0.serial.close()
            except:
                pass
            
    def Euro3508_send_man(self,mode):
        upperlim = 80
        if mode == 'Increase(%)':
            self._eurocount_0 += 0.1 # Percentage of Eurotherm
            if self._eurocount_0 > upperlim:
                self._eurocount_0 = upperlim
        if mode == 'Decrease(%)':
            self._eurocount_0 -= 0.1 # Percentage of Eurotherm
            if self._eurocount_0 < 0:
                self._eurocount_0 = 0             
        try:
            self.eurotherm3508_0 = Eurotherm3508('COM1', 1)
            self.eurotherm3508_0.set_op_loop1(self._eurocount_0)
        except IOError:
            print("Sending failed to read from instrument, please check the Port, slave, and connection")
            pass
        except self.eurotherm3508_0.serial.SerialException:
            print("Serial Exception: Please check the Port, slave, and connection")
            pass
        finally:
            try:
                self.eurotherm3508_0.serial.close()
            except:
                pass
            
    def Euro3508_send_PID(self,P,I,D,SP):
        try:
            self.eurotherm3508_0 = Eurotherm3508('COM1', 1)
            self.eurotherm3508_0.set_PID_Proportional(P)
            self.eurotherm3508_0.set_PID_Integral(I)
            self.eurotherm3508_0.set_PID_Derivative(D)
            self.eurotherm3508_0.set_sp_loop1(SP)
        except IOError:
            print("Sending failed to read from instrument, please check the Port, slave, and connection")
            pass
        except self.eurotherm3508_0.serial.SerialException:
            print("Serial Exception: Please check the Port, slave, and connection")
            pass
        finally:
            try:
                self.eurotherm3508_0.serial.close()
            except:
                pass
            
    def Euro3508_check(self):
        try:
            self.eurotherm3508_0 = Eurotherm3508('COM1', 1)
            self._eurotemp_0 = self.eurotherm3508_0.get_pv_loop1()
            self._eurocount_0 = self.eurotherm3508_0.get_op_loop1()
            print("OP counter = ", self._eurocount_0," %")
            print("Temperature = ", self._eurotemp_0," C")
        except IOError:
            print("Checking failed to read from instrument, please check the Port, slave, and connection")
            pass
        except self.eurotherm3508_0.serial.SerialException:
            print("Serial Exception: Please check the Port, slave, and connection")
            pass
        finally:
            try:
                self.eurotherm3508_0.serial.close()
            except:
                pass

        
##################################################################
#####Get the Widgets for modular function#####
##################################################################
    def module_sets(self): #Put a new module here
        self._posEuro = -20;self.ui.Euro_mod=[];self.ui.Eurocount = 0
        self._posHVPV = -20;self.ui.HVPV_mod=[];self.ui.HVPVcount = 0
        self._posHVPA = -20;self.ui.HVPA_mod=[];self.ui.HVPAcount = 0
        self._posTime = -20;self.ui.Time_mod=[];self.ui.Timecount = 0
        self._posShut = -20;self.ui.Shut_mod=[];self.ui.Shutcount = 0
        self._eurotemp_0 = 30
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
        text = self.ui.comboBox_20.currentText()
        self.settings = QtCore.QSettings( 'User', text )
        self.settings.setValue( "Eurocount", self.ui.Eurocount)
        self.settings.setValue( "HVPVcount", self.ui.HVPVcount)
        self.settings.setValue( "HVPAcount", self.ui.HVPAcount)
        self.settings.setValue( "Timecount", self.ui.Timecount)
        self.settings.setValue( "Shutcount", self.ui.Shutcount)
        self.settings.setValue( "modBox_0", self.ui.comboBox_2.currentIndex())
        self.settings.setValue( "modBox_1", self.ui.comboBox_5.currentIndex())
        self.settings.setValue( "modBox_2", self.ui.comboBox_17.currentIndex())
        self.settings.setValue( "modBox_3", self.ui.comboBox_16.currentIndex())
        self.settings.setValue( "modBox_4", self.ui.comboBox_18.currentIndex())
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
        text = self.ui.comboBox_20.currentText()
        self.settings = QtCore.QSettings( 'User', text )
        self.ui.comboBox_2.setCurrentIndex(self.settings.value("modBox_0"))
        self.ui.comboBox_5.setCurrentIndex(self.settings.value("modBox_1"))
        self.ui.comboBox_17.setCurrentIndex(self.settings.value("modBox_2"))
        self.ui.comboBox_16.setCurrentIndex(self.settings.value("modBox_3"))
        self.ui.comboBox_18.setCurrentIndex(self.settings.value("modBox_4"))
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
    