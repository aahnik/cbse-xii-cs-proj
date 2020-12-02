from sqlTor import SqlTor
from utils import clear_screen


def delete_employee(cursor, emp_id=None):
    if not emp_id:
        emp_id = int(input('Enter the emp_id to delete: '))

    employee_deletion = f'DELETE FROM employees WHERE emp_id={emp_id}'

    try:
        cursor.execute(employee_deletion)
    except Exception as err:
        print(err)
    else:
        print('Successfully deleted')


with SqlTor() as my_con:
    cursor = my_con.cursor()
    while True:
        clear_screen()

        delete_employee(cursor)
        my_con.commit()
