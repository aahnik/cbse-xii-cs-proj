'''
Program to connect with database and store record of employee and display records.

Sqlite3 is serverless. And comes pre-installed with python. So its preferred over MySQL or Postgress
'''


import sqlite3

con = sqlite3.connect('data/sqlDatabase.db')

cursor = con.cursor()

cursor.execute('''CREATE TABLE employees
                (id int, 
                name text, 
                age int, 
                department text, 
                gender text, 
                PRIMARY KEY (ID));
                ''')
