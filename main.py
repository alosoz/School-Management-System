from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import psycopg2
import teacherLogin
import studentLogin

class Main(QMainWindow):
    
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('ui/main_login.ui', self)
        self.teacher_main.clicked.connect(self.teacher)
        self.student_main.clicked.connect(self.student)
        self.show()
    
    def teacher(self):
        self.cams = teacherLogin.TeacherLogin()


    def student(self):
        self.cams = studentLogin.StudentLogin()

    







if (__name__ == '__main__'):
    # Main App
    app=QApplication(sys.argv)
    mainwindow=Main()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(800)
    widget.setFixedHeight(800)
    widget.show()
    app.exec_()
