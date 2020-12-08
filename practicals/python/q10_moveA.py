''' Remove all the lines that contain the character `a' in a file and write it
to another file.
'''


def move(old: str, new: str):
    ''' The function that does the job

    Args:
        old (str): file path of original file
        new (str): file path of new file
    '''
    
    with open(old, 'r') as old_file:
        lines = old_file.readlines()
        a_lines = [line for line in lines if 'a' in line]
        not_a_lines = [line for line in lines if 'a' not in line]

    with open(old, 'w') as old_file:
        old_file.writelines(not_a_lines)

    with open(new, 'w') as new_file:
        new_file.writelines(a_lines)


def main():
    old = input('Enter the old file path: ')
    new = input('Enter the new file path: ')
    move(old, new)


if __name__ == "__main__":
    main()
