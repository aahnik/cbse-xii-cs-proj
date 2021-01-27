''' Program to connect with database and update the employee record of entered empno. '''

from utils import clear_screen
from sqlTor import SqlTor

from q18_dbSearch import get_employee
from q17_dbRecord import input_employee_details


def update_employee(cursor):
    ''' Update an employee '''

    emp = get_employee(cursor)

    if not emp:
        print('Employee does not exist.')
        return

    print('Enter new details of employee.')
    name, department, salary = input_employee_details()

    employee_updation = f"UPDATE employees \
                        SET name='{name}',\
                            department='{department}',\
                            salary={salary} \
                        WHERE emp_id={emp[0]};"

    try:
        cursor.execute(employee_updation)
    except Exception as err:
        print(err)
    else:
        print('Update Successful!')


if __name__ == "__main__":
    with SqlTor() as my_con:
        cursor = my_con.cursor()
        while True:
            clear_screen()
            print('UPDATE EMPLOYEE')
            update_employee(cursor)
            my_con.commit()
