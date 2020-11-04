'''
Program to implement Queue in Python using List
'''
from tabulate import tabulate
from utils import drive_menu


class Queue():
    def __init__(self, length=9999) -> None:
        self.q = []
        if (type(length) != int) or (length <= 0):
            print(f'Invalid Limit : must be int greater than zero')
            return
        self.length = length

    def is_empty(self):
        return self.q == []

    def front(self):
        if self.is_empty():
            print('Empty Queue : No front element')
            return
        return self.q[0]

    def rear(self):
        if self.is_empty():
            print('Empty Queue : No rear element')
            return
        return self.q[len(self.q)-1]

    def enqueue(self, data=None):
        if not data:
            data = input('Enter data to enqueue: ')
        if len(self.q) == self.length:
            print('Queue Overflow : Size of queue exceeded length')
            return
        self.q.append(data)

    def dequeue(self):
        if self.is_empty():
            print('Queue Underflow : Empty queue, nothing to dequeue')
            return
        rm = self.q[0]
        del self.q[0]
        return rm

    def display(self):
        if self.is_empty():
            return
        print('front')
        print(tabulate([self.q], tablefmt='fancy_grid'))


def main():
    qu = Queue()
    menus = {}
    menus['1'] = {'desc': 'Enqueue', 'func': qu.enqueue}
    menus['2'] = {'desc': 'Dequeue', 'func': qu.dequeue}
    menus['3'] = {'desc': 'Peek (front)', 'func': qu.front}
    menus['4'] = {'desc': 'Rear', 'func': qu.rear}
    menus['5'] = {'desc': 'Display', 'func': qu.display}
    drive_menu('Queue Operations', menus)


if __name__ == "__main__":
    main()
