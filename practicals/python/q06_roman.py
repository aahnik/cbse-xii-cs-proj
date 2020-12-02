''' Write a program using Dictionary and Text file to store roman numbers and find their equivalent.
'''


# base roman numbers and their integer equivalents
ROMAN = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def parse_roman(roman_num: str) -> int:
    ''' Parses a string which is roman numeral and returns equivalent integer.

    Args:
        roman_num (str): Roman numeral to parse

    Raises:
        ValueError: Invalid character in roman numeral
        ValueError: Character occured more than 3 times consecutivel
        ValueError: Invalid roman numeral, incorrect subtractive notation

    Returns:
        int: Integer equivalent
    '''

    # stripping any space
    roman_num = roman_num.strip()

    # convert string to uppercase
    roman_num = roman_num.upper()

    # list of parsed characters
    prev = []

    # total is the value to be returned
    total = 0

    # checker for valid roman string
    largest = 0

    # iterating the roman numeral from right to left
    for chr in roman_num[::-1]:

        # get the integer value of the character, None if not in ROMAN
        curr_num = ROMAN.get(chr)

        # if current character does not exist in ROMAN dictionary
        if not curr_num:
            raise ValueError(f'Invalid character "{chr}" in roman numeral')

        # list of last 3 characters parsed
        last3 = prev[-3:]

        # if last 3 characters exist
        if len(last3) == 3:
            # if all of the last 3 characters are same as current one
            if all(chr == last for last in last3):
                raise ValueError(
                    f'Invalid roman numeral, "{chr}" occured more than 3 times consecutively')

        # if atleast one character have been already parsed
        if prev:
            # numeric value of last character parsed
            last_num = ROMAN.get(prev[-1])

            # if last character is numerically smaller or equal to current one
            if last_num <= curr_num:
                total += curr_num

                # checking validity of roman string
                if curr_num > largest:
                    largest = curr_num
                elif curr_num < largest:
                    raise ValueError(
                        'Invalid roman numeral, incorrect subtractive notation')
            else:
                total -= curr_num

        # parsing the first character, ie the last character of the roman string
        else:
            total += curr_num
            largest = curr_num

        prev.append(chr)
    return total


if __name__ == "__main__":
    # Checking whether our algorithm passes all test cases

    with open('data/romans.txt') as file:
        for line in file:
            roman, decimal = line.split(',')
            print(f'\nTesting if "{roman}" is same as {decimal.strip()}')
            try:
                assert parse_roman(roman) == int(decimal)
                print('True')
            except ValueError as err:
                print(err)
            except AssertionError:
                print(f'False. The correct decimal is {parse_roman(roman)}')
