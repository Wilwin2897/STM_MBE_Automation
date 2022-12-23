# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:32:21 2022

@author: wilwin
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class EuroGroup(QtWidgets.QWidget):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 261, 171))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(50, 50, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 151, 16))
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(50, 100, 131, 22))
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setProperty("value", 300.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 151, 16))
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(50, 140, 131, 22))
        self.doubleSpinBox_2.setMaximum(100.0)
        self.doubleSpinBox_2.setProperty("value", 10.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.add_button = QtWidgets.QPushButton(self.groupBox)
        self.add_button.setGeometry(QtCore.QRect(190, 110, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.remove_button = QtWidgets.QPushButton(self.groupBox)
        self.remove_button.setGeometry(QtCore.QRect(190, 140, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(190, 70, 42, 22))
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(170, 75, 21, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 20, 51, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_104 = QtWidgets.QLabel(self.groupBox)
        self.label_104.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label_104.setObjectName("label_104")
        self.label_P = QtWidgets.QLabel(self.groupBox)
        self.label_P.setGeometry(QtCore.QRect(130, 5, 41, 16))
        self.label_P.setObjectName("P:")
        self.label_I = QtWidgets.QLabel(self.groupBox)
        self.label_I.setGeometry(QtCore.QRect(180, 5, 41, 16))
        self.label_I.setObjectName("I:")
        self.label_D = QtWidgets.QLabel(self.groupBox)
        self.label_D.setGeometry(QtCore.QRect(230, 5, 41, 16))
        self.label_D.setObjectName("D:")
        self.doubleP = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleP.setGeometry(QtCore.QRect(110, 20, 51, 22))
        self.doubleP.setMaximum(9999.0)
        self.doubleP.setProperty("value", 20.0)
        self.doubleP.setObjectName("doubleSpinBox_2")
        self.doubleI = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleI.setGeometry(QtCore.QRect(160, 20, 51, 22))
        self.doubleI.setMaximum(9999.0)
        self.doubleI.setProperty("value", 360.0)
        self.doubleI.setObjectName("doubleSpinBox_2")
        self.doubleD = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleD.setGeometry(QtCore.QRect(210, 20, 51, 22))
        self.doubleD.setMaximum(9999.0)
        self.doubleD.setProperty("value", 60.0)
        self.doubleD.setObjectName("doubleSpinBox_2")
        self.mv_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.mv_checkBox.setGeometry(QtCore.QRect(190, 48, 81, 22))
        self.mv_checkBox.setText("PID On")
        self.mv_checkBox.setObjectName("mv_checkBox_Fe")
        self.retranslateUi()
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Eurotherm module"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Ramping up"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cooling down"))
        self.label_1.setText(_translate("MainWindow", "Mode"))
        self.label_2.setText(_translate("MainWindow", "Target Temperature (K):"))
        self.label_3.setText(_translate("MainWindow", "Rate Setting (K/min)"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))
        self.label_4.setText(_translate("MainWindow", "ID:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Te"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Sn"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "BaF2"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Co"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Fe"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Dy"))
        self.label_104.setText(_translate("MainWindow", "Select:"))
        self.label_P.setText(_translate("MainWindow", "P:"))
        self.label_I.setText(_translate("MainWindow", "I:"))
        self.label_D.setText(_translate("MainWindow", "D:"))
    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)
            mime =QtCore.QMimeData()
            drag.setMimeData(mime)
            pixmap = QtGui.QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(QtCore.Qt.MoveAction)
            
    
class HVPower_Voltage(QtWidgets.QWidget):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 241, 151))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(50, 20, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 50, 151, 16))
        self.label_1.setObjectName("label_1")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(50, 70, 131, 22))
        self.doubleSpinBox.setMaximum(1500.0)
        self.doubleSpinBox.setProperty("value", 300.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 151, 16))
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(50, 120, 131, 22))
        self.doubleSpinBox_2.setMaximum(100.0)
        self.doubleSpinBox_2.setProperty("value", 10.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.add_button = QtWidgets.QPushButton(self.groupBox)
        self.add_button.setGeometry(QtCore.QRect(190, 80, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.label_97 = QtWidgets.QLabel(self.groupBox)
        self.label_97.setGeometry(QtCore.QRect(190, 20, 21, 16))
        self.label_97.setObjectName("label_97")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(190, 40, 42, 22))
        self.spinBox_2.setProperty("value", 1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.remove_button = QtWidgets.QPushButton(self.groupBox)
        self.remove_button.setGeometry(QtCore.QRect(190, 110, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.retranslateUi()
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "HV Power Supply (Voltage)"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Ramping up"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cooling down"))
        self.label.setText(_translate("MainWindow", "Mode"))
        self.label_1.setText(_translate("MainWindow", "Target Voltage (V):"))
        self.label_2.setText(_translate("MainWindow", "Rate Setting (V/min)"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.label_97.setText(_translate("MainWindow", "ID"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))
        
    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)
            mime =QtCore.QMimeData()
            drag.setMimeData(mime)
            pixmap = QtGui.QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(QtCore.Qt.MoveAction)
            
            
class HVPower_Current(QtWidgets.QWidget):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 241, 151))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(50, 20, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 50, 151, 16))
        self.label_1.setObjectName("label_1")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(50, 70, 131, 22))
        self.doubleSpinBox.setMaximum(5.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 151, 16))
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_1.setGeometry(QtCore.QRect(50, 120, 131, 22))
        self.doubleSpinBox_1.setMaximum(0.5)
        self.doubleSpinBox_1.setSingleStep(0.01)
        self.doubleSpinBox_1.setProperty("value", 0.1)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.add_button = QtWidgets.QPushButton(self.groupBox)
        self.add_button.setGeometry(QtCore.QRect(190, 80, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setGeometry(QtCore.QRect(190, 40, 42, 22))
        self.spinBox_3.setProperty("value", 1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(190, 20, 21, 16))
        self.label_3.setObjectName("label_3")
        self.remove_button = QtWidgets.QPushButton(self.groupBox)
        self.remove_button.setGeometry(QtCore.QRect(190, 110, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.retranslateUi()
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "HV Power Supply (Current)"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Ramping up"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cooling down"))
        self.label.setText(_translate("MainWindow", "Mode"))
        self.label_1.setText(_translate("MainWindow", "Target Current (A):"))
        self.label_2.setText(_translate("MainWindow", "Rate Setting (A/min)"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "ID"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))
        
    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)
            mime =QtCore.QMimeData()
            drag.setMimeData(mime)
            pixmap = QtGui.QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(QtCore.Qt.MoveAction)
            
            
class Time_delay(QtWidgets.QWidget):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 231, 81))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 20, 21, 16))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(20, 20, 51, 22))
        self.spinBox.setMaximum(9999)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_1 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_1.setGeometry(QtCore.QRect(100, 20, 51, 22))
        self.spinBox_1.setMaximum(9999)
        self.spinBox_1.setProperty("value", 100)
        self.spinBox_1.setObjectName("spinBox_1")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(160, 20, 51, 16))
        self.label_1.setObjectName("label_1")
        self.add_button = QtWidgets.QPushButton(self.groupBox)
        self.add_button.setGeometry(QtCore.QRect(120, 50, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.remove_button = QtWidgets.QPushButton(self.groupBox)
        self.remove_button.setGeometry(QtCore.QRect(170, 50, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(70, 50, 42, 22))
        self.spinBox_2.setProperty("value", 1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.retranslateUi()
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Time Delay"))
        self.label.setText(_translate("MainWindow", "(s)"))
        self.label_1.setText(_translate("MainWindow", "(min)"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))
        self.label_2.setText(_translate("MainWindow", "from PID"))
        
    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)
            mime =QtCore.QMimeData()
            drag.setMimeData(mime)
            pixmap = QtGui.QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(QtCore.Qt.MoveAction)
            
            
class Stabilization_set(QtWidgets.QWidget):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(0,0, 241, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 16))
        self.label.setObjectName("label")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(50, 40, 131, 22))
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setProperty("value", 2.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_1.setGeometry(QtCore.QRect(50, 90, 131, 22))
        self.doubleSpinBox_1.setMaximum(10.0)
        self.doubleSpinBox_1.setSingleStep(0.1)
        self.doubleSpinBox_1.setProperty("value", 0.5)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 70, 231, 16))
        self.label_1.setObjectName("label_1")
        self.retranslateUi()
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Stabilization settings"))
        self.label.setText(_translate("MainWindow", "Safe pressure threshold (E-9 mbar)"))
        self.label_1.setText(_translate("MainWindow", "Temperature stabilization threshold (K)"))
        
    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)
            mime =QtCore.QMimeData()
            drag.setMimeData(mime)
            pixmap = QtGui.QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(QtCore.Qt.MoveAction)
            
