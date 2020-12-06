USE sql_practical;

-- note: to execute an particular line 
-- in MySql workbench, 
-- select it and press the execute button


-- display table emp

SELECT * 
FROM emp;

-- i 
-- To display the all information of Sales department.

SELECT * 
FROM emp 
WHERE department='Sales';

-- ii
-- To display all information about the employees whose name starts with 'K'

SELECT *
FROM emp
WHERE name LIKE 'K%';

-- iii
-- To list the name of female employees who are in Finance department.

SELECT name
FROM emp
WHERE sex = 'F' AND department = 'Finance';

-- iv
-- To display name and sex of all the employees whose age is in the range of 40 to 50 in
-- ascending order of their name.

SELECT name,sex
FROM emp
WHERE age BETWEEN 40 AND 50
ORDER BY name;

-- v
-- To count the number of female employees with age greater than 20 and who are in
-- Accounts department.

SELECT COUNT(*) "female emp older than 20 in accounts"
FROM emp
WHERE age > 20 and department = 'Accounts';

-- display table games

SELECT *
FROM games;

-- vi
-- To display the name of all Games with their GCodes.

SELECT gamename,gcode
FROM games;

-- vii
-- To display details of those games which are having PrizeMoney more than 7000.

SELECT *
FROM games
WHERE prizemoney > 7000;

-- viii
-- To display the content of the GAMES table in ascending order of ScheduleDate.

SELECT *
FROM games
ORDER BY scheduledate;

-- ix
-- To display sum of PrizeMoney for each of the Numberof participation groupings ( as shown in
-- column number 2 or 4)

SELECT number,SUM(prizemoney)
FROM games
GROUP BY number;

-- x
-- To display the sum of prize money of all games.

SELECT SUM(prizemoney)
FROM games;


-- display table loans

SELECT *
FROM loans;


-- xi
-- Display the sum of all Loan Amount whose Interest rate is greater than 10.

SELECT SUM(loan_amount)
FROM loans
WHERE int_rate > 10;


-- xii
-- Display the Maximum Interest from Loans table.

SELECT MAX(int_rate)
FROM loans;

-- xiii
-- Display the count of all loan holders whose name ends with ‘SHARMA’.

SELECT COUNT(cust_name)
FROM loans
WHERE cust_name LIKE '%SHARMA';

-- xiv
-- Display the Interest-wise details of Loan Account Holders.

SELECT *
FROM loans
ORDER BY interest;


