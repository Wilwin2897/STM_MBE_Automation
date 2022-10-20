# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:17:41 2022

@author: wilwin
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class DragGroup(QtWidgets.QWidget):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 211, 151))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 110, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox.setTitle("Test module")
        self.pushButton.setText("Add")
        self.pushButton_2.setText("Remove")
        self.pushButton_2.setText("Remove")
        
    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)
            mime =QtCore.QMimeData()
            drag.setMimeData(mime)
            pixmap = QtGui.QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(QtCore.Qt.MoveAction)
            
#Create a independent Widgets class for each module 

        
    
        
        
        
