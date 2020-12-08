''' Program to create CSV file and store empno,name,salary and search any empno and
display name,salary and if not found appropriate message.
'''

import os
import csv
from utils import drive_menu

filename = os.path.join('data', 'employee.csv')


def init():
    ''' Create files if not present '''
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            file.write('empno,name,salary')


def store() -> None:
    ''' Store the record of employee '''
    record = input('Enter empno, name and salary seperated by comma\n>>> ')
    with open(filename, 'a') as file:
        file.write(f'\n{record}')
    print('Employee recorded')


def retrieve() -> None:
    ''' Retrieve the record of existing employee '''
    empno = input('Enter empno to search\n>>> ')
    with open(filename, 'r') as file:
        employees = csv.DictReader(file)
        for row in employees:
            if row['empno'] == empno:
                print(f"Name: {row['name']}\nSalary: {row['salary']}")
                return
        print('Employee not found in records')


def main():
    init()
    menus = {}
    menus['1'] = {'desc': 'Store new Employee', 'func': store}
    menus['2'] = {'desc': 'Search Employee', 'func': retrieve}
    drive_menu('Employee Management', menus)


if __name__ == "__main__":
    main()
