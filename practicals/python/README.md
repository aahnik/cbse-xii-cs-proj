# Python

This directory contains the solutions to all the 20 Python Questions.

## Output

**Q1. A program to calculate the n-th term of Fibonacci series using function.**

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

**Q2. Program to search any word in given string/sentence using function.**

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

**Q3. Read a text file line by line and display each word separated by a # .**

```shell

> python q03_textRead.py
Enter path of the file to read
 >>> data/text.txt
RSA#algorithm#From#Simple#English#Wikipedia,
kfksf#kjkfjsjflksjk#fkjsdlif#jk#kjjfkljslkfjjklj#ksdfkjskl#l#lkjijfiijkkdflijgrofkjporglrj#kljrjiodngl#pkjgjlj#kjglkjf#jlgkmflj#iodjglkjg#jgldjgljglmtioj5o9m#okptg#;jgojg#oglg;od;

```

**Q4. Read a text file and display the number of vowels/consonants/uppercase/lowercase characters and digits in the file.**

```shell

> python q04_txtalyser.py
Enter file path
>>> data/text.txt
{'vowel': 4388, 'consonant': 8344, 'uppercase': 535, 'lowercase': 12182, 'digit': 341}

```

**Q5. Read a text file and display the largest word and maximum number of characters present in a line from text file.**

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