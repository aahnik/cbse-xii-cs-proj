''' Read a text file and display the number of vowels/consonants/uppercase/lowercase
characters and digits in the file.
'''


def analyse(path: str) -> dict:
    ''' Analyses a text file and displays the number of vowels/consonants/uppercase/lowercase characters and digits in the file.

    Args:
        path (str): path of the file to analyse

    Returns:
        dict: dictionary containing the analysis
    '''

    with open(path, 'r') as file:
        content = file.read()

    analysis = {'vowel': 0,
                'consonant': 0,
                'uppercase': 0,
                'lowercase': 0,
                'digit': 0
                }

    def count(categ: str) -> None:
        ''' 
        Helper function to count 
        '''
        analysis[categ] += 1

    for chr in content:
        if chr.isupper():
            count('uppercase')
        if chr.islower():
            count('lowercase')
        if chr.isdigit():
            count('digit')

        if chr.isalpha():
            if chr.lower() in 'aeiou':
                count('vowel')
            else:
                count('consonant')

    return analysis


if __name__ == "__main__":
    # Test the function
    result = analyse(input('Enter file path\n>>> '))
    print(result)
