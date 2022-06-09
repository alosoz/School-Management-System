CREATE TABLE "public.Students" (
	"student_id" serial,
	"first_name" varchar(255),
	"last_name" varchar(255),
	"password" varchar(255) NOT NULL,
	"student_number" integer NOT NULL,
	CONSTRAINT "Students_pk" PRIMARY KEY ("student_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Teachers" (
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



CREATE TABLE "public.Lessons" (
	"lesson_id" serial,
	"name" VARCHAR(255),
	CONSTRAINT "Lessons_pk" PRIMARY KEY ("lesson_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.StudentLessons" (
	"studentlessons_id" serial NOT NULL,
	"student_id" integer NOT NULL,
	"lesson_id" integer NOT NULL,
	CONSTRAINT "StudentLessons_pk" PRIMARY KEY ("studentlessons_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Marks" (
	"mark_id" integer NOT NULL,
	"student_id" integer NOT NULL,
	"lesson_id" integer NOT NULL,
	"date" TIMESTAMP NOT NULL,
	"marks" FLOAT NOT NULL,
	CONSTRAINT "Marks_pk" PRIMARY KEY ("mark_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Grades" (
	"grade_id" serial NOT NULL,
	"grade_name" serial(255) NOT NULL,
	"student_id" integer NOT NULL,
	CONSTRAINT "Grades_pk" PRIMARY KEY ("grade_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Teachers_students" (
	"teacher_student_id" serial NOT NULL,
	"teacher_id" serial NOT NULL,
	"student_id" serial NOT NULL,
	CONSTRAINT "Teachers_students_pk" PRIMARY KEY ("teacher_student_id")
) WITH (
  OIDS=FALSE
);






ALTER TABLE "StudentLessons" ADD CONSTRAINT "StudentLessons_fk0" FOREIGN KEY ("student_id") REFERENCES "Students"("student_id");
ALTER TABLE "StudentLessons" ADD CONSTRAINT "StudentLessons_fk1" FOREIGN KEY ("lesson_id") REFERENCES "Lessons"("lesson_id");

ALTER TABLE "Marks" ADD CONSTRAINT "Marks_fk0" FOREIGN KEY ("student_id") REFERENCES "Students"("student_id");
ALTER TABLE "Marks" ADD CONSTRAINT "Marks_fk1" FOREIGN KEY ("lesson_id") REFERENCES "Lessons"("lesson_id");

ALTER TABLE "Grades" ADD CONSTRAINT "Grades_fk0" FOREIGN KEY ("student_id") REFERENCES "Students"("student_id");

ALTER TABLE "Teachers_students" ADD CONSTRAINT "Teachers_students_fk0" FOREIGN KEY ("teacher_id") REFERENCES "Teachers"("teacher_id");
ALTER TABLE "Teachers_students" ADD CONSTRAINT "Teachers_students_fk1" FOREIGN KEY ("student_id") REFERENCES "Students"("student_id");








