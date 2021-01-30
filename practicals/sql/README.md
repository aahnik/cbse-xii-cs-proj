# SQL

*This directory contains the solutions to all the SQL questions.*

See the following:
1. [`create_db.sql`](create_db.sql) to create the tables as illustrated in question.
2. [`solutions.sql`](solutions.sql) containing the solutions to the 20 questions.

---------


> *[the full `emp` table](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/emp_table.png)*

#### i. To display the all information of Sales department.

```sql
SELECT
    *
FROM
    emp
WHERE
    department = 'Sales';
```

![image of output of question 01](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/01.png)


#### ii. To display all information about the employees whose name starts with 'K'.

```sql
SELECT
    *
FROM
    emp
WHERE
    name LIKE 'K%';

```

![image of output of question 02](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/02.png)

#### iii. To list the name of female employees who are in Finance department.

```sql
SELECT
    name
FROM
    emp
WHERE
    sex = 'F' AND department = 'Finance';
```

![image of output of question 03](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/03.png)

#### iv. To display name and sex of all the employees whose age is in the range of 40 to 50 in ascending order of their name.

```sql
SELECT
    name, sex
FROM
    emp
WHERE
    age BETWEEN 40 AND 50
ORDER BY name;
```

![image of output of question 04](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/04.png)

#### v. To count the number of female employees with age greater than 20 and who are in Accounts department.

```sql
SELECT
    COUNT(*) 'female emp older than 20 in accounts'
FROM
    emp
WHERE
    age > 20 AND department = 'Accounts';
```

![image of output of question 05](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/05.png)

-------

> *[the full `games` table](outputs/games_table.png)*
#### vi. To display the name of all Games with their GCodes.

```sql
SELECT
    gamename, gcode
FROM
    games;
```

![image of output of question 06](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/06.png)

#### vii. To display details of those games which are having PrizeMoney more than 7000.

```sql
SELECT
    *
FROM
    games
WHERE
    prizemoney > 7000;

```

![image of output of question 07](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/07.png)

#### viii. To display the content of the GAMES table in ascending order of ScheduleDate.


```sql
SELECT
    *
FROM
    games
ORDER BY scheduledate;
```

![image of output of question 08](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/08.png)

#### ix. To display sum of PrizeMoney for each of the Numberof participation groupings ( as shown in column number 2 or 4).

```sql
SELECT
    number, SUM(prizemoney)
FROM
    games
GROUP BY number;
```

![image of output of question 09](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/09.png)

#### x. To display the sum of prize money of all games.


```sql
SELECT
    SUM(prizemoney)
FROM
    games;

```

![image of output of question 10](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/10.png)



-------

> *[the full `loans` table](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/loans_table.png)*


#### xi. Display the sum of all Loan Amount whose Interest rate is greater than 10.


```sql
SELECT
    SUM(loan_amount)
FROM
    loans
WHERE
    int_rate > 10;
```

![image of output of question 11](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/11.png)

#### xii. Display the Maximum Interest from Loans table.


```sql
SELECT
    MAX(int_rate)
FROM
    loans;
```

![image of output of question 12](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/12.png)

#### xiii. Display the count of all loan holders whose name ends with ‘SHARMA’.


```sql
SELECT
    COUNT(cust_name)
FROM
    loans
WHERE
    cust_name LIKE '%SHARMA';
```

![image of output of question 13](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/13.png)

#### xiv. Display the count of all loan holders whose Interest is NULL.


```sql
SELECT
    COUNT(cust_name)
FROM
    loans
WHERE
    int_rate IS NULL;
```

![image of output of question 14](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/14.png)

#### xv. Display the Interest-wise details of Loan Account Holders.

```sql
SELECT
    *
FROM
    loans
ORDER BY interest;
```

![image of output of question 15](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/15.png)

#### xvi. Display the Interest-wise details of Loan Account Holders with at least 10 installments remaining

```sql
SELECT
    *
FROM
    loans
WHERE
    installments >= 10
ORDER BY interest;

```

![image of output of question 16](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/16.png)

#### xvii. Display the Interest-wise count of all loan holders whose Installment due is more than 5 in each group.


```sql
SELECT
	int_rate, COUNT(*)
FROM
	loans
GROUP BY
	int_rate
HAVING
	SUM(installments)>5;

```

![image of output of question 17](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/17.png)

#### xviii. Add one more column name ‘Address’ to the LOANS table.


```sql

ALTER TABLE loans
ADD (Adress TEXT);

```

![image of output of question 18](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/18.png)

#### xix. Reduce Interest rate by 1 of all loan holders whose Interest is not NULL.

```sql
UPDATE loans
SET
    int_rate = int_rate - 1
WHERE
    int_rate IS NOT NULL;
```

![image of output of question 19](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/19.png)

#### xx. Delete the record of customer whose account number is 105.

```sql
DELETE FROM loans
WHERE
    accno = 105;

```

![image of output of question 20](https://raw.githubusercontent.com/aahnik/cbse-xii-cs-proj/main/practicals/sql/outputs/20.png)