class Shutter_set(QtWidgets.QWidget):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Change self.tab to self
        self.groupBox = QtWidgets.QGroupBox(self)
        #Always change the origin to 0,0 then move to the desireable position in main.py
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 271, 71))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 20, 101, 16))
        self.label.setObjectName("label")
        self.add_button = QtWidgets.QPushButton(self.groupBox)
        self.add_button.setGeometry(QtCore.QRect(210, 10, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.remove_button = QtWidgets.QPushButton(self.groupBox)
        self.remove_button.setGeometry(QtCore.QRect(210, 40, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(160, 20, 21, 16))
        self.label_1.setObjectName("label_1")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(160, 40, 42, 22))
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(90, 40, 51, 22))
        self.spinBox_2.setMinimum(-180)
        self.spinBox_2.setMaximum(180)
        self.spinBox_2.setProperty("value", 90)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 61, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.retranslateUi()
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Shutter module"))
        self.label.setText(_translate("MainWindow", "Angle (degree)"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))
        self.label_1.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Select:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))

        
    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)
            mime =QtCore.QMimeData()
            drag.setMimeData(mime)
            pixmap = QtGui.QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(QtCore.Qt.MoveAction)

class Functions(QtWidgets.QWidget):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def Estimate_time(warm1,warm2,warm3,cool1,cool2,cool3,maxTempA,maxTempB,maxTempC,delay,anneal):
        time = 0
        time = 300/warm1 + 500/warm2 - 300/cool1-500/cool2
        time += (maxTempA-800)/warm3 - (maxTempA-800)/cool3
        time += (maxTempB-800)/warm3 - (maxTempB-800)/cool3
        time += (maxTempC-800)/warm3 - (maxTempC-800)/cool3
        time += delay + anneal
        hours, minutes= divmod(time, 60)
        string = str(int(hours))+' hours and '+ str(int(minutes))+' minutes'        
        return string

    def get_toy_data():
        T1 = np.random.uniform(335.5, 375.5)	
        T2 = np.random.uniform(335.5, 375.5)	
        T3 = np.random.uniform(335.5, 375.5)	
        T4 = np.random.uniform(335.5, 375.5)	
        JT = np.random.uniform(335.5, 375.5)	
        GGS = np.random.uniform(335.5, 375.5)	
        PSTM = np.random.uniform(3.E-10, 3.E-9)
        PSTM_L= np.random.uniform(3.E-10, 3.E-9)
        PMBE = np.random.uniform(3.E-10, 3.E-9)
        PMBE_L = np.random.uniform(3.E-10, 3.E-9)
        PLOAD_L= np.random.uniform(3.E-10, 3.E-9)
        IG1 = np.random.uniform(3.E-10, 3.E-9)
        PIR = np.random.uniform(3.E-10, 3.E-9)
        A = np.random.uniform(0.1, 1)
        TC = np.random.uniform(20, 300)
        EF_T1 = np.random.uniform(20, 300)
        EF_T2 = np.random.uniform(20, 300)
        EF_T3 = np.random.uniform(20, 300)
        EF_T4 = np.random.uniform(20, 300)
        EF_T5 = np.random.uniform(20, 300)
        EF_T6 = np.random.uniform(20, 300)
        EF_P1 = np.random.uniform(0, 100)
        EF_P2 = np.random.uniform(0, 100)
        EF_P3 = np.random.uniform(0, 100)
        EF_P4 = np.random.uniform(0, 100)
        EF_P5 = np.random.uniform(0, 100)
        EF_P6 = np.random.uniform(0, 100)
        EF_V1 = np.random.uniform(0, 4.5)
        EF_V2 = np.random.uniform(0, 4.5)
        EF_V3 = np.random.uniform(0, 4.5)
        EF_V4 = np.random.uniform(0, 4.5)
        EF_V5 = np.random.uniform(0, 4.5)
        EF_V6 = np.random.uniform(0, 4.5)
        EF_A1 = np.random.uniform(0, 4.5)
        EF_A2 = np.random.uniform(0, 4.5)
        EF_A3 = np.random.uniform(0, 4.5)
        EF_A4 = np.random.uniform(0, 4.5)
        EF_A5 = np.random.uniform(0, 4.5)
        EF_A6 = np.random.uniform(0, 4.5)
        EB_V = np.random.uniform(0, 1000)
        EB_A = np.random.uniform(0, 1)
        EB_FIL_V = np.random.uniform(0, 5)
        EB_FIL_A = np.random.uniform(0, 8)
        return (T1,T2,T3,T4,JT,GGS,PSTM,PSTM_L,PMBE,PMBE_L,PLOAD_L,IG1,PIR,A,TC,EF_T1,
            EF_T2,EF_T3,EF_T4,EF_T5,EF_T6,EF_P1,EF_P2,EF_P3,EF_P4,EF_P5,EF_P6,
            EF_V1,EF_V2,EF_V3,EF_V4,EF_V5,EF_V6,EF_A1,EF_A2,EF_A3,EF_A4,EF_A5,EF_A6,
            EB_V, EB_A, EB_FIL_V,EB_FIL_A)
    
    def generate_init_timeline():
        heating_rate = [12, 8, 6, 4, 3, 2]
        cooling_rate = [12, 8, 6, 4, 3, 2]
        activate = [1, 1, 1, 1]
        substrate_rate = [100, 0.2]
        substrate_set = [1004.2, 3.80]
        standby_temp = [800, 800, 1100, 1100]
        opening_temp = [1060.2, 1050, 1430, 1430]
        opening_time = [30, 15, 30, 30]
        delay_time = [0, 90, 0, 0] #Delay is counted after the first shutter is open
        annealing_para = [1004.2, 3.80, 720]
        temperature_fixed_points = [200, 300, 250, 250, 250, 250]
        pressure_threshold = 2.e-9
        target_temp = []
        delayed=[]
        for i in range(4):
            if delay_time[i] == 0:
               target_temp.append(opening_temp[i])
            else:
               target_temp.append(standby_temp[i])
               delayed.append(i)
        
        print(target_temp)
        string  = ""
        string += "######################\n#PROGRAM STARTS HERE\n######################\n"
        string += "#set [Time (second)] [Commands] [Arguments] \n"
        c = "set "
        string += c+"0 0000\n" 
        string += c+"5 0001\n" 
        string += c+"10 0002\n" 
        time = 10
        current_temp = 23.0 #Check from output
        current_percent = 0
        #For x Celcius increase = y percentage of % power.
        T_to_percent_ratio = 1/0.6 #1K=0.6 percent step (0.06%) increase 
                                #May change with temperature, need a dynamic feedback loop
                                
    #Substrate heating
        steps_voltage = substrate_rate[0]/20
        minutes_voltage = int(substrate_set[0]/substrate_rate[0])
        for minute in range(minutes_voltage):
            for i in range(int(steps_voltage)):
                time += 60/steps_voltage
                string += c+"%i 4002\n"%(time)
        steps_current = substrate_rate[1]/0.05
        minutes_current = int(substrate_set[1]/substrate_rate[1])
        for minute in range(minutes_current):
            for i in range(int(steps_current)):
                time += 60/steps_current
                string += c+"%i 4005\n"%(time)
            
    #Heating part
        for point in range(len(temperature_fixed_points)):
            percent_steps = heating_rate[point]/T_to_percent_ratio
            minutes = int(temperature_fixed_points[point]/heating_rate[point])
            #print("#Temperature fixed point ",current_temp)
            for minute in range(minutes):
                for i in range(int(percent_steps)):
                    time += 60/percent_steps
                    current_temp += T_to_percent_ratio
                    current_percent += 0.1
                    print("#Time = %8i s, Temp = %5.1f K, Percent = %5.1f " %(time,current_temp,current_percent))
                    if (activate[0]==1 and current_temp <= target_temp[0]) :
                        string += c+"%i 3001\n"%(time)
                    if (activate[1]==1 and current_temp <= target_temp[1]):
                        string += c+"%i 3003\n"%(time)
                    if (activate[2]==1 and current_temp <= target_temp[2]):
                        string += c+"%i 3005\n"%(time)
                    if (activate[3]==1 and current_temp <= target_temp[3]):
                        string += c+"%i 3007\n"%(time)       
                    for j in delayed:
                        if (current_temp <= opening_temp[j]) :
                                string += c+"%i 300%i %f A\n"%(time+opening_time[j]*60+delay_time[j]*60,2*j+1,current_temp) 
    
    #Temperature stabilization and shutter opening part
    
    #Cooling part
        for point in range(len(temperature_fixed_points)):
            percent_steps = cooling_rate[-point]/T_to_percent_ratio
            minutes = int(temperature_fixed_points[-point]/cooling_rate[-point])
            #print("#Temperature fixed point ",current_temp)
            for minute in range(minutes):
                for i in range(int(percent_steps)):
                    time += 60/percent_steps
                    current_temp -= T_to_percent_ratio
                    current_percent -= 0.1
                    print("#Time = %8i s, Temp = %5.1f K, Percent = %5.1f " %(time,current_temp,current_percent))
                    if (activate[0]==1 and delay_time[0]==0) :
                        string += c+"%i 3002\n"%(time+delay_time[0]*60+opening_time[0]*60)
                    if (activate[1]==1 and delay_time[1]==0):
                        string += c+"%i 3004\n"%(time+delay_time[1]*60+opening_time[1]*60)
                    if (activate[2]==1 and delay_time[2]==0):
                        string += c+"%i 3006\n"%(time+delay_time[2]*60+opening_time[2]*60)
                    if (activate[3]==1 and delay_time[3]==0):
                        string += c+"%i 3008\n"%(time+delay_time[3]*60+opening_time[3]*60)            
    #Annealing
    
    #Update information every 12 seconds
        interval = 12
        for i in range(int(time/interval)):
            string += c+"%i 1002\n"%(i*interval+interval)
            string += c+"%i 1007\n"%(i*interval+interval)
    
    #Sorting timeline
    
        timeline_file = open("timeline.txt", "wt")
        timeline_file.write(string)
        timeline_file.close()                  
        return string