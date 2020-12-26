from sqlite3 import Cursor
import logging
from marksman.utils import ___
logger = logging.getLogger(__name__)


def analyse_exam(cursor: Cursor, exam_id: int) -> dict:
    ''' Gives all stats about the exam

    Args:
        cursor (Cursor):
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
