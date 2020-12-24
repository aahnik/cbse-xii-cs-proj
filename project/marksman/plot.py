from sqlite3 import Cursor
from marksman.analyser import analyse_exam
from matplotlib import pyplot as plt


def plot_student_performance(cursor: Cursor, roll: int, exam_id: int):
    ''' Plots students performance against the batch

    Args:
        cursor (Cursor):
        roll (int): roll no of student
        exam_id (int): unique id of exam
    '''

    cursor.execute(
        f'SELECT marks FROM marks WHERE exam={exam_id} AND student={roll} ')
    marks = cursor.fetchone()[0]

    analysis = analyse_exam(cursor, exam_id)

    x = ['student', 'highest', 'average']
    y = [marks, analysis.get('highest'), analysis.get('average')]

    plt.barh(x, y)

    for index, value in enumerate(y):
        plt.text(value, index, str(value))

    plt.show()
