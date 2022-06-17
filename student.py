from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import psycopg2




class Student(QMainWindow):

    def __init__(self,number):
        super(Student, self).__init__()
        uic.loadUi('ui/student_functions.ui', self)
        self.tableWidget_lesson_teacher.setColumnWidth(0,205)
        self.tableWidget_lesson_teacher.setColumnWidth(1,250)
        self.tableWidget_lesson_grade.setColumnWidth(0,205)
        self.tableWidget_lesson_grade.setColumnWidth(1,250)
        self.pushButton_update_pass.clicked.connect(self.update_pass)
        self.conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '1234')
        self.number = int(number)
        self.show()
        self.show_lessons()
        self.personal_info()
        self.show_grades()
        self.show_lesson_teachers()
         


    def update_pass(self):
        cur = self.conn.cursor()
        Current_Password = self.lineEdit_current_pass.text()
        New_Password = self.lineEdit_new_pass.text()
  
        cur.execute("update students set password = %s  where password = %s",(New_Password,Current_Password))
        self.conn.commit()

    def show_lesson_teachers(self):
        cur = self.conn.cursor()
        show_lesson_teacher_sqlquery = """select lessons.name,teachers.first_name || ' ' || last_name from ((teachers_lessons
                                          inner join teachers on teachers.teacher_id = teachers_lessons.teacher_id)
                                          inner join lessons on teachers_lessons.lesson_id = lessons.lesson_id );"""   
        cur.execute(show_lesson_teacher_sqlquery)
        teacher = cur.fetchall()
        row1 = 0

        for i in teacher:
            self.tableWidget_lesson_teacher.setItem(row1, 0, QtWidgets.QTableWidgetItem(i[0]))
            
            row1 = row1+1

        row2 = 0    
        for i in teacher:
            self.tableWidget_lesson_teacher.setItem(row2, 1, QtWidgets.QTableWidgetItem(i[1]))
            
            row2 = row2+1   
        self.conn.commit()


    def show_lessons(self):
        cur = self.conn.cursor()      
        show_lesson_grade_sqlquery = """select lessons.name from lessons
                                        inner join grades on lessons.lesson_id = grades.lesson_id"""  
        cur.execute(show_lesson_grade_sqlquery)
        lesson = cur.fetchall()
 
        row3 = 0

        for i in lesson:
            self.tableWidget_lesson_grade.setItem(row3, 0, QtWidgets.QTableWidgetItem(i[0]))
            row3 = row3+1
        self.conn.commit()

    def show_grades(self):
        cur = self.conn.cursor()      
        show_lesson_grade_sqlquery = """select grades.grade from lessons
                                        inner join grades on lessons.lesson_id = grades.lesson_id"""  
        cur.execute(show_lesson_grade_sqlquery)
        grade = cur.fetchall()
        strr = ([str(t[0]) for t in grade])
    
        row4 = 0    
        for i in strr:
            self.tableWidget_lesson_grade.setItem(row4, 1, QtWidgets.QTableWidgetItem(i[0]))
            
            row4 = row4+1   
        
        self.conn.commit()
        
        



    def personal_info(self):
        cur = self.conn.cursor()
        print(self.number)
        cur.execute("select first_name,last_name, password, student_number from students where student_number = %s",(self.number,))
        Student = cur.fetchall()
        for r in Student:
            self.First_name_lineEdit.insert(r[0])
            self.LastName_lineEdit.insert(r[1])
            self.lineEdit_Password_stu.insert(r[2])
            self.lineEdit_Stu_number.insert(str(r[3]))

        self.conn.commit()


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

