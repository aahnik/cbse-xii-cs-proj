USE sql_practical;

-- note: to execute an particular line 
-- in MySql workbench, 
-- select it and press the execute button


SELECT 
    *
FROM
    emp;

-- i 
-- To display the all information of Sales department.

SELECT 
    *
FROM
    emp
WHERE
    department = 'Sales';

-- ii
-- To display all information about the employees whose name starts with 'K'

SELECT 
    *
FROM
    emp
WHERE
    name LIKE 'K%';

-- iii
-- To list the name of female employees who are in Finance department.

SELECT 
    name
FROM
    emp
WHERE
    sex = 'F' AND department = 'Finance';

-- iv
-- To display name and sex of all the employees whose age is in the range of 40 to 50 in
-- ascending order of their name.

SELECT 
    name, sex
FROM
    emp
WHERE
    age BETWEEN 40 AND 50
ORDER BY name;

-- v
-- To count the number of female employees with age greater than 20 and who are in
-- Accounts department.

SELECT 
    COUNT(*) 'female emp older than 20 in accounts'
FROM
    emp
WHERE
    age > 20 AND department = 'Accounts';

-- display table games

SELECT 
    *
FROM
    games;

-- vi
-- To display the name of all Games with their GCodes.

SELECT 
    gamename, gcode
FROM
    games;

-- vii
-- To display details of those games which are having PrizeMoney more than 7000.

SELECT 
    *
FROM
    games
WHERE
    prizemoney > 7000;

-- viii
-- To display the content of the GAMES table in ascending order of ScheduleDate.

SELECT 
    *
FROM
    games
ORDER BY scheduledate;

-- ix
-- To display sum of PrizeMoney for each of the Numberof participation groupings ( as shown in
-- column number 2 or 4)

SELECT 
    number, SUM(prizemoney)
FROM
    games
GROUP BY number;

-- x
-- To display the sum of prize money of all games.

SELECT 
    SUM(prizemoney)
FROM
    games;


-- display table loans

SELECT 
    *
FROM
    loans;


-- xi
-- Display the sum of all Loan Amount whose Interest rate is greater than 10.

SELECT 
    SUM(loan_amount)
FROM
    loans
WHERE
    int_rate > 10;


-- xii
-- Display the Maximum Interest from Loans table.

SELECT 
    MAX(int_rate)
FROM
    loans;

-- xiii
-- Display the count of all loan holders whose name ends with ‘SHARMA’.

SELECT 
    COUNT(cust_name)
FROM
    loans
WHERE
    cust_name LIKE '%SHARMA';


-- xiv
-- Display the count of all loan holders whose Interest is NULL.

SELECT 
    COUNT(cust_name)
FROM
    loans
WHERE
    int_rate IS NULL;


-- xv
-- Display the Interest-wise details of Loan Account Holders.

SELECT 
    *
FROM
    loans
ORDER BY interest;

-- xvi
-- Display the Interest-wise details of Loan Account Holders with at least 10 installments
-- remaining.

SELECT 
    *
FROM
    loans
WHERE
    installments >= 10
ORDER BY interest;

-- xvii
-- Display the Interest-wise count of all loan holders whose Installment due is more than
-- 5 in each group.

SELECT 
	int_rate, COUNT(*)
FROM 
	loans
GROUP BY 
	int_rate
HAVING
	SUM(installments)>5;

-- xviii
-- Add one more column name ‘Address’ to the LOANS table.

ALTER TABLE loans
ADD (Adress TEXT);

-- xix
-- Reduce Interest rate by 1 of all loan holders whose Interest is not NULL.

UPDATE loans 
SET 
    int_rate = int_rate - 1
WHERE
    int_rate IS NOT NULL;
    
-- xx
-- Delete the record of customer whose account number is 105.

DELETE FROM loans 
WHERE
    accno = 105;



