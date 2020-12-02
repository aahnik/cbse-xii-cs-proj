from sqlTor import SqlTor
import mysql.connector
from mysql.connector import errorcode
from tabulate import tabulate
from utils import clear_screen


def create_table(cursor):
    table_creation = ("CREATE TABLE employees("
                      "emp_id integer NOT NULL PRIMARY KEY,"
                      "name char(20) NOT NULL,"
                      "department char(20) NOT NULL,"
                      "salary integer NOT NULL);")

    try:
        cursor.execute(table_creation)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('table already exists')
        else:
            print(err)
    else:
        print('Created table `employees` successfully')


def display_all(cursor):
    query = 'SELECT * FROM employees'

    try:
        cursor.execute(query)
    except Exception as err:
        print(err)
    else:
        employees = cursor.fetchall()
        if employees:
            print(f'''\n\nHere is the list of all employees
            \n{tabulate(employees,tablefmt='fancy_grid',headers=['emp_id','name','department','salary'])}\n''')
        else:
            print('No employees recorded yet')


def record_new(cursor):
    print('Enter the details to add new employee.\n')
    try:
        emp_id = int(input('employee id: '))
        name = input('name: ')
        department = input('department: ')
        salary = int(input('salary: '))
    except ValueError as err:
        print(err)
        print('emp_id and salary must be integers')
        return

    insert_employee = f"INSERT INTO employees VALUES({emp_id},'{name}','{department}',{salary})"
    try:
        cursor.execute(insert_employee)
    except Exception as err:
        if err.errno == errorcode.ER_DUP_ENTRY:
            print('Duplicate entry: emp_id must be unique')
            print('If you want to update the data run `q19_dbUpdate.py`')
    else:
        print('New employee added successfully 😃')


if __name__ == "__main__":

    with SqlTor() as my_con:
        cursor = my_con.cursor()
        create_table(cursor)
        while True:
            clear_screen()
            display_all(cursor)
            record_new(cursor)
            my_con.commit()
