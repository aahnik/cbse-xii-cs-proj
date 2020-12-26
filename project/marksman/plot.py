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
        logger.warn(
            f'Marks entry does not exist for exam with uid = {exam} and student with roll = {roll} ')
        return

    if not cache.get(exam):
        cache[exam] = analyse_exam(cursor, exam)

    analysis = cache[exam]

    x = ['student', 'highest', 'average']
    y = [marks[0], analysis.get('highest'), analysis.get('average')]

    plt.bar(x, y, width=0.4)

    logger.info(f'Plottng horizontal bar grapth with \nx = {x} \n\ny = {y}')

    for index, value in enumerate(y):
        plt.text(value, index, str(value))

    plt.xlabel('Comparison')
    plt.ylabel('Marks')

    plt.show()


def plot_batch_performance(cursor: Cursor, exam: int):
    cursor.execute(
        ___(f'SELECT student,marks FROM marks WHERE exam={exam}'))
    marks_list = cursor.fetchall()

    if not marks_list:
        logger.warning(f'No marks entries exist for exam with uid = {exam}')
        return

    x = [f'{i[0]}' for i in marks_list]
    y = [i[1] for i in marks_list]

    plt.stem(x, y)

    logger.info(f'Plotting stem graph with \nx = {x} \n\ny = {y}')

    plt.xlabel('Students')
    plt.ylabel('Marks')

    plt.show()
