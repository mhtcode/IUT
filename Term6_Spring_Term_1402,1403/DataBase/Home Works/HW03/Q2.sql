---- Part 2.1 ----
SELECT MIN(grade) AS minimum_grade ,course_id
FROM StudentCourseRelations
WHERE course_id = 1 or course_id = 3
GROUP BY course_id
---- Part 2.2 ----
SELECT *
FROM(
	SELECT DISTINCT TOP 2 grade
	FROM StudentCourseRelations
	WHERE grade is not null
	ORDER BY grade ASC 
	) as sbq
ORDER BY grade DESC
---- Part 2.3 ----
SELECT course_id,MIN(grade) AS minimum_grade
FROM StudentCourseRelations
WHERE grade is not null
GROUP BY course_id
ORDER BY minimum_grade ASC
---- Part 2.4 ----
SELECT SUM(grade) as sum_grade,student_id
FROM StudentCourseRelations
GROUP BY student_id
HAVING COUNT(student_id) > 1
---- Part 2.5 ----
SELECT MAX(grade) as maximum_grade,course_id
FROM StudentCourseRelations
WHERE grade > 5 and student_id is not null
GROUP BY course_id
---- Part 2.6 ----
SELECT student_id,course_id
FROM StudentCourseRelations
GROUP BY student_id,course_id
HAVING COUNT(student_id) > 1
---- Part 2.7 ----
(((SELECT course_id FROM StudentCourseRelations WHERE year = 1400 ) INTERSECT (SELECT course_id FROM StudentCourseRelations WHERE year = 1401)) 
EXCEPT
((SELECT course_id FROM StudentCourseRelations WHERE year = 1403 ) UNION (SELECT course_id FROM StudentCourseRelations WHERE year = 1402)))