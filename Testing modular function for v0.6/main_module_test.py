# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:49:38 2022

@author: wilwin
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from module_test import Ui_MainWindow
from mod_widgets import DragGroup,button_group

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.setAcceptDrops(True)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

#        self.setAcceptDrops(True)
        self.ui.buttons = button_group(self.ui.centralwidget)

        #self.layout = QtWidgets.QVBoxLayout()
        #self.layout.addWidget(self.ui.buttons)
       # self.ui.setupUi.setCentralWidget(self.buttons)
        #self.ui.centralwidget.
        self.ui.buttons.pushButton.clicked.connect(DragGroup.add)

        self.show()

        
    def dragEnterEvent(self, e):
        e.accept()
        
    def dropEvent(self, e):
        pos = e.pos()
        self.ui.buttons.move(pos)
        print(pos)
        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
        

        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    