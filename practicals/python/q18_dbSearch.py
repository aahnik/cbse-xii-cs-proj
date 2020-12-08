''' Program to connect with database and search employee number in table employee
and display record, if empno not found display appropriate message. '''

from utils import clear_screen
from sqlTor import SqlTor
from q17_dbRecord import input_emp_id


def get_employee(cursor) -> tuple or None:
    ''' Input employee id and fetch details of employee. 
    Returns a tuple or None if not found '''

    emp_id = input_emp_id()

    query = f'SELECT * FROM employees WHERE emp_id={emp_id}'

    try:
        cursor.execute(query)
    except Exception as err:
        print(err)
    else:
        employees = cursor.fetchall()
        if employees:
            return employees[0]


if __name__ == "__main__":

    with SqlTor() as my_con:
        cursor = my_con.cursor()

        while True:
            clear_screen()
            print('SEARCH EMPLOYEE')
            emp = get_employee(cursor)
            if emp:
                print('Record found 🥰')
                print(f'''
                        name: {emp[1]}, 
                        department: {emp[2]}, 
                        salary: {emp[3]}''')
            else:
                print('Employee Not found 😢')
