import hashlib, binascii, os # to hash passwords
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
import sys
import psycopg2
import student_forget_password,student


class StudentLogin(QMainWindow):
    def __init__(self):
        super(StudentLogin, self).__init__()
        uic.loadUi('ui/student_login.ui', self)
        self.student_login.clicked.connect(self.login)
        self.student_forgot.clicked.connect(self.forgot_password)
        self.conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '1234')

        self.show()

    def login(self):
        try:
            cur = self.conn.cursor() 
            number = self.student_number.text()
            password = self.student_password.text()                        
            
            qry = "SELECT student_number,password from students where student_number = {}::integer and password = {}::varchar ".format(number, password)
            
            cur.execute(qry)
            
            result = cur.fetchone()
            
            if result == None :
                self.labelResult_student.setText("Incorrect Student Number or Password") 
            else:
                self.labelResult_student.setText("You are logged in")
                self.cams = student.Student()
        except psycopg2.Error as e:
            print(e)
            self.labelResult_student.setText("Error")




    def forgot_password(self):
        self.cams = student_forget_password.StudentForgetPassword()
   

    def hash_password(self,password): #Hash a password for storing
        cur = self.conn.cursor()
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self,stored_password, provided_password):#Verify a stored password against one provided by user
        cur = self.conn.cursor()
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
    mainwindow=StudentLogin()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    # window = Ui_teacher_functions()
    widget.setFixedWidth(800)
    widget.setFixedHeight(800)
    widget.show()
    app.exec_()