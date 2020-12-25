# marksman

A simple command-line app to manage marks of students.

## Features

- CRUD ( create|read|update|delete students/exams/marks )
- Email ( email results to students)
- Visualize ( visualize the data )

## Installation

You must have Python 3.9 installed on your system.

Install easily via `pip`, Python's official Package Manager.

```shell
pip install marksman
```

>Note: Linux and Mac users might have to use `pip3` to invoke pip

## Usage

```text
usage: marksman [-h] [-l] [-v] {crud,email,visualize} ...

Command Line Tool to manage marks of students

optional arguments:
  -h, --help            show this help message and exit
  -l, --loud            increase output verbosity
  -v, --version         show program's version number and exit

actions:
  {crud,email,visualize}
                        actions you can take
    crud                Do crud operations
    email               Email results to students
    visualize           Visualize the results

To learn how to use an action (crud|email|visualize) use 
    marksman <action> -h

```


