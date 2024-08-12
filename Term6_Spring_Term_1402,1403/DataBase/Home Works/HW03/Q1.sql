CREATE DATABASE DB_HW3;
GO
USE DB_HW3;
GO
CREATE TABLE "Students" ( 
    "id" INT PRIMARY KEY, 
    "name" NVARCHAR(100), 
    "family" NVARCHAR(100), 
    "mobile" NVARCHAR(50), 
    "isGraduated" BIT, 
    "majorId" NVARCHAR(20), 
    "major_name" NCHAR(20), 
); 
GO
CREATE TABLE "Courses" 
( 
    "id"          integer not null constraint courses_pkey primary key,   
    "name"        Nvarchar(20), 
    "department" Nvarchar(20) 
); 
GO
INSERT INTO "Students" (id, name, family, mobile, "isGraduated", "majorId", major_name) VALUES (3779898, N' بزرگ', N'قدیمی', '10203040506', 1, '1', N'افزار نرم'); 
INSERT INTO "Students" (id, name, family, mobile, "isGraduated", "majorId", major_name) VALUES (3921478, N'دلدار', N'خجسته', null, 0, '1', N'افزار نرم'); 
INSERT INTO "Students" (id, name, family, mobile, "isGraduated", "majorId", major_name) VALUES (3981122, N' نادر', N'ابراهیمی', '09515253', 1, '2', N'مصنوعی هوش'); 
INSERT INTO "Students" (id, name, family, mobile, "isGraduated", "majorId", major_name) VALUES (4001234, N' محمدرضا', N'گلزار', '09223344556', 0, '1', N'افزار نرم'); 
INSERT INTO "Students" (id, name, family, mobile, "isGraduated", "majorId", major_name) VALUES (4004321, N' مجید', N'سمیعی', null, 0, '2', N'مصنوعی هوش'); 
INSERT INTO "Students" (id, name, family, mobile, "isGraduated", "majorId", major_name) VALUES (4012222, N'علی', N'صادقی', '09131234567', 0, '3', N'داده علم'); 
INSERT INTO "Students" (id, name, family, mobile, "isGraduated", "majorId", major_name) VALUES (4015555, N' عادل', N'پور فردوسی ', null, 0, '3', N'داده علم'); 
INSERT INTO "Students" (id, name, family, mobile, "isGraduated", "majorId", major_name) VALUES (4025678, N'مریم', N'میرزاخانی', null, 0, '1', N'افزار نرم'); 
INSERT INTO "Students" (id, name, family, mobile, "isGraduated", "majorId", major_name) VALUES (4015678, N'علی', N'وحیدی', null, 0, '1', N'افزار نرم');
GO
INSERT INTO "Courses" (id, name, department) VALUES (1, N'داده پایگاه', N'کامپیوتر مهندسی'); 
INSERT INTO "Courses" (id, name, department) VALUES (2, N'الگوریتم طراحی', N'کامپیوتر مهندسی'); 
INSERT INTO "Courses" (id, name, department) VALUES (3, N'گسسته', N'ریاضی'); 
INSERT INTO "Courses" (id, name, department) VALUES (4, N'اساسی قانون', N'معارف');
GO
CREATE TABLE StudentCourseRelations (
    id INT NOT NULL,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    year INT,
    grade FLOAT,
    PRIMARY KEY (id),
    FOREIGN KEY (student_id) REFERENCES Students(id),
	FOREIGN KEY (course_id) REFERENCES Courses(id)
);
GO
INSERT INTO "StudentCourseRelations" (id,student_id,course_id,year,grade) VALUES(5,4015555,1,1401,11)
INSERT INTO "StudentCourseRelations" (id,student_id,course_id,year,grade) VALUES(8,4015555,3,null,18.5)
INSERT INTO "StudentCourseRelations" (id,student_id,course_id,year,grade) VALUES(11,4025678,3,1403,20)
INSERT INTO "StudentCourseRelations" (id,student_id,course_id,year,grade) VALUES(4,4025678,3,1402,19)
INSERT INTO "StudentCourseRelations" (id,student_id,course_id,year,grade) VALUES(2,3779898,1,1380,13)
INSERT INTO "StudentCourseRelations" (id,student_id,course_id,year,grade) VALUES(1,4001234,1,1401,18)
INSERT INTO "StudentCourseRelations" (id,student_id,course_id,year,grade) VALUES(7,4015555,2,1400,16)
INSERT INTO "StudentCourseRelations" (id,student_id,course_id,year,grade) VALUES(9,4004321,1,1401,15)
INSERT INTO "StudentCourseRelations" (id,student_id,course_id,year,grade) VALUES(10,4001234,3,null,17)
INSERT INTO "StudentCourseRelations" (id,student_id,course_id,year,grade) VALUES(03,4004321,2,1403,null)
GO
---- Part 1.1 ----
SELECT * FROM StudentCourseRelations
---- Part 1.2 ----
SELECT name,family,id FROM Students
where id >= 3990000 and name != 'علی' and  name != 'محمد' and (mobile LIKE '09_________' OR mobile IS NULL)
---- Part 1.3 ----
SELECT name,family,id
FROM Students
WHERE (name != 'علی' and  name != 'محمد') OR (id >= 3990000) OR (mobile LIKE '09_________' OR mobile IS NULL)
---- Part 1.4 ----
SELECT student_id,course_id,
CASE 
	WHEN course_id = 1 THEN grade - 2
	WHEN course_id = 2 THEN 0
	WHEN course_id = 3 THEN grade*1.02
	ELSE grade
END AS grade
FROM StudentCourseRelations
---- Part 1.5 ----
SELECT Students.name,family,major_name,Courses.name,grade
FROM Students,Courses,StudentCourseRelations
WHERE student_id = Students.id and Courses.id = course_id and isGraduated = 0 and year > 1300 and grade IS NOT NULL
ORDER BY student_id asc