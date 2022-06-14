from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import psycopg2
import main_login
import teacher_forget_password


class Teacher_New(QMainWindow):
    
    def __init__(self):
        super(Teacher_New, self).__init__()
        uic.loadUi('ui/teacher_login.ui', self)
        self.teacher_login_back.clicked.connect(self.back)
        self.teacher_forgot.clicked.connect(self.forgot_password)


    def back(self):
        self.cams = main_login.Main_Login()

    def forgot_password(self):
        self.cams = teacher_forget_password.TeacherForgetPassword()





if (__name__ == '__main__'):
    # Main App
    app=QApplication(sys.argv)
    mainwindow=Teacher_New()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    # window = Ui_teacher_functions()
    widget.setFixedWidth(800)
    widget.setFixedHeight(800)
    widget.show()
    app.exec_()