import psycopg2

conn = psycopg2.connect(
    host= 'localhost',
    database = 'school_management',
    user = 'postgres',
    password = '123')

cur = conn.cursor()

create_script = '''CREATE TABLE IF NOT EXISTS "public.Students" (
	"student_id" serial,
	"first_name" varchar(255),
	"last_name" varchar(255),
	"password" varchar(255) NOT NULL,
	"student_number" integer NOT NULL,
	CONSTRAINT "Students_pk" PRIMARY KEY ("student_id")
) WITH (
  OIDS=FALSE
);
CREATE TABLE IF NOT EXISTS "public.Teachers" (
	"teacher_id" serial,
	"student_id" integer,
	"user_name" VARCHAR(255),
	"password" varchar(255) NOT NULL,
	"first_name" varchar(255) NOT NULL,
	"last_name" varchar(255) NOT NULL,
	"teacher_email" varchar(255) NOT NULL,
	CONSTRAINT "Teachers_pk" PRIMARY KEY ("teacher_id")
) WITH (
  OIDS=FALSE
);
CREATE TABLE IF NOT EXISTS "public.Lessons" (
	"lesson_id" serial,
	"name" VARCHAR(255),
	CONSTRAINT "Lessons_pk" PRIMARY KEY ("lesson_id")
) WITH (
  OIDS=FALSE
);
CREATE TABLE IF NOT EXISTS  "public.StudentLessons" (
	"studentlessons_id" serial NOT NULL,
	"student_id" integer NOT NULL,
	"lesson_id" integer NOT NULL,
	CONSTRAINT "StudentLessons_pk" PRIMARY KEY ("studentlessons_id")
) WITH (
  OIDS=FALSE
);
CREATE TABLE IF NOT EXISTS "public.Marks" (
	"mark_id" integer NOT NULL,
	"student_id" integer NOT NULL,
	"lesson_id" integer NOT NULL,
	"date" TIMESTAMP NOT NULL,
	"marks" FLOAT NOT NULL,
	CONSTRAINT "Marks_pk" PRIMARY KEY ("mark_id")
) WITH (
  OIDS=FALSE
);
CREATE TABLE IF NOT EXISTS "public.Grades" (
	"grade_id" serial NOT NULL,
	"grade_name" VARCHAR(255),
	"student_id" integer NOT NULL,
	CONSTRAINT "Grades_pk" PRIMARY KEY ("grade_id")
) WITH (
  OIDS=FALSE
);
CREATE TABLE IF NOT EXISTS "public.Teachers_students" (
	"teacher_student_id" serial NOT NULL,
	"teacher_id" serial NOT NULL,
	"student_id" serial NOT NULL,
	CONSTRAINT "Teachers_students_pk" PRIMARY KEY ("teacher_student_id")
) WITH (
  OIDS=FALSE
);





'''

cur.execute(create_script)

insert_script = 'INSERT INTO Lessons ("lesson_id","name") VALUES (%s,%s)'
insert_Value = (1,"math")
cur.execute(insert_script,insert_Value)

conn.commit()

# conn.close()