''' Dofile '''

from os import curdir
from sqlite3.dbapi2 import Cursor


def fill_dummy_data():
    import sqlite3
    from marksman.models import Modelz
    from marksman.settings import DB_PATH

    my_conn = sqlite3.connect(DB_PATH)
    cursor = my_conn.cursor()

    students = Modelz('students', cursor)
    exams = Modelz('exams',cursor)
    marks = Modelz('marks',cursor)

    

def tests():
    pass

