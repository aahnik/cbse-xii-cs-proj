from marksman.utils import ___
from sqlite3 import Cursor
import logging
from marksman.analyser import analyse_exam
from matplotlib import pyplot as plt
logger = logging.getLogger(__name__)


def plot_student_performance(cursor: Cursor, roll: int, exam: int, cache: dict = {}):
    ''' Plots students performance against the batch

    Args:
        cursor (Cursor):
        roll (int): roll no of student
        exam_id (int): unique id of exam
    '''

    cursor.execute(
        ___(f'SELECT marks FROM marks WHERE exam={exam} AND student={roll} '))
    marks = cursor.fetchone()

    if not marks:
        logger.warn('Marks entry does not exist')
        return

    if not cache.get(exam):
        cache[exam] = analyse_exam(cursor, exam)

    analysis = cache[exam]

    x = ['student', 'highest', 'average']
    y = [marks[0], analysis.get('highest'), analysis.get('average')]

    plt.barh(x, y)

    for index, value in enumerate(y):
        plt.text(value, index, str(value))

    plt.show()


def plot_batch_performance(cursor: Cursor, exam: int):
    print('todo')
