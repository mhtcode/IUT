---- Part 3.1 ----
SELECT COUNT(course_id) AS counted_course,student_id 
FROM StudentCourseRelations
WHERE grade > 14
GROUP BY student_id
---- Part 3.2 ----
SELECT COUNT(course_id) AS counted_course, student_id 
FROM StudentCourseRelations
WHERE grade IS NOT NULL
GROUP BY student_id
HAVING AVG(grade) > 14;

