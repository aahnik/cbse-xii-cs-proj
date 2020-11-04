'''
Write a menu driven program to perform read and write operations using a text file
called “student.txt” counting student roll_no, name and address.
'''

import os
from utils import clear_screen, drive_menu

filename = ''


def init(path: str):
    '''Creates an file `student.txt` in desired directory, if not exists

    # Parameters:
        - path:str directory path

    # Returns: None

    '''
    try:
        os.makedirs(path)
        print("directory created")
    except FileExistsError:
        print("directory exists")

    global filename
    filename = os.path.join(path, 'student.txt')

    if not os.path.isfile(filename):
        # create file if does not exist
        with open(filename, 'w+') as file:
            file.write('Roll,Name,Address')
            # writing the headers in first line ( line no = 0)
            print("file `student.txt` created")
            return

    print("file `student.txt` exists in desired directory")


def search_student(roll: int) -> list:
    '''Searches the roll no. in the text file.
    - If exists returns line no else -1

    # Parameters:
        - roll:int the roll number of student

    # Returns:
        - record:list the record list which looks like [roll,name,address]
                None if student's record is absent
    '''

    with open(filename, 'r') as file:
        content = file.read()

    lines = content.splitlines()

    def record(line): return line.split(',')

    for line in lines:
        if record(line)[0] == str(roll):
            return record(line)

    return None


def record_student():
    '''
    Records a new student in the text file.
    - Roll numbers must be unique.
    - If roll number already exists, returns False
    '''
    try:
        roll = int(input("Enter Student's roll number\n>>> "))
    except ValueError:
        print("Roll number must be an Integer")
        return
    name = input("Enter name\n>>> ")
    address = input("Enter address\n>>> ").replace('\n', ';')
    # new line in address is not allowed

    if roll <= 0:
        print('Invalid roll no')
        return
    if search_student(roll):
        print('Student already exists')
        return

    with open(filename, 'a') as file:
        file.write(f'\n{roll},{name},{address}')
        # multi line address is converted to single line
        print('Successfully Recorded')


def read_data() -> None:
    '''Displays the details of the student searhced
    '''
    roll = input("Enter roll no. to search\n>>> ")
    record = search_student(roll)
    if not record:
        print("Record not found")
    else:
        print(f'''
        Name : {record[1]}
        -------------------
        Roll no. : {record[0]}

        Address: {record[2]}
        ''')


def display_all():
    with open(filename, 'r') as file:
        print(file.read())


def main():

    path = input('Enter directory path to store/retrieve data\n>>> ')
    init(path)

    menus = {}
    menus['1'] = {'desc': 'Add new student',
                  'func': record_student}
    menus['2'] = {'desc': 'Display details of all students',
                  'func': display_all}
    menus['3'] = {'desc': 'Search student by roll no',
                  'func': read_data}
    drive_menu('Student Management Portal',menus)


if __name__ == "__main__":
    main()
