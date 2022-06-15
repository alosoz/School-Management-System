import hashlib, binascii, os # to hash passwords
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
import sys
import psycopg2
import teacher_forget_password, teacher

class TeacherLogin(QMainWindow):
    def __init__(self):
        super(TeacherLogin, self).__init__()
        uic.loadUi('ui/teacher_login.ui', self)
        self.teacher_login.clicked.connect(self.login)
        self.teacher_forgot.clicked.connect(self.forgot_password)
        self.conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '1234')

        self.show()

    def login(self):
        try:
            cur = self.conn.cursor() 
            user_name = self.username.text()
            password = self.teacher_password.text()                  
            query = "SELECT user_name,password from teachers where user_name like '"+user_name + "'and password like '" +password + "'"
            cur.execute(query)
            result = cur.fetchone() 
            if result == None:
                self.labelResult.setText("Incorrect UserName or Password") 
            else:
                self.labelResult.setText("You are logged in")
                # mydialog =QDialog()
                # mydialog.setModal(True)
                # mydialog.exec_()
                self.cams = teacher.Teacher()
        except psycopg2.Error as e:
            self.labelResult.setText("Error")
    def forgot_password(self):
        self.cams = teacher_forget_password.TeacherForgetPassword()

    
    

    def hash_password(password): #Hash a password for storing
        conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '1234')
        cur = conn.cursor()
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(stored_password, provided_password):#Verify a stored password against one provided by user
        conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '1234')
        cur = conn.cursor()
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

if (__name__ == '__main__'):
    # Main App
    app=QApplication(sys.argv)
    mainwindow=TeacherLogin()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    # window = Ui_teacher_functions()
    widget.setFixedWidth(800)
    widget.setFixedHeight(800)
    widget.show()
    app.exec_()