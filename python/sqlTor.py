'''
An utility module that helps to connect to the my sql database
'''

import mysql.connector


HOST = ''
USER_NAME = ''
PASS = ''
DB = ''


class SqlTor():
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(host='HOST',
                                            user='USER_NAME',
                                            passwd='PASS',
                                            database='DB')
    def __enter__(self):
        if self.conn.is_connected():
            return self.conn
        else:
            raise Exception('Not connected to MySQL')

    def __exit__(self):
        self.conn.close()

        
