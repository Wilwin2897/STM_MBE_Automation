# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:32:21 2022

@author: wilwin
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class EuroGroup(QtWidgets.QWidget):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 241, 171))
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
        self.label_4.setGeometry(QtCore.QRect(190, 50, 21, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 20, 61, 22))
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
        self.label_4.setText(_translate("MainWindow", "PID"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Te"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Sn"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "BaF2"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Co"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Fe"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Dy"))
        self.label_104.setText(_translate("MainWindow", "Select:"))
        
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
        self.label_97.setText(_translate("MainWindow", "PID"))
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
        self.label_3.setText(_translate("MainWindow", "PID"))
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.retranslateUi()
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Shutter module"))
        self.label.setText(_translate("MainWindow", "Angle (degree)"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))
        self.label_1.setText(_translate("MainWindow", "PID"))
        self.label_2.setText(_translate("MainWindow", "Select:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Te"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Sn"))
        self.comboBox.setItemText(2, _translate("MainWindow", "BaF2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Co"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Fe"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Dy"))
        
    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)
            mime =QtCore.QMimeData()
            drag.setMimeData(mime)
            pixmap = QtGui.QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(QtCore.Qt.MoveAction)