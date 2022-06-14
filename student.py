from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys
import psycopg2



class Student(QMainWindow):

    def __init__(self):
        super(Student, self).__init__()
        uic.loadUi('ui/student_functions.ui', self)
        self.tableWidget_lesson_teacher.setColumnWidth(0,205)
        self.tableWidget_lesson_teacher.setColumnWidth(1,250)
        self.tableWidget_lesson_grade.setColumnWidth(0,205)
        self.tableWidget_lesson_grade.setColumnWidth(1,250)
        self.pushButton_update_pass.clicked.connect(self.update_pass)
        self.show()
        self.show_lesson_grades()
        self.show_lesson_teachers()
         


    def update_pass(self):
        conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = 'Palmiye76')
        cur = conn.cursor()
        Current_Password = self.lineEdit_current_pass.text()
        New_Password = self.lineEdit_new_pass.text()
  
        cur.execute("update students set password = %s  where password = %s",(New_Password,Current_Password))
        conn.commit()

    def show_lesson_teachers(self):
        conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = 'Palmiye76')
        cur = conn.cursor()
        show_lesson_teacher_sqlquery = "SELECT first_name FROM teachers LIMIT 10"
        cur.execute(show_lesson_teacher_sqlquery)
        teacher = cur.fetchall()
        row = 0


        for i in teacher:
            self.tableWidget_lesson_teacher.setItem(row, 0, QtWidgets.QTableWidgetItem(i[0]))
            
            row = row+1
           

        conn.commit()


    def show_lesson_grades(self):
        conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = 'Palmiye76')
        cur = conn.cursor()
        
        show_lesson_grade_sqlquery = "SELECT name FROM lessons LIMIT 10"
        cur.execute(show_lesson_grade_sqlquery)
        grade = cur.fetchall()
        row = 0


        for i in grade:
            self.tableWidget_lesson_grade.setItem(row, 0, QtWidgets.QTableWidgetItem(i[0]))
            row = row+1

        
        conn.commit()


    def personal_info(self):
        conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = 'Palmiye76')
        cur = conn.cursor()
        cur.execute("select first_name,last_name, password, student_number from students where student_id = 1")
        Student = cur.fetchall()
        for r in Student:
            self.First_name_lineEdit.insert(r[0])
            self.LastName_lineEdit(r[1])
            self.lineEdit_Password_stu.insert(r[2])
            self.lineEdit_Stu_number.insert(r[3])




if (__name__ == '__main__'):
# Main App
    app = QApplication(sys.argv)
    mainwindow = Student()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(800)
    widget.setFixedHeight(800)
    widget.show()
    app.exec_()


















