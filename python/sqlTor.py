'''
An utility module that helps to connect to the my sql database
'''

import mysql.connector


class SqlTor():
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(host='localhost',
                                            user='newuser',
                                            passwd='password',
                                            database='py_sql')

    def __enter__(self):
        if self.conn.is_connected():
            return self.conn
        else:
            raise Exception('Not connected to MySQL')

    def __exit__(self, exception_type, exception_value, traceback):
        self.conn.close()
