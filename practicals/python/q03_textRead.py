''' Read a text file line by line and display each word separated by a # .
'''


path = input('Enter path of the file to read \n >>> ')

try:
    with open(path, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            for word in line.split():
                print(word, end='#')

except FileNotFoundError:
    print("Sorry ! File does not exist")

finally:
    print("Done")
