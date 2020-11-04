'''
Write a random number generator that generates random numbers
between 1 and 6 (simulates a dice).
'''

import random

while True:
    print('Throwing a dice ...')
    print(random.randint(1,6))
    choice = input('Press ENTER to throw again, or X to quit')
    if choice == 'X':
        break




