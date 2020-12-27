import os
from dotenv import load_dotenv
from rich import print

MARKSMAN_DIR = os.path.expanduser('~/.marksman')
GLOBAL_CONFIG_PATH = os.path.join(MARKSMAN_DIR, '.env')
DEFAULT_DB_PATH = os.path.join(MARKSMAN_DIR, 'database.db')

load_dotenv(GLOBAL_CONFIG_PATH)
load_dotenv(override=True)


DB_PATH = os.getenv('marksman_db', DEFAULT_DB_PATH)
SENDER_EMAIL = os.getenv('marksman_sender')
SENDER_AUTH = os.getenv('marksman_auth')
LOUD = bool(os.getenv('marksman_loud'))
SHOW_PATH = bool(os.getenv('marksman_show_path'))
SMTP_HOST = os.getenv('marksman_smtp_host')
SMTP_PORT = int(os.getenv('marksman_smtp_port', 587))
INST_NAME = os.getenv('marksman_inst')

if LOUD:
    print(f'''\n\t[red]YOU ARE WORKING IN A LOUD ENVIRONMENT[/red]
        [dim]DATABASE PATH = {DB_PATH}
        SENDER EMAIL = {SENDER_EMAIL}
        SENDER AUTH = {'EXISTS' if SENDER_AUTH else 'EMPTY'}
        SHOW PATH = {SHOW_PATH} [/dim] \n\n''')
