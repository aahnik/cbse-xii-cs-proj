import csv

with open('sam.txt') as file:
    dict = csv.DictReader(file)
    for row in dict:
        print(row['a'],row['b'])

print(dict)
print(type(dict))