import logging
from sqlite3 import Cursor
from marksman.utils import ___

logger = logging.getLogger(__name__)


def gen_kv_str(kwargs) -> str:
    ''' Generate key value strings

    Returns:
        str: key value string
    '''

    key_val_string = ''

    c = 0

    for key, value in kwargs.items():
        if c >= 1:
            key_val_string += ' AND '
        key_val_string += f'{key} = {value}'
        c += 1

    return key_val_string


def create_tables(cursor: Cursor):
    logger.info('Starting creation of tables')
    try:
        cursor.executescript(___('''
            DROP TABLE IF EXISTS students ;
            CREATE TABLE students(
                        roll INTEGER NOT NULL PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL
                                );

            DROP TABLE IF EXISTS exams ;
            CREATE TABLE exams(
                        uid INTEGER NOT NULL PRIMARY KEY,
                        name TEXT NOT NULL
                            );
            
            DROP TABLE IF EXISTS marks ;
            CREATE TABLE marks(
                        student INTEGER NOT NULL,
                        exam INTEGER NOT NULL,
                        marks INTEGER NOT NULL,

                        FOREIGN KEY (student) 
                            REFERENCES students(roll)
                            ON DELETE CASCADE,
                        
                        FOREIGN KEY (exam) 
                            REFERENCES exams(uid)
                            ON DELETE CASCADE,

                        PRIMARY KEY (student,exam)
                            );
                '''))
    except Exception as err:
        logger.warning(
            'Failed to create tables. Delete the database file and try again')
        logger.exception(err)
    else:
        logger.info('Successfully created tables')


def foreign_key_constraint(cursor: Cursor):
    cursor.execute(___('PRAGMA foreign_keys = ON;'))


class Modelz:

    def __init__(self, table: str, cursor: Cursor) -> None:
        ''' 

        Args:
            table (str): [description]
            cursor (Cursor): [description]
        '''
        self.table = table
        self.cursor = cursor
        logger.info(f'Created {self}')

    def __str__(self) -> str:
        return f'Modelz object for {self.table}'

    def fetch(self, **conds) -> list:
        ''' Fetches a list of results based on condition parameters

        Returns:
            list: results
        '''

        cond_str = gen_kv_str(conds)
        self.cursor.execute(___(f'''SELECT * FROM {self.table} 
                            {'WHERE' if cond_str else ''} {cond_str}'''))
        return self.cursor.fetchall()

    def exists(self, **conds) -> tuple or None:
        ''' Checks whether an entry exists, based on given condition

        Returns:
            tuple or None: returns the tuple containing the entity if exists
                           else None
        '''

        cond_str = gen_kv_str(conds)
        self.cursor.execute(___(f'''SELECT * 
                                FROM {self.table} 
                                WHERE {cond_str}'''))

        return self.cursor.fetchone()

    def insert(self, values: tuple) -> None:
        ''' Inserts the values provided in the table

        Args:
            values (tuple): values to insert
        '''

        self.cursor.execute(___(f'''INSERT INTO {self.table} 
                                VALUES{values} '''))
        logger.info(f'{values} were inserted using {self}')

    def update(self, set_string: str, **conds) -> None:
        ''' Updates the table using set_string, based on given conditions

        Args:
            set_string (str): the string to put beside SET keyword in SQL
        '''

        cond_str = gen_kv_str(conds)
        self.cursor.execute(___(f'''UPDATE  {self.table}
                                SET {set_string}
                                WHERE {cond_str} '''))

    def delete(self, **conds) -> None:
        ''' Deletes the entries satisfying given condtions
        '''

        cond_str = gen_kv_str(conds)
        self.cursor.execute(___(f'''DELETE FROM {self.table}
                                WHERE {cond_str} '''))
