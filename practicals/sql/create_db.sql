-- this is a script to create the tables given in question  

DROP DATABASE IF EXISTS sql_practical;
CREATE DATABASE sql_practical;
USE sql_practical;


DROP TABLE IF EXISTS emp;
CREATE TABLE emp(
   Id         INTEGER  NOT NULL PRIMARY KEY 
  ,Name       VARCHAR(20) NOT NULL
  ,Age        INTEGER  NOT NULL
  ,Department VARCHAR(10) NOT NULL
  ,Sal        INTEGER  NOT NULL
  ,Sex        CHAR(1) NOT NULL
);
INSERT INTO emp(Id,Name,Age,Department,Sal,Sex) VALUES
 (1,'Arprit',62,'Sales',38000,'M')
,(2,'Zarina',22,'Accounts',29000,'F')
,(3,'Kareem',32,'Sales',17000,'M')
,(4,'Arun',42,'Manager',80000,'M')
,(5,'Zubin',30,'Accounts',35000,'M')
,(6,'Kettaki',26,'Finance',60000,'F')
,(7,'Ankita',29,'Finance',65000,'F')
,(8,'Zareen',45,'Sales',28000,'F')
,(9,'Kush',29,'Accounts',32000,'M')
,(10,'Shilpa',23,'Sales',22000,'F');


DROP TABLE IF EXISTS games;
CREATE TABLE games(
   GCode        INTEGER  NOT NULL PRIMARY KEY 
  ,GameName     VARCHAR(12) NOT NULL
  ,Number       INTEGER  NOT NULL
  ,PrizeMoney   INTEGER  NOT NULL
  ,ScheduleDate VARCHAR(11) NOT NULL
);
INSERT INTO games(GCode,GameName,Number,PrizeMoney,ScheduleDate) VALUES
 (101,'Carom Board',2,5000,'23-Jan-2021')
,(102,'Badminton',2,1200,'12-Dec-2020')
,(103,'Table Tennis',4,8000,'14-Feb-2021')
,(105,'Chess',2,9000,'02-Jan-2021')
,(108,'Lawn Tennis',4,25000,'19-Mar-2021');


DROP TABLE IF EXISTS player;
CREATE TABLE player(
   PCode INTEGER  NOT NULL PRIMARY KEY 
  ,Name  VARCHAR(12) NOT NULL
  ,GCode INTEGER  NOT NULL
);
INSERT INTO player(PCode,Name,GCode) VALUES
 (1,'Jiten Singh',101)
,(2,'Ravi Dev',108)
,(3,'Tiyasha Basu',101)
,(4,'Sonam Kapoor',10);


DROP TABLE IF EXISTS loans;
CREATE TABLE loans(
   AccNo        INTEGER  NOT NULL PRIMARY KEY 
  ,Cust_Name    VARCHAR(10) NOT NULL
  ,Loan_Amount  INTEGER  NOT NULL
  ,Installments INTEGER  NOT NULL
  ,Int_Rate     NUMERIC(5,2)
  ,Start_Date   VARCHAR(10) NOT NULL
  ,Interest     INTEGER  NOT NULL
);
INSERT INTO loans(AccNo,Cust_Name,Loan_Amount,Installments,Int_Rate,Start_Date,Interest) VALUES
 (101,'R.K.GUPTA',300000,36,12.00,'19-07-2019',1200)
,(102,'S.P.SHARMA',500000,48,10.00,'22-03-2018',1800)
,(103,'K.P.JAIN',300000,36,NULL,'08-03-2017',1600)
,(104,'M.P.YADAV',800000,60,10.00,'06-12-2018',2250)
,(105,'S.P.SINHA',200000,36,12.50,'03-01-2020',4500)
,(106,'P.SHARMA',700000,60,12.50,'05-06-2018',3500)
,(107,'K.S.DHALL',500000,48,NULL,'05-03-2018',3800);


-- automatically generated script from https://www.convertcsv.com/csv-to-sql.htm 