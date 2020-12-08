''' General purpose utility module, to reduce number of lines of code in solution 
Enables my code to be DRY (Dont Repeat Yourself)
'''

import os
from tabulate import tabulate
import sys
import signal


def handle_interrupt(*args):
    print('\nInterrupt recieved. Quitting.')
    sys.exit(0)


def clear_screen():

    # handle user interrupt
    signal.signal(signal.SIGTERM, handle_interrupt)
    signal.signal(signal.SIGINT, handle_interrupt)

    # wait for user to see current screen
    input('\nPress [ENTER] to continue or CTRL+C to quit\n')

    if os.name == 'posix':
        # for Linux and Mac
        os.system('clear')
    else:
        # for Windows
        os.system('cls')


def drive_menu(heading: str, menus: dict) -> None:
    ''' Function to allow a menu driven program

    Args:
        heading (str): heading to be displayed on top of menu
        menus (dict): dictionary of menus containing 
        key (menu id) value (another dictionary having `desc` and `func` )
    '''

    table = [[ch, menu['desc']] for ch, menu in menus.items()]
    menu_chart = f'''
        MENU for {heading}
    \n{tabulate(table,tablefmt='fancy_grid',headers=['Choice','Description'])}
    Enter your choice or X to quit
    \n>>> '''
    choice = ''
    while choice != 'X':
        clear_screen()
        choice = input(menu_chart)
        if choice in menus.keys():
            val = menus[choice]['func']()
            if val:
                print(val)
        elif choice == 'X':
            print('Bye 🤗')
        else:
            print('INVALID CHOICE')
