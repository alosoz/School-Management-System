import base64
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import psycopg2
import student_forget_password,student,main


class StudentLogin(QMainWindow):
    def __init__(self):
        super(StudentLogin, self).__init__()
        uic.loadUi('ui/student_login.ui', self)
        self.student_login.clicked.connect(self.login)
        self.student_forgot.clicked.connect(self.forgot_password)
        self.student_login_back.clicked.connect(self.back)
        self.conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '1234')

        self.show()

    def login(self):
        try:
            cur = self.conn.cursor() 
            number = self.student_number.text()
            password = self.student_password.text()   
            encoded = password.encode("utf-8")
            password = base64.b16encode(encoded).decode("utf-8")

            
            qry = "SELECT student_number,password from students where student_number = {}::integer and password = {}::varchar ".format(number, password)
            
            cur.execute(qry)
            
            result = cur.fetchone()
            
            if result == None :
                self.labelResult_student.setText("Incorrect Student Number or Password") 
            else:
                self.labelResult_student.setText("You are logged in")
                self.cams = student.Student(result[0])
        except psycopg2.Error as e:
            self.labelResult_student.setText("Error")

    def forgot_password(self):
        self.cams = student_forget_password.StudentForgetPassword()

    def back(self):
        self.cams = main.Main()
   