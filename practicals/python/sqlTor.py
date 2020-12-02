'''
An utility module that helps to connect to the my sql database
'''

import mysql.connector
import yaml

with open('config.yaml') as f:
    config = yaml.full_load(f)


class SqlTor():
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(**config)
    def __enter__(self):
        if self.conn.is_connected():
            return self.conn
        else:
            raise Exception('Not connected to MySQL')

    def __exit__(self, exception_type, exception_value, traceback):
        self.conn.close()
