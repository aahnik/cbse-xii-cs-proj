from sqlTor import SqlTor

from q18_dbSearch import search_employee


with SqlTor() as my_con:
    cursor = my_con.cursor()

    emp_id = int(input('Enter the emp_id to update: '))

    new_name = input('new name: ')
    new_department = input('new department: ')
    new_salary = int(input('new salary: '))

    update_employee = f"UPDATE employees \
                        SET name='{new_name}',\
                            department='{new_department}',\
                            salary={new_salary} \
                        WHERE emp_id={emp_id};"

    try:
        cursor.execute(update_employee)
    except Exception as err:
        print(err)
    else:
        my_con.commit()
        print('Update Successful')
