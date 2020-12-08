''' Program to connect with database and delete the record of entered employee number. '''

from sqlTor import SqlTor
from utils import clear_screen
from q18_dbSearch import get_employee


def delete_employee(cursor):
    ''' Delete an employee '''

    emp = get_employee(cursor)

    if not emp:
        print('Employee does not exist.')
        return

    employee_deletion = f'DELETE FROM employees WHERE emp_id={emp[0]}'

    try:
        cursor.execute(employee_deletion)
    except Exception as err:
        print(err)
    else:
        print('Successfully deleted.')


if __name__ == "__main__":

    with SqlTor() as my_con:
        cursor = my_con.cursor()
        while True:
            clear_screen()
            print('DELETE EMPLOYEE')
            delete_employee(cursor)
            my_con.commit()
