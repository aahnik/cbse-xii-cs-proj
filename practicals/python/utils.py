import os
from tabulate import tabulate


def clear_screen():
    input('ENTER to continue: ')  # wait for user to see current screen
    if os.name == 'posix':
        # for Linux and Mac
        os.system('clear')
    else:
        # for Windows
        os.system('cls')


def drive_menu(heading:str, menus:dict) -> None:
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
