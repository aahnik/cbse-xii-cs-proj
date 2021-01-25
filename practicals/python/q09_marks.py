''' Create a binary file with roll number, name and marks. Input a roll
number and update the marks.
'''


import pickle
from utils import drive_menu
from tabulate import tabulate
import os

# in data folder of current directory
filename = os.path.join('data', 'marks.bin')

students = {}  # dictionary containing students


def load_file() -> None:
    with open(filename, 'rb') as file:
        global students
        students = pickle.load(file)


def write_to_file() -> None:
    with open(filename, 'wb') as file:
        pickle.dump(students, file)


def record_student() -> None:
    global students
    roll, name, marks = input(
        'Enter roll, name and marks seperated by comma\n> ').split(',')
    students[roll] = [name, marks]
    write_to_file()
    print('Sucessfully recorded')


def update_marks() -> None:
    roll, marks = input(
        'Enter roll, and new marks seperated by comma\n ').split(',')
    if roll in students.keys():
        students[roll][1] = marks
        write_to_file()
        print('Sucessfully updated')
    else:
        print('Student does not exist in records')


def display() -> None:
    table = []
    for key, value in students.items():
        table.append([key, value[0], value[1]])
    print(tabulate(table, tablefmt='fancy_grid',
                   headers=['Roll', 'Name', 'Marks']))


def main():
    ''' Driving the app.
    '''
    if not os.path.isfile(filename):
        write_to_file()
    else:
        load_file()

    menus = {}

    menus['1'] = {'desc': 'Record new student',
                  'func': record_student}
    menus['2'] = {'desc': 'Update marks of existing student',
                  'func': update_marks}
    menus['3'] = {'desc': 'Display all records',
                  'func': display}

    drive_menu('Marks Manager', menus)


if __name__ == "__main__":
    main()
