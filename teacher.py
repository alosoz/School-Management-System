from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import psycopg2



class Teacher(QMainWindow):

    def __init__(self):
        super(Teacher, self).__init__()
        uic.loadUi('ui/teacher_functions.ui', self)
        self.pushButton_lesson_add_newlesson_add.clicked.connect(self.add_lesson)
        self.pushButton_Lesson_add_StuToLesson_add.clicked.connect(self.add_student)
        self.pushButton_Lesson_Edit_edit.clicked.connect(self.edit)
        self.pushButton_lesson_remove_lesson_rem.clicked.connect(self.remove_lesson)
        self.pushButton_Lesson_remove_remstu_remove.clicked.connect(self.remove_student)
        self.pushButton_grades_add_add.clicked.connect(self.add_grade)
        self.pushButton_grades_edit_search.clicked.connect(self.search_grade)
        self.pushButton_grades_edit_edit.clicked.connect(self.edit_grade)
        self.pushButton_grades_remove_remove.clicked.connect(self.remove_grade)
        self.show()
    
    
    
    def add_lesson(self):
        conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '12345')
        cur = conn.cursor()
        lesson_name = self.lineEdit_lesson_add_newlesson.text()
        qry = "insert into lessons(name) values(%s)"
        value = (lesson_name)
        cur.execute(qry,value)
        conn.commit()
        # TypeError: not all arguments converted during string formatting


    def add_student(self):
        pass

    def edit(self):
        pass

    def remove_lesson(self):
        pass

    def remove_student(self):
        pass

    def add_grade(self):
        pass

    def search_grade(self):
        pass

    def edit_grade(self):
        pass

    def remove_grade(self):
        pass

# Main App
app=QApplication(sys.argv)
mainwindow=Teacher()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
# window = Ui_teacher_functions()
widget.setFixedWidth(800)
widget.setFixedHeight(800)
widget.show()
app.exec_()