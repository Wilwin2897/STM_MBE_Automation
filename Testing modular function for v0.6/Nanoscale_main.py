# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:31:55 2022
@author: wilwin
pip install lakeshore
with static IP address 169.254.125.29 port 7777 for 336
and 169.254.125.30 port 23 for TLC-500
Remember to set your computer IP address to static ip 169.254.125.XXX
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Nanoscale_GUI import Ui_MainWindow
from Nanoscale_widgets import Functions,EuroGroup,HVPower_Voltage,HVPower_Current,Time_delay,Stabilization_set,Shutter_set
from Nanoscale_default import default_parameters
from Nanoscale_instruments import Eurotherm3508
from Nanoscale_calibration import Calibration_OP_PV
import datetime
import time
import pyqtgraph as pg
import numpy as np
import pyvisa as visa
from lakeshore import Model336
from math import nan, isnan
from pyvisa import constants


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.setAcceptDrops(True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Set up initial variables
        self.port_serial = {'Te': 'COM1', 'Sn': 'COM2','BaF2': 'COM3', 'Co': 'COM4','Fe': 'COM5', 'Dy': 'COM6'}
        self.timer_1, self.timer_2, self.timer_3, self.wait, self.lp_timer , self._eurocount, self._eurotemp = ([None for i in range(6)] for j in range(7))
        
        self.Euroshot_count = [0,0,0,0,0,0]
        self.current_status = [0,0,0,0,0,0]
        self.my_dict = {}
        #Initialization
        self.module_sets()
        self.write_data_log()
        self.calibration = Calibration_OP_PV()
        self.ui.mbe_savegrowthtimeline_13.clicked.connect(self.run_processes)
        self.livedata_start()
        
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
        Ntimers = 5
        variables = {0: self.wait, 1: self.timer_1, 2: self.timer_2, 3: self.timer_3, 4: self.lp_timer}
        print("Stopping all timer, returning to manual hand-control")
        for i in range(Ntimers):
            v = variables[i]
            for j in range(6):
                try:
                    v[j].stop()
                except:
                    print('Timer %s (%i-th) was not started'%(i, j))
                    pass


##################################################################
########################Process Control###########################
##################################################################  
    def run_processes(self):    
        #Run every process with the same IDs with some specified delay
        #Will detect active modules and assign a process by each active module
        self.current_process_id = 0
        self.ui.mbe_savegrowthtimeline_13.setEnabled(False)
        executed = False
        if self.ui.Euro_mod !=[]:
            time_delay = [0 for i in range(10)]
            for i in range(len(self.ui.Time_mod)):
                process_id = self.ui.Time_mod[i].spinBox_2.value()
                minutes = self.ui.Time_mod[i].spinBox_1.value()
                seconds = self.ui.Time_mod[i].spinBox.value()
                time_delay[process_id] = (minutes*60+seconds)*1000
                
            for i in range(len(self.ui.Euro_mod)):
                selected = self.ui.Euro_mod[i].comboBox_2.currentText()
                process_id = self.ui.Euro_mod[i].spinBox.value()
                print('Selected cells:', selected)
                print('Process_ID:', process_id)
                self.my_dict.setdefault(process_id, [])
                self.my_dict[process_id].append([selected,i])
                #Think how to solve this map selected cell and proc id to one dic
                
                if process_id == 0:
                    self.process_Euro3508(selected,i)
                else:
                    #wait until previous id is finished
                    if executed == False:
                        self.timer_2[i] = QtCore.QTimer()
                        self.timer_2[i].timeout.connect(lambda: self.process_status_check(time_delay))
                        self.timer_2[i].start(10000)#check every 10 s regarding the status of PID1
                        executed = True
        else:
            print("No Eurotherm module detected, please add the widget before continuing")

    def process_status_check(self,time_delay):
        #Check the dict, see the PID 1, and multiply all current status if 1 then shoot next one
        #if #All process are completed, then do the next PID
        print('Active process ID and cells ', self.my_dict)
        mapping = {'Te': 0, 'Sn': 1,'BaF2': 2, 'Co': 3,'Fe': 4, 'Dy': 5}
        try:
            a = []
            for selected,i in self.my_dict[self.current_process_id]:
                a.append(self.current_status[mapping[selected]])
            status = 1
            for k in range(0,len(a)):
                status = status * a[k]
            if status == 1:
                print(status, ': All cell process has been finished, continuing to the next process')
                for selected,i in self.my_dict[self.current_process_id]:
                    QtCore.QTimer.singleShot(time_delay[self.current_process_id-1], lambda: self.process_Euro3508(selected,i))
                self.current_status[:] = 0
                self.current_process_id += 1
        except:
            self.current_process_id += 1
        
        print('current status: ', self.current_process_id, self.current_status)
        if self.current_process_id > 30:
            self.ui.mbe_savegrowthtimeline_13.setEnabled(True)
            self.timer_2.stop()
            
    def process_Euro3508(self,value,i):
        print('Running process for:', value)
        self.Euro3508_init(value,i)
        self.Euro3508_check(value,i)
        
        if self.ui.Euro_mod[i].mv_checkBox.checkState() == QtCore.Qt.Checked:
            print('PID control activated, using PID instead of fitted temperature data')
            P_value = self.ui.Euro_mod[i].doubleP.value()
            I_value = self.ui.Euro_mod[i].doubleI.value()
            D_value = self.ui.Euro_mod[i].doubleD.value()
            SP_value = self.ui.Euro_mod[i].doubleSpinBox .value()
            print('P = %.2f, I = %.2f, D = %.2f, SP = %.2f C' %(P_value,I_value,D_value,SP_value))
            self.Euro3508_send_PID(P_value,I_value,D_value,SP_value)
            self.timer_1[i] = QtCore.QTimer()
            self.timer_1[i].timeout.connect(self.Euro3508_check)
            self.timer_1[i].start(5000)
            self.Treach_count = 0
            #self.Tnotreach_count
            #Later check the stabilization procedure
            while abs(self._eurotemp_0-SP_value) < self.ui.Stabilizationset.doubleSpinBox_1.value():
                QtCore.QTimer.singleShot(20000, self.stabilization_T(SP_value,i))
                print(self.Treach_count)
        else:
            print('Using fitted temperature and output power data for ', value)
            SP_value = self.ui.Euro_mod[i].doubleSpinBox.value()
            rate = self.ui.Euro_mod[i].doubleSpinBox_2.value()
            print(value,self._eurotemp,SP_value,rate)
            timestep, nstep = self.calibration.time_rate(value,self._eurotemp[i],SP_value,rate)
            mode = self.ui.Euro_mod[i].comboBox.currentText()
            if mode == "Ramping up":
                mode = 'Increase(%)'
            else:
                mode = 'Decrease(%)'
            print(mode,value,nstep)
            print(self.Eurotherm_shots(mode,value,nstep,i))
            self.timer_1[i] = QtCore.QTimer()
            self.timer_1[i].timeout.connect(lambda: self.Eurotherm_shots(mode,SP_value,value,nstep,i))
            self.timer_1[i].start(int(timestep*1000))
            

    def stabilization_T(self,value,SP_value,i):
        QtCore.QTimer.singleShot(500, lambda : self.Euro3508_check(value,i))
        if abs(self._eurotemp[i]-SP_value) < self.ui.Stabilizationset.doubleSpinBox_1.value():
            self.Treach_count += 1
            self.Tnotreach_count =0
            if self.Treach_count >= 10:
                print("Temperature is stable at the Set Point ", SP_value)
                try:
                    self.timer_1[i].stop()
                except:
                    pass
                try:
                    self.timer_3[i].stop()
                except:
                    pass
                print('Fine tuning of Eurotherm finished, reached the SP_temperature')
                self.current_status[i] = 1

        else:
            self.Treach_count = 0
            self.Tnotreach_count += 1
            if self.Tnotreach_count >= 20:
                if self._eurotemp[i] < SP_value:
                    print('Fine increase')
                    self.timer_1[i] = QtCore.QTimer()
                    self.timer_1[i].timeout.connect(lambda: self.Euro3508_send_man('Increase(%)',value,i))
                    self.timer_1[i].start(int(20000)) 
                else:
                    print('Fine decrease')
                    self.timer_1[i] = QtCore.QTimer()
                    self.timer_1[i].timeout.connect(lambda: self.Euro3508_send_man('Decrease(%)',value,i))
                    self.timer_1[i].start(int(20000)) 
                #QtCore.QTimer.singleShot(500, lambda: self.Eurotherm_finetune(value,SP_value,i))
                self.Tnotreach_count = 0
                #self.timer3[i] = QtCore.QTimer()
                #self.timer3[i].timeout.connect(lambda: self.stabilization_T(value,SP_value,i))
                #self.timer3[i].start(int(800))
        return self.Treach_count
    
    def Eurotherm_finetune(self,value,SP_value,i):
        print('The temperature of %i is %.2f K, target is %.2f K'%(i, self._eurotemp[i], SP_value))
        self.timer3[i] = QtCore.QTimer()
        self.timer3[i].timeout.connect(lambda: self.stabilization_T(value,SP_value,i))
        self.timer3[i].start(int(1000)) 
         

    def Eurotherm_shots(self,mode,SP_value,value,nstep,i):
        self.Euro3508_send_man(mode,value,i)
        self.Euroshot_count[i] += 1
        print(value,self.Euroshot_count[i],nstep)
        if self.Euroshot_count[i] > nstep:
            print("Finished reaching the calibrated data point, now doing fine adjustment")
            self.timer_1[i].stop()
            self.Euroshot_count[i] = 0
            QtCore.QTimer.singleShot(15000, lambda: self.Eurotherm_finetune(value,SP_value,i))

        #self.Euro3508_check(value,i)
        print(self._eurotemp[i])
        
        #self.Euro3508_send('Increase(%)')
        
##################################################################
#####Communication with the instruments modular function#####
##############Eurotherm communication module#################
##################################################################    
    def Euro3508_init(self,value,i):
        serial = self.port_serial[value]
        try:
            self.eurotherm3508 = Eurotherm3508(serial, 1)
            self._eurotemp[i] = self.eurotherm3508.get_pv_loop1()
            self._eurocount[i] = self.eurotherm3508.get_op_loop1()
            self._eurocount[i]=round(self._eurocount[i],1)
            print("Connected to Eurotherm with OP counter = ", self._eurocount," %")
            print("Connected to Eurotherm with Temperature = ", self._eurotemp," C")
        except IOError:
            print("Initialization failed to read from instrument, please check the Port, slave, and connection")
        
        except self.eurotherm3508.serial.SerialException:
            print("Serial Exception: Please check the Port, slave, and connection")
            pass
        finally:
            try:
                self.eurotherm3508.serial.close()
            except:
                pass
            
    def Euro3508_send_man(self,mode,value,i):
        serial = self.port_serial[value]
        upperlim = 80
        if mode == 'Increase(%)':
            self._eurocount[i] += 0.1 # Percentage of Eurotherm
            if self._eurocount[i] > upperlim:
                self._eurocount[i] = upperlim
        if mode == 'Decrease(%)':
            self._eurocount[i] -= 0.1 # Percentage of Eurotherm
            if self._eurocount[i] < 0:
                self._eurocount[i] = 0  
        self._eurocount[i]=round(self._eurocount[i],1)
        print(self._eurocount[i])
        try:
            self.eurotherm3508 = Eurotherm3508(serial, 1)
            self.eurotherm3508.set_op_loop1(self._eurocount[i])
        except IOError:
            print("Sending failed to read from instrument, please check the Port, slave, and connection")
            pass
        except self.eurotherm3508.serial.SerialException:
            print("Serial Exception: Please check the Port, slave, and connection")
            pass
        finally:
            try:
                self.eurotherm3508.serial.close()
            except:
                pass
        
        QtCore.QTimer.singleShot(800, lambda : self.Euro3508_check(value,i))
            
    def Euro3508_send_PID(self,P,I,D,SP,value):
        serial = self.port_serial[value]
        try:
            self.eurotherm3508 = Eurotherm3508(serial, 1)
            self.eurotherm3508.set_PID_Proportional(P)
            self.eurotherm3508.set_PID_Integral(I)
            self.eurotherm3508.set_PID_Derivative(D)
            self.eurotherm3508.set_sp_loop1(SP)
        except IOError:
            print("Sending failed to read from instrument, please check the Port, slave, and connection")
            pass
        except self.eurotherm3508.serial.SerialException:
            print("Serial Exception: Please check the Port, slave, and connection")
            pass
        finally:
            try:
                self.eurotherm3508.serial.close()
            except:
                pass
            
    def Euro3508_check(self,value,i):
        serial = self.port_serial[value]
        try:
            self.eurotherm3508 = Eurotherm3508(serial, 1)
            self._eurotemp[i] = self.eurotherm3508.get_pv_loop1()
            self._eurocount[i] = self.eurotherm3508.get_op_loop1()
            self._eurocount[i]=round(self._eurocount[i],1)
            print("OP counter = ", self._eurocount," %")
            print("Temperature = ", self._eurotemp," C")
        except IOError:
            print("Checking failed to read from instrument, please check the Port, slave, and connection")
            pass
        except self.eurotherm3508.serial.SerialException:
            print("Serial Exception: Please check the Port, slave, and connection")
            pass
        finally:
            try:
                self.eurotherm3508.serial.close()
            except:
                pass
##################################################################          
##############High Voltage Power Supply module#################
##################################################################   





       
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


        
##################################################################
########################Plotting control##########################
################################################################## 
    def livedata_start(self):
        #EDIT- Live_plot_1#Today task finish plotting function
        self.plot_mode = {'T1,T2,T3,T4,JT,GGS vs time':[['T1','T2','T3','T4','JT','GGS'],'Temperature (K)'],'MBE pressure (mbar) vs time': [['PMBE'],'Pressure (mbar)'],\
                   'MBE+STM pressure (mbar) vs time': [['PMBE','PSTM'],'Pressure (mbar)'],'Beam Flux vs time':[['IG1'],'Beam Flux'] }
        self.ui.data_line = [None,None,None,None,None,None]
        self.update_plot()
        self.ui.mv_comboBox.currentTextChanged.connect(self.update_plot)
        self.ui.mv_unit_select.currentTextChanged.connect(self.update_plot)
        
        self.lp_timer[0] = QtCore.QTimer()
        self.lp_timer[0].timeout.connect(self.lcd_update)
        self.lp_timer[0].start(2000)
        self.lp_timer[1] = QtCore.QTimer()
        self.lp_timer[1].timeout.connect(self.write_data_log)
        self.lp_timer[1].start(8000)
        self.lp_timer[2] = QtCore.QTimer()
        self.lp_timer[2].timeout.connect(lambda:self.update_plot_data())
        self.lp_timer[2].start(2000)

    
    def update_plot(self):
        styles = {"color": "#000000", "font-size": "20px"}
        try:
            self.graphWidget.clear()
        except:
            print('Initiating live plot')
            self.graphWidget = pg.PlotWidget(self.ui.groupBox_10)
            self.graphWidget.setGeometry(QtCore.QRect(35, 75, 505, 285))
            self.graphWidget.showGrid(x=True, y=True)
            self.graphWidget.setTitle("" , color="black", size="15pt")
            self.graphWidget.setBackground('w')
        axis = pg.DateAxisItem(orientation='bottom')
        self.graphWidget.setAxisItems({'bottom':axis})
        mode  = self.ui.mv_comboBox.currentText()
        self.graphWidget.addLegend(offset=(1, 1),verSpacing=-5,brush='w')

        self.graphWidget.setLabel("bottom", self.ui.mv_unit_select.currentText(), **styles)
        self.graphWidget.setLabel("left", self.plot_mode[mode][1], **styles)
        self.x,self.y = self.read_data_log(self.plot_mode[mode][0],0,self.ui.mv_unit_select.currentText())
        colors = [(0, 0, 0),(255,0,0),(0,0,255),(0,255,0),(255,0,255),(100,0,100),(100,0,200)]
        for i in range(len(self.x)):
            self.ui.data_line[i] =  self.graphWidget.plot(x=[x.timestamp() for x in self.x[i]], y=self.y[i], pen=pg.mkPen(color=colors[i]),\
                                                          symbol='o',symbolPen =colors[i],symbolBrush='w', symbolSize = 6,name=self.plot_mode[mode][0][i])
    def update_plot_data(self):
        mode  = self.ui.mv_comboBox.currentText()
        self.x,self.y = self.read_data_log(self.plot_mode[mode][0],0,self.ui.mv_unit_select.currentText())
        for i in range(len(self.x)):
            self.ui.data_line[i].setData([x.timestamp() for x in self.x[i]],self.y[i])  # Update the data.

    def button_clicked(self):
        self.graphWidget.setTitle(self.ui.mv_title.text())
###############################################################
###############################################################
#######NON-ESSENTIAL FUNCTIONS (Logging,plotting,etc)##########
###############################################################
###############################################################

    def get_data(self):
        try:
            my_model_336 = Model336(ip_address='169.254.125.29')
            T_All = my_model_336.get_all_sensor_reading()
            rm = visa.ResourceManager() 
            tlc_ip = 'TCPIP0::169.254.125.30::23::SOCKET'
            TLC500 = rm.open_resource(tlc_ip)
            TLC500.read_termination = '\n'
            TLC500.write_termination = '\n'  
            TLC_out = [float(x) for x in TLC500.query('getOutput').split(', ')]
            TLC_out = [0 if isnan(i) else i for i in TLC_out ]
            TLC500.close()
            T1 = TLC_out[0]	
            T2 = TLC_out[1]
            T3 = TLC_out[2]	
            T4 = TLC_out[3]
            JT = T_All[0]	
            GGS = T_All[1]
        except:
            T1,T2,T3,T4,JT,GGS = 0,0,0,0,0,0	

        try:
            inficon = rm.open_resource('ASRL8::INSTR',read_termination='',write_termination='')
            rm.visalib.set_buffer(inficon.session, constants.VI_IO_IN_BUF, 32)
            rm.visalib.set_buffer(inficon.session, constants.VI_IO_OUT_BUF, 32)
            inficon.query("PR1\r\n")
            PLL = inficon.query("\05")
            PLOAD_L = float(PLL[3:]) 
            inficon.close()
        except:
            PLOAD_L = 0
            
            
        PSTM = 0
        PSTM_L= 0
        PMBE = 0
        PMBE_L = 0
        
        IG1 = 0
        PIR = 0
        A = 0
        TC = 0
        
        EF_T1 = 0
        EF_T2 = 0
        EF_T3 = 0
        EF_T4 = 0
        EF_T5 = 0
        EF_T6 = 0
        EF_P1 = 0
        EF_P2 = 0
        EF_P3 = 0
        EF_P4 = 0
        EF_P5 = 0
        EF_P6 = 0
        EF_V1 = 0
        EF_V2 = 0
        EF_V3 = 0
        EF_V4 = 0
        EF_V5 = 0
        EF_V6 = 0
        EF_A1 = 0
        EF_A2 = 0
        EF_A3 = 0
        EF_A4 = 0
        EF_A5 = 0
        EF_A6 = 0
        EB_V = 0
        EB_A = 0
        EB_FIL_V = 0
        EB_FIL_A = 0
        return (T1,T2,T3,T4,JT,GGS,PSTM,PSTM_L,PMBE,PMBE_L,PLOAD_L,IG1,PIR,A,TC,EF_T1,
            EF_T2,EF_T3,EF_T4,EF_T5,EF_T6,EF_P1,EF_P2,EF_P3,EF_P4,EF_P5,EF_P6,
            EF_V1,EF_V2,EF_V3,EF_V4,EF_V5,EF_V6,EF_A1,EF_A2,EF_A3,EF_A4,EF_A5,EF_A6,
            EB_V, EB_A, EB_FIL_V,EB_FIL_A)
    
    def read_data_log(self,args,timespan,mode):
        f = open("system_history.txt", "r")
        now = datetime.datetime.now()
        if timespan == 0:
            if mode == 'second (s)':
                timespan = datetime.timedelta(minutes= 10)
                interval = datetime.timedelta(seconds = 5)
            elif mode == 'minute (m)':
                timespan = datetime.timedelta(minutes= 60)
                interval = datetime.timedelta(minutes = 1)
            elif mode == 'hour (h)':
                timespan = datetime.timedelta(days= 1)
                interval = datetime.timedelta(hours = 1)
            elif mode == 'day (d)':
                timespan = datetime.timedelta(days= 30)
                interval = datetime.timedelta(hours = 12)
                
        prev_time = now - timespan
        lines = f.readlines()
        x_data = [[] for i in range(len(args))]
        y_data = [[] for i in range(len(args))]
        time_prev = datetime.datetime.strptime(lines[0], "%d/%m/%Y %H:%M:%S\n") 
        for i in range(0,len(lines)-7,10):
            if '/' in lines[i]:
                date = datetime.datetime.strptime(lines[i], "%d/%m/%Y %H:%M:%S\n")
                stripped = lines[i+1].replace('T1,T2,T3,T4,JT,GGS = ', '').replace(' K', '')
                T1,T2,T3,T4,JT,GGS = tuple(map(float, stripped.split(', ')))
                stripped = lines[i+2].replace('PSTM,PSTM_L,PMBE,PMBE_L,PLOAD_L = ', '').replace(' mbar', '')
                PSTM,PSTM_L,PMBE,PMBE_L,PLOAD_L = tuple(map(float, stripped.split(', ')))
                stripped = lines[i+3].replace('IG1,PIR,A,TC = ', '')
                IG1,PIR,A,TC = tuple(map(float, stripped.split(', ')))
                stripped = lines[i+4].replace('EF_T1,EF_T2,EF_T3,EF_T4,EF_T5,EF_T6 = ', '').replace(' K', '')
                EF_T1,EF_T2,EF_T3,EF_T4,EF_T5,EF_T6 = tuple(map(float, stripped.split(', ')))
                stripped = lines[i+5].replace('EF_P1,EF_P2,EF_P3,EF_P4,EF_P5,EF_P6 = ', '')
                EF_P1,EF_P2,EF_P3,EF_P4,EF_P5,EF_P6 = tuple(map(float, stripped.split(', ')))
                stripped = lines[i+6].replace('EF_V1,EF_V2,EF_V3,EF_V4,EF_V5,EF_V6 = ', '').replace(' V', '')
                EF_V1,EF_V2,EF_V3,EF_V4,EF_V5,EF_V6 = tuple(map(float, stripped.split(', ')))                          
                stripped = lines[i+7].replace('EF_A1,EF_A2,EF_A3,EF_A4,EF_A5,EF_A6 = ', '').replace(' A', '')
                EF_A1,EF_A2,EF_A3,EF_A4,EF_A5,EF_A6 = tuple(map(float, stripped.split(', ')))                          
                stripped = lines[i+8].replace('EB_V,EB_A,EB_FIL_V,EB_FIL_A = ', '').replace(' V', '').replace(' A', '')
                EB_V,EB_A,EB_FIL_V,EB_FIL_A = tuple(map(float, stripped.split(', ')))                          
            time_int = date-time_prev
            time_span = now - date
            if time_int >= interval:
                if time_span <= timespan:
                    for j in range(len(args)):
                        item = args[j]
                        y_data[j].append(locals()[f"{item}"])
                        x_data[j].append(date)
                time_prev = date
            else:
                time_prev = time_prev
        f.close()
        return x_data,y_data
        
    def write_data_log(self):
        (T1,T2,T3,T4,JT,GGS,PSTM,PSTM_L,PMBE,PMBE_L,PLOAD_L,IG1,PIR,A,TC,EF_T1,
            EF_T2,EF_T3,EF_T4,EF_T5,EF_T6,EF_P1,EF_P2,EF_P3,EF_P4,EF_P5,EF_P6,
            EF_V1,EF_V2,EF_V3,EF_V4,EF_V5,EF_V6,EF_A1,EF_A2,EF_A3,EF_A4,EF_A5,EF_A6,
            EB_V, EB_A, EB_FIL_V,EB_FIL_A) = self.get_data()
        f = open("system_history.txt", "a")
        now = datetime.datetime.now()
        f.write('%s\n' % (now.strftime("%d/%m/%Y %H:%M:%S")))
        f.write('T1,T2,T3,T4,JT,GGS = %.2f, %.2f, %.2f, %.2f, %.2f, %.2f K\n' % (T1,T2,T3,T4,JT,GGS))
        f.write('PSTM,PSTM_L,PMBE,PMBE_L,PLOAD_L = {:.2e}, {:.2e}, {:.2e}, {:.2e}, {:.2e} mbar\n'.format(PSTM,PSTM_L,PMBE,PMBE_L,PLOAD_L))
        f.write('IG1,PIR,A,TC = {:.2e}, {:.2e}, {:.2e}, {:.2e}\n'.format(IG1,PIR,A,TC))
        f.write('EF_T1,EF_T2,EF_T3,EF_T4,EF_T5,EF_T6 = %.2f, %.2f, %.2f, %.2f, %.2f, %.2f K\n' % (EF_T1,EF_T2,EF_T3,EF_T4,EF_T5,EF_T6))
        f.write('EF_P1,EF_P2,EF_P3,EF_P4,EF_P5,EF_P6 = %.1f, %.1f, %.1f, %.1f, %.1f, %.1f \n' % (EF_P1,EF_P2,EF_P3,EF_P4,EF_P5,EF_P6))
        f.write('EF_V1,EF_V2,EF_V3,EF_V4,EF_V5,EF_V6 = %.2f, %.2f, %.2f, %.2f, %.2f, %.2f V\n' % (EF_V1,EF_V2,EF_V3,EF_V4,EF_V5,EF_V6))
        f.write('EF_A1,EF_A2,EF_A3,EF_A4,EF_A5,EF_A6 = %.2f, %.2f, %.2f, %.2f, %.2f, %.2f A\n' % (EF_A1,EF_A2,EF_A3,EF_A4,EF_A5,EF_A6))
        f.write('EB_V,EB_A,EB_FIL_V,EB_FIL_A = %.2f V, %.2f A, %.2f V, %.2f A \n \n' % (EB_V, EB_A, EB_FIL_V,EB_FIL_A))
        f.close()
        
    def lcd_update(self):
        (T1,T2,T3,T4,JT,GGS,PSTM,PSTM_L,PMBE,PMBE_L,PLOAD_L,IG1,PIR,A,TC,EF_T1,
            EF_T2,EF_T3,EF_T4,EF_T5,EF_T6,EF_P1,EF_P2,EF_P3,EF_P4,EF_P5,EF_P6,
            EF_V1,EF_V2,EF_V3,EF_V4,EF_V5,EF_V6,EF_A1,EF_A2,EF_A3,EF_A4,EF_A5,EF_A6,
            EB_V, EB_A, EB_FIL_V,EB_FIL_A) = self.get_data()
        ####FIRST PAGE LCDs####
        self.ui.mv_lcd_T1.display(T1); self.ui.mv_lcd_T2.display(T2); self.ui.mv_lcd_T3.display(T3)
        self.ui.mv_lcd_T4.display(T4); self.ui.mv_lcd_JT.display(JT); self.ui.mv_lcd_GGS.display(GGS)
        self.ui.mv_lcd_P_stm.display(PSTM); self.ui.mv_lcd_P_mbeline.display(PMBE_L); self.ui.mv_lcd_P_stmline.display(PSTM_L)
        self.ui.mv_lcd_P_mbe.display(PMBE); self.ui.mv_lcd_P_loadlock.display(PLOAD_L); self.ui.mv_lcd_IG1.display(IG1)
        self.ui.mv_lcd_pir.display(PIR); self.ui.mv_lcd_a.display(A); self.ui.mv_lcd_Tc.display(TC)
        self.ui.mv_lcd_T_Te.display(EF_T1); self.ui.mv_lcd_T_Sn.display(EF_T2); self.ui.mv_lcd_T_BaF2.display(EF_T3)
        self.ui.mv_lcd_T_Co.display(EF_T4); self.ui.mv_lcd_T_Fe.display(EF_T5); self.ui.mv_lcd_T_Dy.display(EF_T6)
        self.ui.mv_lcd_p_Te.display(EF_P1); self.ui.mv_lcd_p_Sn.display(EF_P2); self.ui.mv_lcd_p_BaF2.display(EF_P3)
        self.ui.mv_lcd_p_Co.display(EF_P4); self.ui.mv_lcd_p_Fe.display(EF_P5); self.ui.mv_lcd_p_Dy.display(EF_P6)
        self.ui.mv_lcd_V_Te.display(EF_V1); self.ui.mv_lcd_V_Sn.display(EF_V2); self.ui.mv_lcd_V_BaF2.display(EF_V3)
        self.ui.mv_lcd_V_Co.display(EF_V4); self.ui.mv_lcd_V_Fe.display(EF_V5); self.ui.mv_lcd_V_Dy.display(EF_V6)
        self.ui.mv_lcd_A_Te.display(EF_A1); self.ui.mv_lcd_A_Sn.display(EF_A2); self.ui.mv_lcd_A_BaF2.display(EF_A3)  
        self.ui.mv_lcd_A_Co.display(EF_A4); self.ui.mv_lcd_A_Fe.display(EF_A5); self.ui.mv_lcd_A_Dy.display(EF_A6)
        self.ui.mv_lcd_V_bias.display(EB_V); self.ui.mv_lcd_A_bias.display(EB_A); self.ui.mv_lcd_V_fil.display(EB_FIL_V)  
        self.ui.mv_lcd_A_fil.display(EB_FIL_A) 
        self.ui.mv_lcd_shut_Te.display(1); self.ui.mv_lcd_shut_Sn.display(1); self.ui.mv_lcd_shut_BaF2.display(1)  
        self.ui.mv_lcd_shut_Co.display(1); self.ui.mv_lcd_shut_Fe.display(1); self.ui.mv_lcd_shut_Dy.display(1)  
        ####SECOND PAGE LCDs####
        self.ui.mbe_lcd_T_Te.display(EF_T1); self.ui.mbe_lcd_T_Sn.display(EF_T2); self.ui.mbe_lcd_T_Baf2.display(EF_T3)
        self.ui.mbe_lcd_T_Co.display(EF_T4); self.ui.mbe_lcd_T_Fe.display(EF_T5); self.ui.mbe_lcd_T_Dy.display(EF_T6)
        self.ui.mbe_lcd_p_Te.display(EF_P1); self.ui.mbe_lcd_p_Sn.display(EF_P2); self.ui.mbe_lcd_p_Baf2.display(EF_P3)
        self.ui.mbe_lcd_p_Co.display(EF_P4); self.ui.mbe_lcd_p_Fe.display(EF_P5); self.ui.mbe_lcd_p_Dy.display(EF_P6)
        self.ui.mbe_lcd_V_Te.display(EF_V1); self.ui.mbe_lcd_V_Sn.display(EF_V2); self.ui.mbe_lcd_V_Baf2.display(EF_V3)
        self.ui.mbe_lcd_V_Co.display(EF_V4); self.ui.mbe_lcd_V_Fe.display(EF_V5); self.ui.mbe_lcd_V_Dy.display(EF_V6) 
        self.ui.mbe_lcd_A_Te.display(EF_A1); self.ui.mbe_lcd_A_Sn.display(EF_A2); self.ui.mbe_lcd_A_Baf2.display(EF_A3)
        self.ui.mbe_lcd_A_Co.display(EF_A4); self.ui.mbe_lcd_A_Fe.display(EF_A5); self.ui.mbe_lcd_A_Dy.display(EF_A6) 
        self.ui.mbe_lcd_V_bias.display(EB_V); self.ui.mbe_lcd_A_bias.display(EB_A); self.ui.mbe_lcd_V_fil.display(EB_FIL_V) 
        self.ui.mbe_lcd_A_fil.display(EB_FIL_A) 
        self.ui.mbe_lcd_shut_Te.display(2); self.ui.mbe_lcd_shut_Sn.display(2); self.ui.mbe_lcd_shut_Baf2.display(2)  
        self.ui.mbe_lcd_shut_Co.display(2); self.ui.mbe_lcd_shut_Fe.display(2); self.ui.mbe_lcd_shut_Dy.display(2) 
        self.ui.mbe_lcd_P_mbe.display(PMBE); self.ui.mbe_lcd_P_mbeline.display(PMBE_L); self.ui.mbe_lcd_P_loadlock.display(PLOAD_L)
        self.ui.mbe_progressBar.setValue(int(0.2)) 
        ####THIRD PAGE LCDs####  
        self.ui.man_T_Te.display(self._eurotemp[0]);self.ui.man_T_Sn.display(self._eurotemp[1]);self.ui.man_T_Baf2.display(self._eurotemp[2])
        self.ui.man_T_Co.display(self._eurotemp[3]);self.ui.man_T_Fe.display(self._eurotemp[4]);self.ui.man_T_Dy.display(self._eurotemp[5])
        self.ui.man_p_Te.display(self._eurocount[0]);self.ui.man_p_Sn.display(self._eurocount[1]);self.ui.man_p_Baf2.display(self._eurocount[2])
        self.ui.man_p_Co.display(self._eurocount[3]);self.ui.man_p_Fe.display(self._eurocount[4]);self.ui.man_p_Dy.display(self._eurocount[5])
        #self.ui.man_progressBar_Te.setValue(self._eurocount[0]);self.ui.man_progressBar_Sn.setValue(self._eurocount[1]) 
        #self.ui.man_progressBar_Baf2.setValue(self._eurocount[2]);self.ui.man_progressBar_Co.setValue(self._eurocount[3]) 
        #self.ui.man_progressBar_Fe.setValue(self._eurocount[4]);self.ui.man_progressBar_Dy.setValue(self._eurocount[5]) 
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    