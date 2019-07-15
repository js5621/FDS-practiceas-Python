# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from question_r import Ui_Question
import question_r
import pymysql
from PyQt5.QtCore import QCoreApplication
from time import sleep
class Ui_fdsLogin(object):







    def create(self):
       
          
        conn = pymysql.connect(host='localhost', user='andro5621', password='js930519',
                       db='fdsDb', charset='utf8')
        try:
            with conn.cursor() as cursor:
                sql = 'INSERT INTO c_member (member_id, pwd,age,e_address,c_name) VALUES (%s, %s,%s,%s,%s)'
                cursor.execute(sql, (self.plainTextEdit.toPlainText(),self.plainTextEdit2.toPlainText(),
                                     self.plainTextEdit5.toPlainText(),self.plainTextEdit3.toPlainText(),self.plainTextEdit4.toPlainText()))
            conn.commit()
            print(cursor.lastrowid)
            
       
        finally:
            conn.close()
        sleep(1)
        self.close()
         
            
            
    def id_checking(self):
        id_list=[]
        id_col=[] 
        if not self.plainTextEdit.toPlainText() is '':
            conn = pymysql.connect(host='localhost', user='andro5621', password='js930519',
                       db='fdsDb', charset='utf8')
            try:
                with conn.cursor() as cursor:
                    sql = 'select member_id from c_member'
                    cursor.execute(sql)
                    rows=cursor.fetchall()
              
                    id_list=list(rows)
                    id_col=[ id_list[m_id][0] for m_id in range(0,len(id_list))]
                    if self.plainTextEdit.toPlainText() in id_col:
                        print("중복된 아이디 입니다")
                   

                    
                   
                    
                    
                    

                conn.commit()
           
            finally:
                conn.close()
            
                
        else:
            print("id를 입력해주세요")
       

    
        
            
            
   
            
        
    def setupUi(self, fds_Login):
        fds_Login.setObjectName("Login")
        fds_Login.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(fds_Login)
        self.centralwidget.setObjectName("centralwidget")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(20, 60, 111, 21))
        self.name_label.setObjectName("name_label")

        self.pwd_label = QtWidgets.QLabel(self.centralwidget)
        self.pwd_label.setGeometry(QtCore.QRect(20, 120, 111, 21))
        self.pwd_label.setObjectName("pwd_label")

        self.age_label = QtWidgets.QLabel(self.centralwidget)
        self.age_label.setGeometry(QtCore.QRect(10,180, 111, 21))
        self.age_label.setObjectName("ead_label")


        self.ead_label = QtWidgets.QLabel(self.centralwidget)
        self.ead_label.setGeometry(QtCore.QRect(10, 240, 111, 21))
        self.ead_label.setObjectName("ead_label")

        self.user_name_label = QtWidgets.QLabel(self.centralwidget)
        self.user_name_label.setGeometry(QtCore.QRect(10, 300, 111, 21))
        self.user_name_label.setObjectName("name_label")

        

        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 60, 131, 30))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.plainTextEdit2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit2.setGeometry(QtCore.QRect(50,120, 131, 30))
        self.plainTextEdit2.setObjectName("plainTextEdit2")

        self.plainTextEdit5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit5.setGeometry(QtCore.QRect(50,180, 131, 30))
        self.plainTextEdit5.setObjectName("plainTextEdit5")


        self.plainTextEdit3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit3.setGeometry(QtCore.QRect(50,240, 131, 30))
        self.plainTextEdit3.setObjectName("plainTextEdit3")

        self.plainTextEdit4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit4.setGeometry(QtCore.QRect(50,300, 131, 30))
        self.plainTextEdit4.setObjectName("plainTextEdit3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 60, 91, 31))
        self.pushButton.setObjectName("pushButton")

        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 60, 91, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushSubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushSubmitButton.setGeometry(QtCore.QRect(190, 240, 91, 31))
        self.pushSubmitButton.setObjectName("pushSubmitButton")

        
        fds_Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fds_Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        fds_Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(fds_Login)
        self.statusbar.setObjectName("statusbar")
        fds_Login.setStatusBar(self.statusbar)
        

        self.retranslateUi(fds_Login)
        QtCore.QMetaObject.connectSlotsByName(fds_Login)
        self.pushSubmitButton.clicked.connect(self.create)
        self.pushButton.clicked.connect(self.id_checking)
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.name_label.setText(_translate("Login", "id"))
        self.pwd_label.setText(_translate("Login", "pwd"))
        self.age_label.setText(_translate("Login", "age"))
        self.ead_label.setText(_translate("Login", "email"))
        self.user_name_label.setText(_translate("Login", "name"))
        self.pushButton.setText(_translate("Login", "id 중복확인"))
        self.pushSubmitButton.setText(_translate("Login", "제출"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fds_Login = QtWidgets.QMainWindow()
    ui = Ui_fdsLogin()
    ui.setupUi(fds_Login)
    fds_Login.show()
    sys.exit(app.exec_())

