from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import psycopg2


class Main_Login(QMainWindow):
    
    def __init__(self):
        super(Main_Login, self).__init__()
        uic.loadUi('ui/main_login.ui', self)
        self.teacher.clicked.connect(self.teacher)
        self.student.clicked.connect(self.student)

    def teacher(self):
        pass

    def student(self):
        pass

        
    




if (__name__ == '__main__'):
    # Main App
    app=QApplication(sys.argv)
    mainwindow=Main_Login()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    # window = Ui_teacher_functions()
    widget.setFixedWidth(800)
    widget.setFixedHeight(800)
    widget.show()
    app.exec_()