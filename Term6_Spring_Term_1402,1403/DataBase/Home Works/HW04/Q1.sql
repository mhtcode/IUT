--- Q1 ---

--- Q1.A
--ALTER TABLE section
--ADD numa numeric; 

--SELECT *
--FROM section

--- Q1.B
--UPDATE section 
--SET numa = (
--	SELECT COUNT(*)
--	FROM takes
--	WHERE section.course_id = takes.course_id AND takes.grade like 'A_'
--) 

--SELECT TOP 10 course_id,sec_id,year,semester,numa
--FROM section
--ORDER BY section.numa DESC;

--- Q1.C
--CREATE OR ALTER TRIGGER Update_Numa
--ON takes
--AFTER UPDATE
--AS
--BEGIN
--UPDATE section 
--SET numa = (
--	SELECT COUNT(*)
--	FROM takes
--	WHERE section.course_id = takes.course_id AND takes.grade like 'A_'
--) 
--END;


--update takes
--set grade = 'A'
--where ID = 10527 and course_id = 362 and grade = 'C'

--select *
--from takes
--where  ID = 10527 and course_id = 362
--SELECT *
--FROM section
--WHERE course_id = 362


--- Q1.D
--SELECT TOP 10 course.course_id,
--    CASE
--	    WHEN numa <= PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY numa) OVER (PARTITION BY course.dept_name) THEN 2       
--		WHEN numa <= PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY numa) OVER (PARTITION BY course.dept_name) THEN 3
--        WHEN numa <= PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY numa) OVER (PARTITION BY course.dept_name) THEN 4

--        ELSE 1
--    END AS charak
--FROM course INNER JOIN section ON course.course_id = section.course_id
--ORDER BY course.course_id,charak DESC

--- Q2 ---
--CREATE OR REPLACE FUNCTION get_actor_count(actor_id_input INT)
--RETURNS TABLE (first_name VARCHAR, last_name VARCHAR, film_title VARCHAR, rental_count BIGINT)
--AS $$
--BEGIN
--    RETURN QUERY
--    SELECT
--        a.first_name,
--        a.last_name,
--        f.title AS film_title,
--        COUNT(r.rental_id) AS rental_count
--    FROM
--        actor a
--    INNER JOIN
--        film_actor fa ON a.actor_id = fa.actor_id
--    INNER JOIN
--        film f ON fa.film_id = f.film_id
--    LEFT JOIN
--        inventory i ON f.film_id = i.film_id
--    LEFT JOIN
--        rental r ON i.inventory_id = r.inventory_id
--    WHERE
--        a.actor_id = actor_id_input
--    GROUP BY
--        f.film_id, f.title, a.first_name, a.last_name;
--END; 
--$$ LANGUAGE plpgsql;

--SELECT *
--FROM get_actor_count(10);


--- Q3 ---
--CREATE TABLE IF NOT EXISTS my_table (
--    id_customer INT,
--    pay_avg DECIMAL,
--    profit NUMERIC(15, 2),
--    day_pay DOUBLE PRECISION
--);

--CREATE OR REPLACE PROCEDURE update_customer_payments (
--    IN customer_first_name VARCHAR,
--    IN customer_last_name VARCHAR
--)
--LANGUAGE plpgsql
--AS $$
--DECLARE
--    target_customer_id INT;
--    payment_record RECORD;
--BEGIN
--    SELECT customer_id INTO target_customer_id
--    FROM customer
--    WHERE first_name = customer_first_name AND last_name = customer_last_name
--    LIMIT 1;

--    IF target_customer_id IS NOT NULL THEN
--        FOR payment_record IN
--            SELECT amount, payment_date
--            FROM payment
--            WHERE customer_id = target_customer_id
--        LOOP

--            INSERT INTO my_table (id_customer, pay_avg, profit, day_pay)
--            VALUES (target_customer_id, 0, ROUND(payment_record.amount * 0.1, 2), EXTRACT(day FROM payment_record.payment_date));
--        END LOOP;


--        UPDATE my_table
--        SET pay_avg = (
--            SELECT AVG(amount)
--            FROM payment
--            WHERE customer_id = target_customer_id
--        )
--        WHERE id_customer = target_customer_id;
--    ELSE

--        RAISE NOTICE 'Customer % % not found', customer_first_name, customer_last_name;
--    END IF;
--END;
--$$;


--CALL update_customer_payments('Mary', 'Smith');


--SELECT * FROM my_table;


