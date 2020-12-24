''' Dofile '''

import logging


logging.basicConfig(level=logging.INFO)


def fill_dummy():
    try:
        import random
        import sqlite3
        from marksman.models import Modelz, create_tables
        from marksman.settings import DB_PATH

        my_conn = sqlite3.connect(DB_PATH)
        cursor = my_conn.cursor()

        create_tables(cursor)

        students = Modelz('students', cursor)
        exams = Modelz('exams', cursor)
        marks = Modelz('marks', cursor)

        for i in range(1, 50):
            students.insert((i, f'stud_{i}', f'{i}@email.com'))

        for j in range(1, 10):
            exams.insert((j, f'exam_{j}'))

        for j in range(1, 10):
            for i in range(1, 50):
                m = random.randint(1, 100)
                marks.insert((i, j, m))

        my_conn.commit()

        cursor.close()

        my_conn.close()
    except Exception as err:
        logging.exception(err)
    else:
        logging.info('\n \n filling dummy data succeded')
    finally:
        logging.info('exiting')


def tests():
    import sqlite3
    from marksman.settings import DB_PATH
    my_conn = sqlite3.connect(DB_PATH)
    cursor = my_conn.cursor()

    from marksman.plot import plot_student_performance

    # for s in range(1, 10):
    plot_student_performance(cursor, 10, 3)
