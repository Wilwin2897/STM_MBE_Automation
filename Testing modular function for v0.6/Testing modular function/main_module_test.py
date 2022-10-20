# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:49:38 2022

@author: wilwin
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from module_test import Ui_MainWindow
from mod_widgets import DragGroup

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.setAcceptDrops(True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._add_pos = 0
        self.ui.buttons = DragGroup(self.ui.centralwidget)
        self.ui.buttons.pushButton.clicked.connect(self.add_button)
        self.show()
        
    def add_button(self):
        self._add_pos += 20
        #Add another button_group
        self.ui.buttons2 = DragGroup(self.ui.centralwidget)
        self.ui.buttons2.pushButton.clicked.connect(self.add_button)
        self.ui.buttons2.move(self._add_pos,self._add_pos)
        self.ui.buttons2.show()

    def dragEnterEvent(self, e):
        e.accept()
        
    def dropEvent(self, e):
        pos = e.pos()
        #How to make both buttons can move independently?
        e.source().move(pos)
        print(pos)
        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    