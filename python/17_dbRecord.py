from sqlTor import SqlTor

with SqlTor() as my_con:
    # print(my_con)
    cursor = my_con.cursor()
    # print(cursor)

    cursor.execute('''
                DROP TABLE IF EXISTS employees;
                CREATE TABLE employees(
                emp_id integer,
                name char(20),
                department char(20),
                salary integer
                );''',multi=True)
    my_con.commit()
    cursor.execute('''SELECT * FROM employees''')
    employees = cursor.fetchall()
    print('\n\nHere is the list of all employees')
    print(employees)
    print('\n\n')
    # print(cursor)

    while True:
        print('Enter the details to add new employee')
        emp_id = int(input('employee id: '))
        name = input('name: ')
        department = input('department: ')
        salary = int(input('salary: '))

        cursor.execute(f'''INSERT INTO employees
            VALUES(
                {emp_id},
                '{name}',
                '{department}',
                {salary}
                ); 
        ''')
        # print(cursor)
        my_con.commit()

        print('New employee added successfully 😃')
        input('Press ENTER to add another employee or CTRL+C to quit')

        # cursor.execute('''SELECT * FROM employees''')
        # employees = cursor.fetchall()
        # print('\n\nHere is the list of all employees')
        # print(employees)
        # print('\n\n')
