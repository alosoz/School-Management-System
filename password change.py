import base64
import sys
import psycopg2

conn = psycopg2.connect(host= 'localhost',database = 'school_management',user = 'postgres',password = '1234')
cur = conn.cursor()
teacher = input("id : ")
print(type(teacher))
password1 = cur.execute("select password from teachers where teacher_id = %s", (teacher,))
new_password = cur.fetchone()[0]
print(new_password)
encoded = new_password.encode("utf-8")
password = base64.b16encode(encoded).decode("utf-8")
cur.execute("update teachers set password = %s where teacher_id = %s", (password,teacher))
conn.commit()