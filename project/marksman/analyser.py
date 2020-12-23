from sqlite3 import Cursor

def analyse_exam(cursor:Cursor,exam_id:int)->dict:
    ''' Gives all stats about the exam

    Args:
        cursor (Cursor):
        exam_id (int): the unique id of the exam

    Returns:
        dict: all the stats
    '''
    
    cursor.execute(f'SELECT AVG(marks) FROM marks WHERE exam={exam_id}')
    average = cursor.fetchone()[0]
    cursor.execute(f'SELECT MAX(marks) FROM marks WHERE exam={exam_id}')
    highest = cursor.fetchone()[0]

    return {'average':average,'highest':highest}

