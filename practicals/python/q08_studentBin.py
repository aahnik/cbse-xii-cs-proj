''' Create a binary file with name and roll number. Search for a given roll
number and display the name, if not found display appropriate message.
'''


import pickle
import os
from utils import drive_menu

students = {}
filename = ''


def init(path: str) -> None:
    ''' Load the file. If file does not exist, creates it.

    Args:
        path (str): file path
    '''

    global students
    if not os.path.isdir(path):
        os.makedirs(path)
    global filename
    filename = os.path.join(path, 'student.bin')
    if not os.path.isfile(filename):
        with open(filename, 'wb') as file:
            pickle.dump(students, file)
    else:
        with open(filename, 'rb') as file:
            students = pickle.load(file)


def record() -> None:
    ''' Record a new student.
    '''
    roll = input('Enter roll: ')
    name = input('Enter name: ')
    student = {roll: name}
    try:
        students.update(student)
        with open(filename, 'wb') as file:
            pickle.dump(students, file)
        print('Successfully recorded student')
    except Exception as e:
        print(f'Failed to record student due to error \n {e}')


def search() -> None:
    ''' Search for an existing student.
    '''
    roll = input('Enter roll to search student: ')
    try:
        print(f'Student found : {students[roll]}')
    except KeyError:
        print('Student not found in records')


def main():
    ''' Driving the app.
    '''

    path = input('Enter directory path to store/retrieve data\n >>> ')
    init(path)

    menus = {}

    menus['1'] = {'desc': 'Record new student',
                  'func': record}
    menus['2'] = {'desc': 'Search student by roll',
                  'func': search}

    drive_menu('Student Management', menus)


if __name__ == "__main__":
    main()
