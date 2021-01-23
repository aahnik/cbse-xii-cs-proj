# Python

*This directory contains the solutions to all the 20 Python Questions.*


## 1

[**A program to calculate the n-th term of Fibonacci series using function.**](q01_fibo.py)

```shell

> python -i q01_fibo.py
The 50th fibonacci number is 12586269025
The 100th fibonacci number is 354224848179261915075
>>> fibo(1)
1
>>> fibo(20)
6765
>>> fibo(34)
5702887
>>> fibo(69)
117669030460994
>>> fibo(475)
831082459908702935293955784701120993704369028200651613859972830080739980541065544674812034151699525
>>>

```

## 2

[**Program to search any word in given string/sentence using function.**](q02_wordSearch.py)

```shell

> python -i q02_wordSearch.py
>>> search('I love Computer Science','love')
[2]
>>> search('FAANG rules the world','India')
[]
>>> search('Aeio u aeio aieo','a')
[7, 12]
>>>

```

## 3

[**Read a text file line by line and display each word separated by a # .**](q03_textRead.py)

```shell

> python q03_textRead.py
Enter path of the file to read
 >>> data/text.txt
RSA#algorithm#From#Simple#English#Wikipedia,
kfksf#kjkfjsjflksjk#fkjsdlif#jk#kjjfkljslkfjjklj#ksdfkjskl#l#lkjijfiijkkdflijgrofkjporglrj#kljrjiodngl#pkjgjlj#kjglkjf#jlgkmflj#iodjglkjg#jgldjgljglmtioj5o9m#okptg#;jgojg#oglg;od;

```

## 4

[**Read a text file and display the number of vowels/consonants/uppercase/lowercase characters and digits in the file.**](q04_txtalyser.py)

```shell

> python q04_txtalyser.py
Enter file path
>>> data/text.txt
{'vowel': 4388, 'consonant': 8344, 'uppercase': 535, 'lowercase': 12182, 'digit': 341}

```

## 5

[**Read a text file and display the largest word and maximum number of characters present in a line from text file.**](q05_largestMax.py)

```shell

Enter file path
>>> data/text.txt
Line:1 Empty Line
Line:2 Character Count : 13     Largest Word: algorithm
Line:3 Character Count : 52     Largest Word: the
Line:4 Character Count : 32     Largest Word: to
Line:5 Empty Line
Line:6 Character Count : 197    Largest Word: write
Line:7 Character Count : 566    Largest Word: when
Line:8 Empty Line
Line:9 Character Count : 263    Largest Word: with
Line:10 Empty Line

```

## 6

[**Write a program using Dictionary and Text file to store roman numbers and find their equivalent.**](q06_roman.py)

```shell

> cat data/romans.txt
xii,12
v,5
c,100
cii,102
iiv,3
xv,12

> py -i q06_roman.py

Testing if "xii" is same as 12
True

Testing if "v" is same as 5
True

Testing if "c" is same as 100
True

Testing if "cii" is same as 102
True

Testing if "iiv" is same as 3
Invalid roman numeral, incorrect subtractive notation

Testing if "xv" is same as 12
False. The correct decimal is 15
>>>
>>> parse_roman('xvii')
17
>>> parse_roman('ii')
2
>>> parse_roman('iiii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/aahnik/Projects/cbse-xii-cs-proj/practicals/python/q06_roman.py", line 64, in parse_roman
    raise ValueError(
ValueError: Invalid roman numeral, "I" occured more than 3 times consecutively
>>> parse_roman('c')
100
>>> parse_roman('cxvii')
117
>>>

```

## 7

[**Write a menu driven program to perform read and write operations using a text file called “student.txt” counting student roll_no, name and address.**](q07_student.py)

```shell

> python q07_student.py
Enter directory path to store/retrieve data
>>> data/students.txt
directory created
file `student.txt` created

Press [ENTER] to continue or CTRL+C to quit

```
*( the screen gets cleared at this point and menu is displayed )*

```shell
        MENU for Student Management Portal

╒══════════╤═════════════════════════════════╕
│   Choice │ Description                     │
╞══════════╪═════════════════════════════════╡
│        1 │ Add new student                 │
├──────────┼─────────────────────────────────┤
│        2 │ Display details of all students │
├──────────┼─────────────────────────────────┤
│        3 │ Search student by roll no       │
╘══════════╧═════════════════════════════════╛
    Enter your choice or X to quit

>>>
```
*( the user chooses menu 1 )*

```shell
>>> 1
Enter Student's roll number
>>> 45
Enter name
>>> Horrible Haru
Enter address
>>> Mars
Successfully Recorded

Press [ENTER] to continue or CTRL+C to quit
```

*( the screen gets cleared at this point and menu is re-displayed )*

```shell
>>> 3
Enter roll no. to search
>>> 2
Record not found

Press [ENTER] to continue or CTRL+C to quit
```

*( the screen gets cleared at this point and menu is re-displayed )*

```shell
>>> 2
Roll,Name,Address
45,Horrible Haru,Mars
23,Asdff,jklls
```

*( the screen gets cleared at this point and menu is re-displayed )*

```shell
>>> 3
Enter roll no. to search
>>> 45

        Name : Horrible Haru
        -------------------
        Roll no. : 45

        Address: Mars


Press [ENTER] to continue or CTRL+C to quit
```

## 9

[**Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.**](q08_studentBin.py)

```shell
> python q08_studentBin.py
Enter directory path to store/retrieve data
 >>> data

Press [ENTER] to continue or CTRL+C to quit
```

*( the screen gets cleared at this point and menu is displayed )*

```shell

        MENU for Student Management

╒══════════╤════════════════════════╕
│   Choice │ Description            │
╞══════════╪════════════════════════╡
│        1 │ Record new student     │
├──────────┼────────────────────────┤
│        2 │ Search student by roll │
╘══════════╧════════════════════════╛
    Enter your choice or X to quit

>>>
```

( the user chooses menu 1 )

```shell

>>> 1
Enter roll: 10
Enter name: Gangabati Das
Successfully recorded student

```

*( the screen gets cleared at this point and menu is re-displayed )*

