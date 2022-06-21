import base64
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import psycopg2

class StudentForgetPassword(QMainWindow):
    
    def __init__(self):
        super(StudentForgetPassword, self).__init__()
        uic.loadUi('ui/student_forgot.ui', self)
        self.conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '1234')
        self.pushButton_Lesson_Edit_edit_2.clicked.connect(self.search)
        self.show()

    def search(self):
        cur = self.conn.cursor()
        first_name = self.lineEdit_first_name_student.text()
        last_name = self.lineEdit_lastname_student.text()
        student_number = self.lineEdit_student_number.text()
        cur.execute("select first_name from students where first_name = %s", (first_name,))
        name = cur.fetchone()[0]              
        cur.execute("select last_name from students where last_name = %s", (last_name,))
        surname = cur.fetchone()[0]
        cur.execute("select student_number from students  where student_number = %s" , (student_number,))
        number = cur.fetchone()[0]
        cur.execute("select password from students  where first_name = %s and last_name = %s and student_number = %s",(name,surname,number))
        password = cur.fetchone()[0]
        password1 = base64.b16decode(password.encode("utf-8")).decode("utf-8")
        self.lineEdit_password_student.insert(password1)


        
