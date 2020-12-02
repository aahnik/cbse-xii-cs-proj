-- this is a script to create the tables given in question  

CREATE DATABASE IF NOT EXISTS sql_practical;

USE sql_practical;

DROP TABLE IF EXISTS emp;
CREATE TABLE emp (
	id INTEGER,
    name CHAR(20),
    age INTEGER,
    department CHAR(20),
    sal INTEGER,
    sex CHAR(1)
    );
    
INSERT INTO emp VALUES(
1,'Arprit',62,'Sales',38000,'M'
2,'Zarina',22,'Accounts',29000,'F'
3,'Kareem',32,'Sales',17000,'M'
4,'Arun',42,'Manager',80000,'M'
5,'Zubin',30,'Accounts',35000,'M'
6,'Kettaki',26,'Finance',60000,'F'
7,'Ankita',29,'Finance',65000,'F'
8,'Zareen',45,'Sales',28000,'F'
9,'Kush',29,'Accounts',32000,'M'
10,'Shilpa',23,'Sales',22000,'F'

)
    

