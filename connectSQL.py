import psycopg2

conn = psycopg2.connect(
    host= 'localhost',
    database = 'school_management',
    user = 'postgres',
    password = '123')

cur = conn.cursor()

create_script = '''CREATE TABLE IF NOT EXISTS Students (
	"student_id" serial,
	"first_name" varchar(255),
	"last_name" varchar(255),
	"password" varchar(255) NOT NULL,
	"student_number" integer NOT NULL,
	CONSTRAINT "Students_pk" PRIMARY KEY ("student_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS Teachers (
	"teacher_id" serial,
	"user_name" VARCHAR(255),
	"password" varchar(255) NOT NULL,
	"first_name" varchar(255) NOT NULL,
	"last_name" varchar(255) NOT NULL,
	"teacher_email" varchar(255) NOT NULL,
	CONSTRAINT "Teachers_pk" PRIMARY KEY ("teacher_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS Lessons (
	"lesson_id" serial,
	"name" VARCHAR(255),
	CONSTRAINT "Lessons_pk" PRIMARY KEY ("lesson_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS StudentLessons (
	"studentlessons_id" serial NOT NULL,
	"student_id" integer NOT NULL,
	"lesson_id" integer NOT NULL,
	CONSTRAINT "StudentLessons_pk" PRIMARY KEY ("studentlessons_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS Grades (
	"grade_id" integer NOT NULL,
	"student_id" integer NOT NULL,
	"lesson_id" integer NOT NULL,
	"grade" FLOAT NOT NULL,
	CONSTRAINT "Grades_pk" PRIMARY KEY ("grade_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE IF NOT EXISTS Teachers_lessons (
	"teacher_lesson_id" serial NOT NULL,
	"teacher_id" serial NOT NULL,
	"lesson_id" serial NOT NULL,
	CONSTRAINT "Teachers_lessons_pk" PRIMARY KEY ("teacher_lesson_id")
) WITH (
  OIDS=FALSE
);






ALTER TABLE StudentLessons ADD CONSTRAINT "StudentLessons_fk0" FOREIGN KEY ("student_id") REFERENCES Students("student_id");
ALTER TABLE StudentLessons ADD CONSTRAINT "StudentLessons_fk1" FOREIGN KEY ("lesson_id") REFERENCES Lessons("lesson_id");

ALTER TABLE Grades ADD CONSTRAINT "Grades_fk0" FOREIGN KEY ("student_id") REFERENCES Students("student_id");
ALTER TABLE Grades ADD CONSTRAINT "Grades_fk1" FOREIGN KEY ("lesson_id") REFERENCES Lessons("lesson_id");

ALTER TABLE Teachers_lessons ADD CONSTRAINT "Teachers_lessons_fk0" FOREIGN KEY ("teacher_id") REFERENCES Teachers("teacher_id");
ALTER TABLE Teachers_lessons ADD CONSTRAINT "Teachers_lessons_fk1" FOREIGN KEY ("lesson_id") REFERENCES Lessons("lesson_id");

'''

cur.execute(create_script)

insert_script = 'INSERT INTO Lessons ("lesson_id","name") VALUES (%s,%s)'
insert_Value = (2,"english")
cur.execute(insert_script,insert_Value)

conn.commit()

# conn.close()