import base64
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import psycopg2
import teacher_forget_password, teacher, main

class TeacherLogin(QMainWindow):
    def __init__(self):
        super(TeacherLogin, self).__init__()
        uic.loadUi('ui/teacher_login.ui', self)
        self.teacher_login.clicked.connect(self.login)
        self.teacher_forgot.clicked.connect(self.forgot_password)
        self.conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '1234')
        self.teacher_login_back.clicked.connect(self.back)
        self.show()

    def login(self):
        try:
            cur = self.conn.cursor() 
            user_name_1 = self.username.text()
            password_1 = self.teacher_password.text()  
            encoded = password_1.encode("utf-8")
            password = base64.b16encode(encoded).decode("utf-8")                
            query = "SELECT user_name,password from teachers where user_name like '"+user_name_1 + "'and password like '" +password + "'"
            cur.execute(query)
            result = cur.fetchone() 
            if result == None:
                self.labelResult.setText("Incorrect UserName or Password") 
            else:
                self.labelResult.setText("You are logged in")
                print(type(result))
                self.cams = teacher.Teacher(result[0])
        except psycopg2.Error as e:
            self.labelResult.setText("Error")

    def forgot_password(self):
        self.cams = teacher_forget_password.TeacherForgetPassword()

    def back(self):
        self.cams = main.Main()
    