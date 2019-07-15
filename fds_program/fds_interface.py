# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import ranking
from PyQt5 import QtCore, QtGui, QtWidgets
from openWdw_r import Ui_NewWindow
from question_r import Ui_Question
from ranking import Ui_Rank
from fds_Login import Ui_fdsLogin
from checking import Ui_Checking
from time import sleep

class Ui_MainWindow(object):
    
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_fdsLogin()
        self.ui.setupUi(self.window)
        self.window.show()
      

    def openLWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openRWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Checking()
        self.ui.setupUi(self.window)
      
        self.window.show()
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 241, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 220, 241, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 370, 251, 101))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 0, 181, 71))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton_2.clicked.connect(self.openLWindow)
        self.pushButton_3.clicked.connect(self.openRWindow)
        
   
  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "회원가입"))
        self.pushButton_2.setText(_translate("MainWindow", "회원정보 수정"))
        self.pushButton_3.setText(_translate("MainWindow", "회원 카드 조회"))
        self.label.setText(_translate("MainWindow", "사기 결제 탐지"))

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())

