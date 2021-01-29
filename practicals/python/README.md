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

# 8

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

*( the user chooses menu 1 )*

```shell

>>> 1
Enter roll: 10
Enter name: Gangabati Das
Successfully recorded student

```

*( the screen gets cleared at this point and menu is re-displayed )*

```shell
>>> 2
Enter roll to search student: 12
Student found : Jack Dorsey

Press [ENTER] to continue or CTRL+C to quit
```

# 9

[**Create a binary file with roll number, name and marks. Input a roll number and update the marks.**](q09_marks.py)


```shell
> python q09_marks.py

Press [ENTER] to continue or CTRL+C to quit
```

*( the screen gets cleared at this point and menu is displayed )*

```shell

        MENU for Marks Manager

╒══════════╤══════════════════════════════════╕
│   Choice │ Description                      │
╞══════════╪══════════════════════════════════╡
│        1 │ Record new student               │
├──────────┼──────────────────────────────────┤
│        2 │ Update marks of existing student │
├──────────┼──────────────────────────────────┤
│        3 │ Display all records              │
╘══════════╧══════════════════════════════════╛
    Enter your choice or X to quit

>>>
```

*( the user chooses 1)*

```shell
>>> 1
Enter roll, name and marks seperated by comma
> 13,Jay Bhatt, 80
Sucessfully recorded

Press [ENTER] to continue or CTRL+C to quit
```

*( the screen gets cleared at this point and menu is displayed )*

```shell
>>> 2
Enter roll, and new marks seperated by comma
 13,90
Sucessfully updated
```

*( the screen gets cleared at this point and menu is re-displayed, and now the user tries an invalid update )*

```shell
>>> 2
Enter roll, and new marks seperated by comma
 100,90
Student does not exist in records
```

*( the screen gets cleared at this point and menu is re-displayed)*

```shell


>>> 3
╒════════╤═══════════╤═════════╕
│   Roll │ Name      │   Marks │
╞════════╪═══════════╪═════════╡
│      1 │ Hitesham  │      90 │
├────────┼───────────┼─────────┤
│     34 │ Ramesha   │      89 │
├────────┼───────────┼─────────┤
│     13 │ Jay Bhatt │      90 │
╘════════╧═══════════╧═════════╛

Press [ENTER] to continue or CTRL+C to quit

```

# 10

