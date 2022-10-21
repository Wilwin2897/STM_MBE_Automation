# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 22:25:05 2022

@author: wilwin
"""
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc 
from PyQt5 import QtGui as qtg #font, etc modules

class MainWindow(qtw.QWidget):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)#give reference to the parent opbject 
        # Your code will go here
        self.show()
        

if __name__ == '__main__': #run this if I run this script not other scripts
    app = qtw.QApplication(sys.argv) #sys to makesure everyone can execute it
    w =  MainWindow(windowTitle='hello word') #Where the bulk of the program
    sys.exit(app.exec_())#Usually the last line will run until the program exit, so the user would expect in a certain platform

