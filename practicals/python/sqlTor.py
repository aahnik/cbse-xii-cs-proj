'''
An utility module that helps to connect to the my sql database
'''

import mysql.connector
import yaml

# read the config file, and load it into a dict
with open('config.yaml') as f:
    config = yaml.full_load(f)


class SqlTor():
    ''' Context manager to enable easy connection to database
    '''

    def __init__(self) -> None:
        self.conn = mysql.connector.connect(**config)

    def __enter__(self):
        ''' Entry point '''
        if self.conn.is_connected():
            return self.conn
        else:
            raise Exception('Not connected to MySQL')

    def __exit__(self, exception_type, exception_value, traceback):
        ''' Exit '''
        self.conn.close()