[**Remove all the lines that contain the character `a' in a file and write it to another file.**](q10_moveA.py)

*Let's first see the original file.*

```shell
> cat data/lines.txt
A good donkey was grazing
No body took notice
But Andrew was eating ice-cream
Hans was jumping with joy
November is the month of winter
Jacob was lost
```

*Now let's run the program.*

```shell
> python q10_moveA.py
Enter the old file path: data/lines.txt
Enter the new file path: data/new_lines.txt
Done!
```

*Now let's see the old file again.*

```shell
> cat data/lines.txt
No body took notice
November is the month of winter
```

*The new file is as follows.*

```shell
> cat data/new_lines.txt
A good donkey was grazing
But Andrew was eating ice-cream
Hans was jumping with joy
Jacob was lost
```

# 11

[**Write a random number generator that generates random numbers between 1 and 6 (simulates a dice).**](q11_dice.py)

```shell
> python q11_dice.py
Throwing a dice ...
3
Press ENTER to throw again, or X to quit
Throwing a dice ...
2
Press ENTER to throw again, or X to quit
Throwing a dice ...
4
Press ENTER to throw again, or X to quit
Throwing a dice ...
3
Press ENTER to throw again, or X to quitX
```

# 12

[**Take a sample of ten phishing e-mails (or any text file) and find most commonly occurring word(s).**](q12_phishy.py)

> **Note** : the file `data/phishing.txt` contains the text extracted from 10 phishing emails
the samples are taken from https://security.berkeley.edu/

```shell
> python q12_phishy.py
Top 20 Commonly used words

╒═══════════╤════╕
│ to        │ 32 │
├───────────┼────┤
│ bank      │ 29 │
├───────────┼────┤
│ the       │ 24 │
├───────────┼────┤
│ immediate │ 24 │
├───────────┼────┤
│ urgent    │ 20 │
├───────────┼────┤
│ you       │ 14 │
├───────────┼────┤
│ for       │ 10 │
├───────────┼────┤
│ in        │ 10 │
├───────────┼────┤
│ my        │  9 │
├───────────┼────┤
│ a         │  9 │
├───────────┼────┤
│ is        │  8 │
├───────────┼────┤
│ of        │  8 │
├───────────┼────┤
│ have      │  7 │
├───────────┼────┤
│ will      │  7 │
├───────────┼────┤
│ I         │  7 │
├───────────┼────┤
│ ID        │  7 │
├───────────┼────┤
│ email     │  6 │
├───────────┼────┤
│ an        │  6 │
├───────────┼────┤
│ from      │  6 │
├───────────┼────┤
│ on        │  6 │
╘═══════════╧════╛
```

# 13

[**Program to create CSV file and store empno,name,salary and search any empno and display name,salary and if not found appropriate message.**](q13_employee.py)

```shell

        MENU for Employee Management

╒══════════╤════════════════════╕
│   Choice │ Description        │
╞══════════╪════════════════════╡
│        1 │ Store new Employee │
├──────────┼────────────────────┤
│        2 │ Search Employee    │
╘══════════╧════════════════════╛
    Enter your choice or X to quit

>>>

```

*( the user chooses 2 )*

```shell
>>> 2
Enter empno to search
>>> 13
Employee not found in records

Press [ENTER] to continue or CTRL+C to quit
```

*( the screen is cleared, and menu re-displayed )*


```shell
>>> 1
Enter empno, name and salary seperated by comma
>>> 12, Akshay Kumar, 10000
Employee recorded

Press [ENTER] to continue or CTRL+C to quit
```

*( the screen is cleared, and menu re-displayed )*

```shell
>>> 2
Enter empno to search
>>> 12
Name:  Akshay Kumar
Salary:  10000

Press [ENTER] to continue or CTRL+C to quit
```


# 14

[**Program to implement Stack in Python using List.**](q14_stack.py)


```shell
        MENU for Stack Operations

╒══════════╤═══════════════╕
│   Choice │ Description   │
╞══════════╪═══════════════╡
│        1 │ Push          │
├──────────┼───────────────┤
│        2 │ Pop           │
├──────────┼───────────────┤
│        3 │ Peek          │
├──────────┼───────────────┤
│        4 │ Display       │
╘══════════╧═══════════════╛
    Enter your choice or X to quit

>>>
```

*( during the execution of the program the screen is cleared and the menu is displayed several times, for an aesthetic experience. To keep stuff clean, the same menu is not being repeated here)*

```shell
>>> 1
Enter data to push: hoch

>>> 1
Enter data to push: poch

>>> 1
Enter data to push: ghosh

>>> 3
ghosh

>>> 4
top
╒═══════╕
│ ghosh │
├───────┤
│ poch  │
├───────┤
│ hoch  │
╘═══════╛

>>> 2
ghosh

>>> 4
top
╒══════╕
│ poch │
├──────┤
│ hoch │
╘══════╛

```

# 15

[**Program to implement Queue in Python using List.**](q15_queue.py)

```shell

        MENU for Queue Operations

╒══════════╤═══════════════╕
│   Choice │ Description   │
╞══════════╪═══════════════╡
│        1 │ Enqueue       │
├──────────┼───────────────┤
│        2 │ Dequeue       │
├──────────┼───────────────┤
│        3 │ Peek (front)  │
├──────────┼───────────────┤
│        4 │ Rear          │
├──────────┼───────────────┤
│        5 │ Display       │
╘══════════╧═══════════════╛
    Enter your choice or X to quit

>>>

```

*( during the execution of the program the screen is cleared and the menu is displayed several times, for an aesthetic experience. To keep stuff clean, the same menu is not being repeated here)*


```shell
>>> 1
Enter data to enqueue: utopia

>>> 1
Enter data to enqueue: distopia

>>> 1
Enter data to enqueue: ultadanga

>>> 5
front
╒════════╤══════════╤═══════════╕
│ utopia │ distopia │ ultadanga │
╘════════╧══════════╧═══════════╛

>>> 3
utopia

>>> 4
ultadanga

>>> 2
utopia

>>> 5
front
╒══════════╤═══════════╕
│ distopia │ ultadanga │
╘══════════╧═══════════╛

```

# 16

[**Program to create 21 Stick Game so that computer always wins.**](q16_stick21.py)

Rules of the 21 Matchstick Puzzle game
- In this Puzzle there are 21 Match Sticks.
- You and Computer will pick up the sticks one by one.
- Sticks can be picked from 1 to 4.
- The who, picked up the last stick, is the loser.


*( during the execution of the program the screen is cleared and the menu is displayed several times, for an aesthetic experience. To keep stuff clean, the same menu is not being repeated here)*

```shell
        MENU for 21 Stick Game

╒══════════╤═══════════════╕
│   Choice │ Description   │
╞══════════╪═══════════════╡
│        1 │ Play the game │
├──────────┼───────────────┤
│        2 │ See the rules │
╘══════════╧═══════════════╛
    Enter your choice or X to quit

>>> 1

Press [ENTER] to continue or CTRL+C to quit

Currently there are 21 sticks
Choose from 1 to 4 sticks
>>> 5
You can choose only between 1 to 4 sticks
Game Aborted

Press [ENTER] to continue or CTRL+C to quit

# MENU IS RE-DISPLAYED
>>> 1

Press [ENTER] to continue or CTRL+C to quit

Currently there are 21 sticks
Choose from 1 to 4 sticks
>>> 2
Now we have 19 sticks left. Its my turn now
I have picked 3 sticks

Currently there are 16 sticks
Choose from 1 to 4 sticks
>>> 4
Now we have 12 sticks left. Its my turn now
I have picked 1 sticks


Currently there are 11 sticks
Choose from 1 to 4 sticks
>>> 2
Now we have 9 sticks left. Its my turn now
I have picked 3 sticks


Currently there are 6 sticks
Choose from 1 to 4 sticks
>>> 4
Now we have 2 sticks left. Its my turn now
I have picked 1 sticks

There is only one stick left. By the rule, you loose 😔
Better Luck next time !

Game Ended

```

# 17

[**Program to connect with database and store record of employee and display records.**](q17_dbRecord.py)

```shell
> python q17_dbRecord.py
table already exists

Press [ENTER] to continue or CTRL+C to quit

# screen gets cleared

No employees recorded yet
RECORD NEW EMPLOYEES
Enter the details to add new employee.

Enter employee id: 12
name: Hans Chen
department: Sales
salary: 10000
New employee added successfully 😃

Press [ENTER] to continue or CTRL+C to quit

# screen gets cleared

Here is the list of all employees

╒══════════╤═══════════╤══════════════╤══════════╕
│   emp_id │ name      │ department   │   salary │
╞══════════╪═══════════╪══════════════╪══════════╡
│       12 │ Hans Chen │ Sales        │    10000 │
╘══════════╧═══════════╧══════════════╧══════════╛

RECORD NEW EMPLOYEES
Enter the details to add new employee.

Enter employee id: 13
name: Jay Chandran
department: Coding
salary: 100000000
New employee added successfully 😃

Press [ENTER] to continue or CTRL+C to quit

# screen gets cleared

Here is the list of all employees

╒══════════╤══════════════╤══════════════╤═══════════╕
│   emp_id │ name         │ department   │    salary │
╞══════════╪══════════════╪══════════════╪═══════════╡
│       12 │ Hans Chen    │ Sales        │     10000 │
├──────────┼──────────────┼──────────────┼───────────┤
│       13 │ Jay Chandran │ Coding       │ 100000000 │
╘══════════╧══════════════╧══════════════╧═══════════╛

RECORD NEW EMPLOYEES
Enter the details to add new employee.

Enter employee id: ^C
Interrupt recieved. Quitting.

```

# 18

[**Program to connect with database and search employee number in table employee and display record, if empno not found display appropriate message.**](q18_dbSearch.py)

```shell
SEARCH EMPLOYEE
Enter employee id: 12
Record found 🥰

                        name: Hans Chen,
                        department: Sales,
                        salary: 10000

Press [ENTER] to continue or CTRL+C to quit

# screen gets cleared

SEARCH EMPLOYEE
Enter employee id: 100
Employee Not found 😢

Press [ENTER] to continue or CTRL+C to quit
^C
Interrupt recieved. Quitting.

```


# 19

[**Program to connect with database and update the employee record of entered empno.**](q19_dbUpdate.py)

```shell

UPDATE EMPLOYEE
Enter employee id: 12
Enter new details of employee.
name: Aahnik Daw
department: Machine Learning
salary: 10
Update Successful!

Press [ENTER] to continue or CTRL+C to quit

# screen gets cleared

UPDATE EMPLOYEE
Enter employee id: 100
Employee does not exist.

Press [ENTER] to continue or CTRL+C to quit
^C
Interrupt recieved. Quitting.

```

# 20

[**Program to connect with database and delete the record of entered employee number.**](q20_dbDelete.py)

```shell
DELETE EMPLOYEE
Enter employee id: 12
Successfully deleted.

Press [ENTER] to continue or CTRL+C to quit

# screen gets cleared

DELETE EMPLOYEE
Enter employee id: 100
Employee does not exist.

Press [ENTER] to continue or CTRL+C to quit
^C
Interrupt recieved. Quitting.
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbNzgyODE3MDQ5XX0=
-->