--- Q4 ---

--WITH FilmData AS (
--    SELECT
--        category.name AS category,
--        film.title AS name,
--        film.length,
--        LAG(film.length) OVER(PARTITION BY category.name ORDER BY film.length) AS previous_length,
--        LEAD(film.length) OVER(PARTITION BY category.name ORDER BY film.length DESC) AS next_length
--    FROM film
--    INNER JOIN film_category ON film.film_id = film_category.film_id  
--    INNER JOIN category ON category.category_id = film_category.category_id
--)
--SELECT
--    category,
--    name,
--    length,
--    length - previous_length AS pre_diff,
--    length - next_length AS post_diff
--FROM FilmData;

--- Q5 ---

--SELECT
--    Month,
--    Age_Rating as rating,
--    SUM(TotalPayment) as sum_amount,
--    LAG(TotalPayment) OVER (PARTITION BY Age_Rating ORDER BY Month) AS previous_month_sales,
--    LEAD(TotalPayment) OVER (PARTITION BY Age_Rating ORDER BY Month) AS next_month_sales
--FROM (
--    SELECT
--        EXTRACT(month FROM rental_date) AS Month,
--        rating AS Age_Rating,
--        SUM(amount) AS TotalPayment
--    FROM rental r
--    INNER JOIN payment p ON r.rental_id = p.rental_id
--    INNER JOIN inventory i ON r.inventory_id = i.inventory_id
--    INNER JOIN film f ON i.film_id = f.film_id
--    GROUP BY Month, Age_Rating
--) AS Subquery
--GROUP BY Month, Age_Rating, TotalPayment
--ORDER BY Month;

--- Q6 ---

--CREATE TABLE IF NOT EXISTS Y (
--    days INT,
--    weight DECIMAL(10, 2)
--);

--INSERT INTO Y (days, weight)
--VALUES
--    (1, 3.5), (2, 3.8), (3, 4.0), (4, 4.2), (5, 4.1),
--    (6, 4.3), (7, 4.4), (8, 4.6), (9, 4.7), (10, 4.9),
--    (11, 5.0), (12, 5.2), (13, 5.4), (14, 5.3), (15, 5.5),
--    (16, 5.6), (17, 5.8), (18, 6.0), (19, 6.1), (20, 6.3),
--    (21, 6.4), (22, 6.6), (23, 6.7), (24, 6.9), (25, 7.0),
--    (26, 7.2), (27, 7.3), (28, 7.5), (29, 7.6), (30, 7.8),
--    (31, 7.9), (32, 8.1), (33, 8.2), (34, 8.4), (35, 8.5),
--    (36, 8.7), (37, 8.8), (38, 9.0), (39, 9.1), (40, 9.3),
--    (41, 9.4), (42, 9.6), (43, 9.7), (44, 9.9), (45, 10.0),
--    (46, 10.2), (47, 10.3), (48, 10.5), (49, 10.6), (50, 10.8),
--    (51, 10.9), (52, 11.1), (53, 11.2), (54, 11.4), (55, 11.5),
--    (56, 11.7), (57, 11.8), (58, 12.0), (59, 12.1), (60, 12.3),
--    (61, 12.4), (62, 12.6), (63, 12.7), (64, 12.9), (65, 13.0),
--    (66, 13.2), (67, 13.3), (68, 13.5), (69, 13.6), (70, 13.8);

--WITH WeightChanges AS (
--    SELECT
--        days,
--        weight,
--        LAG(weight) OVER (ORDER BY days) AS previous_weight
--    FROM Y
--)
--SELECT
--    (days - 1) / 7 + 1 AS week,
--    MAX((weight - previous_weight) / previous_weight * 100) AS max_weight_increased
--FROM WeightChanges
--WHERE previous_weight IS NOT NULL
--GROUP BY (days - 1) / 7 + 1
--ORDER BY week;

--- Q7 ---

--CREATE TABLE IF NOT EXISTS customer_trn (
--    VoucherId VARCHAR(21) NULL, 
--    TrnDate DATE NULL,
--    TrnTime VARCHAR(6) NULL,
--    Amount BIGINT NULL, 
--    CustomerID INT NULL
--);

