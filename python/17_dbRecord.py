from sqlTor import SqlTor

with SqlTor() as my_con:
    cursor = my_con.cursor()

    # cursor.execute('''DROP TABLE IF EXISTS employees; 
    # CREATE TABLE employees(
    #     ecode integer,
    #     ename char(20));

    # INSERT INTO employees
    # VALUES(1,'ji');
    # ''')
    # my_con.commit()
