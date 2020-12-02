from utils import clear_screen
from sqlTor import SqlTor


def search_employee(cursor, emp_id=None):

    if not emp_id:
        try:
            emp_id = int(input('Enter the emp_id: '))
        except ValueError:
            print('emp_id must be integer')
            return

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
            print('Search Employee')
            emp = search_employee(cursor)
            if emp:
                print('Record found 🥰')
                print(f'''
                        name: {emp[1]}, 
                        department: {emp[2]}, 
                        salary: {emp[3]}''')
            else:
                print('Employee Not found 😢')