--INSERT INTO customer_trn (VoucherId, TrnDate, TrnTime, Amount, CustomerID)
--VALUES
--    ('V2001', '2024-06-01', '10:30', 5000, 101),
--    ('V2002', '2024-06-02', '15:45', 7500, 101),
--    ('V2003', '2024-06-03', '09:15', 12000, 101),
--    ('V2004', '2024-06-04', '14:20', 9000, 101),
--    ('V2005', '2024-06-05', '11:00', 6000, 101),
--    ('V2006', '2025-06-01', '10:30', 7000, 101),
--    ('V2007', '2023-06-01', '10:30', 4000, 101),
--    ('V2008', '2023-07-01', '12:30', 4500, 101),
--    ('V2009', '2023-08-01', '09:00', 3000, 102),
--    ('V2010', '2023-09-01', '14:00', 5200, 102),
--    ('V2011', '2024-01-01', '10:00', 4300, 102),
--    ('V2012', '2024-02-01', '13:30', 6100, 102),
--    ('V2013', '2024-03-01', '11:45', 7200, 102),
--    ('V2014', '2024-04-01', '15:15', 5300, 102),
--    ('V2015', '2024-05-01', '16:30', 8000, 102),
--    ('V2016', '2023-10-01', '08:30', 6200, 103),
--    ('V2017', '2023-11-01', '07:15', 4900, 103),
--    ('V2018', '2023-12-01', '12:45', 5700, 103),
--    ('V2019', '2024-06-06', '13:00', 6600, 103),
--    ('V2020', '2024-06-07', '10:45', 7800, 103),
--    ('V2021', '2024-06-08', '09:30', 3400, 103),
--    ('V2022', '2024-06-09', '14:15', 5900, 104),
--    ('V2023', '2024-06-10', '11:30', 6800, 104),
--    ('V2024', '2024-06-11', '15:00', 7900, 104),
--    ('V2025', '2024-06-12', '09:00', 8200, 104),
--    ('V2026', '2024-06-13', '12:00', 9100, 104),
--    ('V2027', '2024-06-14', '08:45', 7600, 104),
--    ('V2028', '2024-06-15', '10:15', 8500, 104),
--    ('V2029', '2024-06-16', '13:45', 9200, 104),
--    ('V2030', '2024-06-17', '11:15', 8300, 104);

--WITH CustomerCounts AS (
--    SELECT
--        CustomerID,
--        COUNT(*) AS TotalCount
--    FROM customer_trn
--    GROUP BY CustomerID
--)
--SELECT
--    c.CustomerID,
--    c.TotalCount AS Voucher_Count,
--    ROW_NUMBER() OVER (PARTITION BY ct.CustomerID ORDER BY ct.TrnDate, ct.TrnTime) AS Counter,
--    ct.VoucherID,
--    ct.TrnDate,
--    ct.TrnTime,
--    ct.Amount
--FROM customer_trn ct
--JOIN CustomerCounts c ON ct.CustomerID = c.CustomerID
--ORDER BY c.TotalCount DESC, ct.CustomerID, ct.TrnDate, ct.TrnTime;


--- Q8 ---

--CREATE TABLE IF NOT EXISTS NumberSequence (
--    id SERIAL PRIMARY KEY,
--    number INTEGER
--);

--INSERT INTO NumberSequence (number)
--VALUES 
--    (1), (1), (2), (3), (4), (3), (1), (1), (1), (5), (6), (7);

--SELECT number AS ConsecutiveNumbers
--FROM (
--    SELECT 
--        number,
--        LEAD(number, 1) OVER (ORDER BY id) AS next_number,
--        LEAD(number, 2) OVER (ORDER BY id) AS next_next_number
--    FROM NumberSequence
--) subquery
--WHERE number = next_number AND number = next_next_number;

--- Q9 ---
--CREATE TABLE LastCallTable(
--    LastRunDate DATE,
--	UntilRowDate DATE
--)
--GO

--CREATE TABLE Transactions (
--    Dpst_num INT,
--    Trsn_time DATETIME,
--    Dpst_trnover INT,
--);
--GO

--CREATE TABLE dpst_trn_bal (
--    Dpst_num INT,
--    Trsn_time DATETIME,
--    Dpst_trnover INT,
--	balance INT
--);
--GO

--INSERT INTO Transactions (Dpst_num, Trsn_time, Dpst_trnover) 
--VALUES 
--    (1022, '2018-06-15 14:13:00', 75),
--    (1022, '2018-06-15 14:28:00', -25),
--    (1022, '2018-06-17 14:58:00', 25),
--    (1067, '2019-07-18 23:32:00', 300),
--    (1022, '2018-06-16 12:00:00', 150),
--    (1022, '2018-06-18 08:45:00', -75),
--    (1022, '2018-06-19 16:30:00', 80),
--    (1067, '2019-07-19 10:15:00', 200),
--    (1067, '2019-07-20 14:20:00', -120),
--    (1067, '2019-07-21 09:00:00', 180);
--GO

