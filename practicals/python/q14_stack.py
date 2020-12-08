''' Program to implement Stack in Python using List
'''

from tabulate import tabulate
from utils import drive_menu


class Stack():
    def __init__(self, limit=9999) -> None:
        self.stk = []
        if (type(limit) != int) or (limit <= 0):
            print(f'Invalid Limit : must be int greater than zero')
            return
        self.limit = limit

    def is_empty(self):
        return self.stk == []

    def peek(self):
        if self.is_empty():
            print('Nothing to peek: Stack is empty')
            return
        return self.stk[len(self.stk)-1]

    def push(self, data=None):
        if not data:
            data = input('Enter data to push: ')
        if len(self.stk) == self.limit:
            print('Stack Overflow : Size of stack exceeded limit')
            return
        self.stk.append(data)

    def pop(self):
        if self.is_empty():
            print('Stack Underflow : Cannot pop from empty stack')
            return
        return self.stk.pop()

    def display(self):
        if self.is_empty():
            return
        else:
            print('top')
            print(tabulate([[item] for item in self.stk[::-1]],
                           tablefmt='fancy_grid'))


def main():
    stack = Stack()
    menus = {}
    menus['1'] = {'desc': 'Push', 'func': stack.push}
    menus['2'] = {'desc': 'Pop', 'func': stack.pop}
    menus['3'] = {'desc': 'Peek', 'func': stack.peek}
    menus['4'] = {'desc': 'Display', 'func': stack.display}
    drive_menu('Stack Operations', menus)


if __name__ == "__main__":
    main()
