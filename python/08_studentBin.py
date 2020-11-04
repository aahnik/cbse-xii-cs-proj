'''
Create a binary file with name and roll number. Search for a given roll
number and display the name, if not found display appropriate message.
'''
import pickle
import os
from utils import drive_menu

students = {}
filename = ''


def init(path):
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
    roll = input('Enter roll to search student: ')
    try:
        print(f'Student found : {students[roll]}')
    except KeyError:
        print('Student not found in records')


def main():

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