--CREATE PROCEDURE UpdateBalancesTransactions
--	@inputDate DATE
--AS
--BEGIN
--    DECLARE @LastUpdateDate DATE, @LastRun DATE

--    SELECT @LastUpdateDate = MAX(LastRunDate) FROM LastCallTable
--	SELECT @LastRun = MAX(UntilRowDate) FROM LastCallTable

--	IF @LastRun IS NULL
--        SELECT @LastRun = CAST(DATEADD(DAY, -1,MIN(Trsn_time)) AS DATE) FROM Transactions

--    IF (@LastUpdateDate >= CAST(GETDATE() AS DATE) AND @LastUpdateDate IS NOT NULL)
--		BEGIN
--			RAISERROR('you have already executed today',16,1)
--			RETURN;
--		END

--	IF (@inputDate <= @LastRun)
--		BEGIN
--			RAISERROR('this date has been already calculated/not available',16,1)
--			RETURN;
--		END

--	IF (DATEADD(DAY,1,@LastRun) != @inputDate)
--		BEGIN
--			SET @inputDate = (SELECT TOP 1 Trsn_time FROM Transactions WHERE Trsn_time > @LastRun ORDER BY Trsn_time ASC)
--		END;

--    WITH RankedTransactions AS (
--        SELECT 
--            Dpst_num, 
--            Trsn_time, 
--            Dpst_trnover,
--            SUM(Dpst_trnover) OVER (PARTITION BY Dpst_num ORDER BY Trsn_time ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS balance
--        FROM Transactions
--        WHERE CAST(Trsn_time AS DATE) = @inputDate
--    )
--    INSERT INTO dpst_trn_bal (Dpst_num, Trsn_time, Dpst_trnover, balance)
--    SELECT Dpst_num, Trsn_time, Dpst_trnover, balance FROM RankedTransactions

--    SET @LastRun = @inputDate
    
--	INSERT INTO LastCallTable(LastRunDate, UntilRowDate)
--	VALUES 
--		(CAST(GETDATE() AS DATE),@LastRun);

--END
--GO

--EXEC UpdateBalancesTransactions @inputDate = "2018-06-15";


--SELECT *
--from dpst_trn_bal

--select *
--from Transactions

--select *
--from LastCallTable

--- Q10 ---
-- Create the VisitorRecords table
--CREATE TABLE IF NOT EXISTS VisitorRecords (
--    Id INT,
--    Visit_Date DATE,
--    Visitors INT
--);

--INSERT INTO VisitorRecords (Id, Visit_Date, Visitors) VALUES
--(1, '2017-01-01', 30),
--(2, '2017-01-02', 120),
--(3, '2017-01-03', 180),
--(4, '2017-01-04', 85),
--(5, '2017-01-05', 160),
--(6, '2017-01-06', 1700),
--(7, '2017-01-07', 210),
--(8, '2017-01-09', 175),
--(9, '2017-01-10', 220),
--(10, '2017-01-11', 300),
--(11, '2017-01-12', 110),
--(12, '2017-01-13', 250),
--(13, '2017-01-14', 180),
--(14, '2017-01-15', 150),
--(15, '2017-01-16', 400);
--WITH RankedVisits AS (
--    SELECT
--        Id,
--        Visit_Date,
--        Visitors,
--        LEAD(Id, 1) OVER (ORDER BY Id) AS NextID,
--        LEAD(Id, 2) OVER (ORDER BY Id) AS NextNextID,
--        LAG(Id, 1) OVER (ORDER BY Id) AS PrevID,
--        LAG(Id, 2) OVER (ORDER BY Id) AS PrevPrevID
--    FROM VisitorRecords
--    WHERE Visitors >= 100
--)
--SELECT DISTINCT
--    rv.Id,
--    rv.Visit_Date,
--    rv.Visitors
--FROM RankedVisits rv
--WHERE 
--    (rv.NextID = rv.Id + 1 AND rv.NextNextID = rv.Id + 2) OR
--    (rv.NextID = rv.Id + 1 AND rv.PrevID = rv.Id - 1) OR
--    (rv.PrevID = rv.Id - 1 AND rv.PrevPrevID = rv.Id - 2);



