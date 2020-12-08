''' Take a sample of ten phishing e-mails (or any text file) and find most.
commonly occurring word(s)

the file `data/phishing.txt` contains the text extracted from 10 phishing emails
the samples are taken from https://security.berkeley.edu/
'''

from collections import Counter
from tabulate import tabulate
import os

# in data folder of current directory
filename = os.path.join('data', 'phishing.txt')

with open(filename, 'r') as file:
    content = file.read()

# take all the words
words = Counter(content.split())

# count the most common words
most_common = words.most_common(20)

print('Top 20 Commonly used words\n')
print(tabulate(most_common, tablefmt='fancy_grid'))
