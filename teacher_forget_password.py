import base64
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import psycopg2

class TeacherForgetPassword(QMainWindow):
    
    def __init__(self):
        super(TeacherForgetPassword, self).__init__()
        uic.loadUi('ui/teacher_forgot.ui', self)
        self.conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '1234')
        self.pushButton_Lesson_Edit_edit.clicked.connect(self.search)
        self.show()

    def search(self):
        cur = self.conn.cursor()
        first_name = self.lineEdit_first_name_teacher.text()
        last_name = self.lineEdit_lastname_teacher.text()
        username = self.lineEdit_username_teacher.text()
        cur.execute("select first_name from teachers where first_name = %s", (first_name,))
        name = cur.fetchone()[0]              
        cur.execute("select last_name from teachers where last_name = %s", (last_name,))
        surname = cur.fetchone()[0]
        cur.execute("select user_name from teachers  where user_name = %s" , (username,))
        user = cur.fetchone()[0]
        cur.execute("select password from teachers  where first_name = %s and last_name = %s and user_name = %s",(name,surname,user))
        password = cur.fetchone()[0]
        password1 = base64.b16decode(password.encode("utf-8")).decode("utf-8")
        self.lineEdit_username_teacher_2.insert(password1)

if (__name__ == '__main__'):
    app=QApplication(sys.argv)
    mainwindow=TeacherForgetPassword()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(800)
    widget.setFixedHeight(800)
    widget.show()
    app.exec_()
