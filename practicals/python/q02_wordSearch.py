''' Program to search any word in given string/sentence using function
'''


def search(string: str, word: str) -> list:
    ''' Searches given word in a given string and returns search result.

    Args:
        string (str): the given string/sentence in which to search
        word (str): the word to search

    Returns:
        list: list containing indexes of occurence of the word (empty if not found)
    '''

    index = -1
    result = []

    while True:
        index = string.find(word, index+1)
        if index == -1:
            break
        result.append(index)

    return result


if __name__ == "__main__":
    # Testing whether the function works correctly
    assert(search('I am a donkey', 'donkey') == [7])
    assert(search('Foo bar foo bar spam egg', 'bar') == [4, 12])
    assert(search('Bharat Mahan', 'pakistan') == [])
