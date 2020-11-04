'''
Program to create 21 Stick Game so that computer always wins

21 Matchstick Puzzle game
- In this Puzzle there are 21 Match Sticks.
- You and Computer will pick up the sticks one by one.
- Sticks can be picked from 1 to 4.
- The who, picked up the last stick, is the loser.
'''

from utils import drive_menu, clear_screen


def display_rules():
    print(__doc__)


def game():
    sticks = 21

    while sticks != 1:
        clear_screen()
        print(f'Currently there are {sticks} sticks')
        try:
            user_choice = int(input('Choose from 1 to 4 sticks\n>>> '))
        except ValueError:
            print('You have entered a non integer value')
            return 'Game Aborted'
        try:
            assert user_choice in (1, 2, 3, 4)
        except AssertionError:
            print('You can choose only between 1 to 4 sticks')
            return 'Game Aborted'
        sticks -= user_choice
        print(f'Now we have {sticks} sticks left. Its my turn now')
        computer_choice = 5-user_choice
        sticks -= computer_choice
        print(f'I have picked {computer_choice} sticks')

    print('\nThere is only one stick left. By the rule, you loose 😔')
    print('Better Luck next time !\n')
    return 'Game Ended'


def main():
    menus = {}
    menus['1'] = {'desc': 'Play the game', 'func': game}
    menus['2'] = {'desc': 'See the rules', 'func': display_rules}
    drive_menu('21 Stick Game', menus)


if __name__ == "__main__":
    main()
