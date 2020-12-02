'''
Read a text file and display the largest word and maximum number of characters
present in a line from text file.
'''


def analyse(path: str) -> None:
    '''
    Analyses a text file and display the largest word and maximum number of characters present in a line from text file.
    ### Parameters:
        - path:str path of the file to analyse
    ### Returns: None
    '''

    with open(path, 'r') as file:
        content = file.read()

    for line_no, line in enumerate(content.splitlines(), start=1):

        if len(line) != 0:
            print(f'''Line:{line_no} Character Count : {len(line)}''',end='\t')
            words = line.split()
            if words:
                print(f'Largest Word: {max(words)}')
            else:
                print('This line has no words')
            
        else:
            print(f'Line:{line_no} Empty Line')


if __name__ == "__main__":
    analyse(input('Enter file path\n>>> '))

