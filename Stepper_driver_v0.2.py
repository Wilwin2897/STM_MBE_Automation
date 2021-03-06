# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Stepper_driver.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import urllib3
http = urllib3.PoolManager()
zero_angle = 90
IP = '192.168.1.143'
def checkconnection():
    resp = http.request('GET', "http://"+IP,timeout=4.0)
    print(resp.status)
    return resp.status
def connect(angle1, angle2, angle3, angle4):
    string = str(angle1)+','+ str(angle2)+','+str(angle3)+','+str(angle4)+','
    print( "http://"+IP+"/command_"+string)
    response = http.request("GET", "http://"+IP+"/command_"+string, timeout=4.0)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 788)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(120, 90, 131, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(280, 90, 131, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(440, 90, 131, 51))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(600, 90, 131, 51))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(620, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 70, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 70, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(580, 70, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(740, 70, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(140, 390, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setRange(-180, 180)
        self.doubleSpinBox.setSingleStep(0.18)
        self.doubleSpinBox.setValue(0.0)        
        
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(300, 390, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setRange(-180, 180)
        self.doubleSpinBox_2.setSingleStep(0.18)
        self.doubleSpinBox_2.setValue(0.0)
        
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(460, 390, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_3.setRange(-180, 180)
        self.doubleSpinBox_3.setSingleStep(0.18)
        self.doubleSpinBox_3.setValue(0.0)
        
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(620, 390, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_4.setFont(font)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.doubleSpinBox_4.setRange(-180, 180)
        self.doubleSpinBox_4.setSingleStep(0.18)
        self.doubleSpinBox_4.setValue(0.0)

        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(150, 150, 71, 81))
        self.dial.setObjectName("dial")
        self.dial.setRange(-180, 180)
        self.dial.setValue(0)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(lambda: self.dialer())
        
        self.dial_2 = QtWidgets.QDial(self.centralwidget)
        self.dial_2.setGeometry(QtCore.QRect(310, 150, 71, 81))
        self.dial_2.setObjectName("dial_2")
        self.dial_2.setRange(-180, 180)
        self.dial_2.setValue(0)
        self.dial_2.setNotchesVisible(True)
        self.dial_2.valueChanged.connect(lambda: self.dialer_2())
        
        self.dial_3 = QtWidgets.QDial(self.centralwidget)
        self.dial_3.setGeometry(QtCore.QRect(460, 150, 71, 81))
        self.dial_3.setObjectName("dial_3")
        self.dial_3.setRange(-180, 180)
        self.dial_3.setValue(0)
        self.dial_3.setNotchesVisible(True)
        self.dial_3.valueChanged.connect(lambda: self.dialer_3())
        
        self.dial_4 = QtWidgets.QDial(self.centralwidget)
        self.dial_4.setGeometry(QtCore.QRect(620, 150, 71, 81))
        self.dial_4.setObjectName("dial_4")
        self.dial_4.setRange(-180, 180)
        self.dial_4.setValue(0)
        self.dial_4.setNotchesVisible(True)
        self.dial_4.valueChanged.connect(lambda: self.dialer_4())
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 350, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 320, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 450, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 540, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 680, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.run_process())
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(320, 0, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(610, 670, 171, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(610, 700, 181, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(250, 370, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(730, 370, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(410, 370, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(570, 370, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(240, 490, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setRange(0, 999)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(0)
        
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(450, 490, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setRange(0, 59)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_2.setValue(0)
        
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(350, 490, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(560, 490, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(350, 580, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(560, 580, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(240, 580, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setRange(0, 999)
        self.spinBox_3.setSingleStep(1)
        self.spinBox_3.setValue(0)
        
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(450, 580, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_4.setRange(0, 59)
        self.spinBox_4.setSingleStep(1)
        self.spinBox_4.setValue(0)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 680, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.reset())
        
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(340, 630, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(430, 640, 31, 21))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 250, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.run_manual())
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 250, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.reset())

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shutter system GUI v0.2"))
        self.label.setText(_translate("MainWindow", "Motor A"))
        self.label_2.setText(_translate("MainWindow", "Motor B"))
        self.label_3.setText(_translate("MainWindow", "Motor C"))
        self.label_5.setText(_translate("MainWindow", "Motor D"))
        self.label_7.setText(_translate("MainWindow", "o"))
        self.label_8.setText(_translate("MainWindow", "o"))
        self.label_9.setText(_translate("MainWindow", "o"))
        self.label_10.setText(_translate("MainWindow", "o"))
        self.label_4.setText(_translate("MainWindow", "Set angle"))
        self.label_6.setText(_translate("MainWindow", "Process control"))
        self.label_11.setText(_translate("MainWindow", "Set delay before opening"))
        self.label_14.setText(_translate("MainWindow", "Set delay before closing"))
        self.pushButton.setText(_translate("MainWindow", "Run!"))
        self.label_15.setText(_translate("MainWindow", "Manual tuning"))
        self.label_16.setText(_translate("MainWindow", "Connection Status :"))
        self.label_17.setText(_translate("MainWindow", "Arduino Wifi Rev2 connected"))
        self.label_18.setText(_translate("MainWindow", "o"))
        self.label_19.setText(_translate("MainWindow", "o"))
        self.label_20.setText(_translate("MainWindow", "o"))
        self.label_21.setText(_translate("MainWindow", "o"))
        self.label_22.setText(_translate("MainWindow", "minutes"))
        self.label_23.setText(_translate("MainWindow", "seconds"))
        self.label_24.setText(_translate("MainWindow", "minutes"))
        self.label_25.setText(_translate("MainWindow", "seconds"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.label_26.setText(_translate("MainWindow", "Repeat"))
        self.pushButton_3.setText(_translate("MainWindow", "Run!"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset"))

    def dialer(self):
        value = self.dial.value()
        self.lcdNumber.display(value)
   
    def dialer_2(self):
        value = self.dial_2.value()
        self.lcdNumber_2.display(value)
        
    def dialer_3(self):
        value = self.dial_3.value()
        self.lcdNumber_3.display(value)
        
    def dialer_4(self):
        value = self.dial_4.value()
        self.lcdNumber_6.display(value)
    
    def run_manual(self):
        Angle1 = self.dial.value()
        Angle2 = self.dial_2.value()
        Angle3 = self.dial_3.value()
        Angle4 = self.dial_4.value()
        print('Activated',Angle1, Angle2, Angle3, Angle4)
        self.send_data(Angle1, Angle2, Angle3, Angle4)
        
    def reset(self):
        print('Reseted',zero_angle, zero_angle, zero_angle, zero_angle)
        self.send_data(zero_angle, zero_angle, zero_angle, zero_angle)

    def run_process(self):
        delay = self.spinBox.value()*60+self.spinBox_2.value()
        Angle1 = self.doubleSpinBox.value()
        Angle2 = self.doubleSpinBox_2.value()
        Angle3 = self.doubleSpinBox_3.value()
        Angle4 = self.doubleSpinBox_4.value()
        Wait = self.spinBox_3.value()*60+self.spinBox_4.value()

        zero_list =[zero_angle,zero_angle,zero_angle,zero_angle]
        Angles = [Angle1,Angle2,Angle3,Angle4]
        print(delay,Angles,Wait)
        #get the minimum value in the list
        time.sleep(delay)
        print('Waiting before sending for ', delay,' seconds')
        self.send_data(Angles[0],Angles[1],Angles[2],Angles[3])
        print('Command sent')
        time.sleep(Wait)
        print('Waiting before closing for ', Wait,' seconds')
        self.send_data(zero_list[0],zero_list[1],zero_list[2],zero_list[3])
        print('process completed')
        if self.checkBox.isChecked():
            for i in range(10):
                print(delay,Angles,Wait)
                #get the minimum value in the list
                time.sleep(delay)
                print('Waiting before sending for ', delay,' seconds')
                self.send_data(Angles[0],Angles[1],Angles[2],Angles[3])
                print('Command sent')
                time.sleep(Wait)
                print('Waiting before closing for ', Wait,' seconds')
                self.send_data(zero_list[0],zero_list[1],zero_list[2],zero_list[3])
                print('iteration', i)
            
        
    def send_data(self,Angle1, Angle2, Angle3, Angle4):
        connect(Angle1, Angle2, Angle3, Angle4)
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
