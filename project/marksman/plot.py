''' This module implements plotting of graphs for the purpose of data visualization'''

import logging
from sqlite3 import Cursor
from matplotlib import pyplot as plt

from marksman.helpers import ___


logger = logging.getLogger(__name__)


def analyse_exam(cursor: Cursor, exam_id: int) -> dict:
    ''' Gives all stats about the exam

    Args:
        cursor (Cursor): sqlite3 Cursor object
        exam_id (int): the unique id of the exam

    Returns:
        dict: all the stats
    '''

    logger.info('Analyzing exam with id ')
    cursor.execute(___(f'SELECT AVG(marks) FROM marks WHERE exam={exam_id}'))
    average = cursor.fetchone()[0]
    cursor.execute(___(f'SELECT MAX(marks) FROM marks WHERE exam={exam_id}'))
    highest = cursor.fetchone()[0]

    return {'average': average, 'highest': highest}


def plot_student_performance(cursor: Cursor, roll: int, exam: int, analysis: dict, path='') -> None:
    ''' Plots students performance against the batch

    Args:
        cursor (Cursor): sqlite3 Cursor object
        roll (int): roll no of student
        exam_id (int): unique id of exam
    '''

    cursor.execute(
        ___(f'SELECT marks FROM marks WHERE exam={exam} AND student={roll} '))
    marks = cursor.fetchone()

    if not marks:
        logger.warning(
            f'''Marks entry does not exist ...
            for exam with uid = {exam} and student with roll = {roll} ''')
        return

    x_axis = ['student', 'highest', 'average']
    y_axis = [marks[0], analysis.get('highest'), analysis.get('average')]

    plt.bar(x_axis, y_axis, width=0.4)

    logger.info(
        f'Plottng horizontal bar grapth with \nx = {x_axis} \n\ny = {y_axis}')

    for index, value in enumerate(y_axis):
        plt.text(value, index, str(value))

    plt.xlabel('Comparison')
    plt.ylabel('Marks')

    if path:
        plt.savefig(path)
        plt.close()
    else:
        plt.show()


def plot_batch_performance(cursor: Cursor, exam: int) -> None:
    ''' Plot the performance of all students in a particular exam

    Args:
        cursor (Cursor): sqlite3 Cursor object
        exam (int): uid of the exam concerned
    '''
    cursor.execute(
        ___(f'SELECT student,marks FROM marks WHERE exam={exam}'))
    marks_list = cursor.fetchall()

    if not marks_list:
        logger.warning(f'No marks entries exist for exam with uid = {exam}')
        return

    x_axis = [f'{i[0]}' for i in marks_list]
    y_axis = [i[1] for i in marks_list]

    plt.stem(x_axis, y_axis)

    logger.info(f'Plotting stem graph with \nx = {x_axis} \n\ny = {y_axis}')

    plt.xlabel('Students')
    plt.ylabel('Marks')

    plt.show()
