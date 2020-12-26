# marksman

CLI Tool to manage marks of students efficiently.

[![MIT license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/aahnik/cbse-xii-cs-proj/blob/main/project/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![telegram-chat](https://img.shields.io/badge/chat-@aahnikdaw-blue?logo=telegram)](https://telegram.me/aahnikdaw)

## Features

- **CRUD** ( create / read / update / delete )
- **Email** ( email results to students)
- **Visualize** ( visualize the data )
- **Utils** ( fill dummy data / import from csv / export csv )

## Installation

You must have Python 3.9 installed on your system.

Install easily via `pip`, Python's official Package Manager.

```shell
pip install marksman
```

>Note: Linux and Mac users might have to use `pip3` to invoke pip

## Usage

Open your terminal and run `marksman --help` and you will get the following output.

```shell

usage: marksman [-h] [-l] [-v] {crud,email,visualize,utils} ...

CLI Tool to manage marks of students efficiently

optional arguments:
  -h, --help            show this help message and exit
  -l, --loud            increase output verbosity
  -v, --version         show program's version number and exit

actions:
  {crud,email,visualize,utils}
                        actions you can take
    crud                Do crud operations
    email               Email results to students
    visualize           Visualize the results
    utils               Additional utility tools for marksman

For tutorials and documentation visit https://git.io/JL1iI 
```

### `marksman crud`

Running `marksman crud --help` will give this.

```shell

usage: marksman crud [-h] {students,exams,marks}

positional arguments:
  {students,exams,marks}
                        Choose what data you want to crud

optional arguments:
  -h, --help            show this help message and exit
```

> **Tip**: You can use the alias `mm` instead of typing the long `marksman`. Its already set for you when you install.

### `marksman email`

Running `marksman email --help` will give this.

```shell

usage: marksman email [-h] exam

positional arguments:
  exam        exam uid

optional arguments:
  -h, --help  show this help message and exit
```

### `marksman visualize`

Running `marksman visualize --help` will give this.

```shell

usage: marksman visualize [-h] [--r ROLL] exam

positional arguments:
  exam        exam uid

optional arguments:
  -h, --help  show this help message and exit
  --r ROLL    roll number of student (default=0 for all)
```

### `marksman utils`

Running `marksman utils --help` will give this.

```shell

usage: marksman utils [-h] {dummy,import,export}

positional arguments:
  {dummy,import,export}
                        Choose the task you want to perform

optional arguments:
  -h, --help            show this help message and exit
```

## Configuration

You can configure

## Tests

There are test scripts that check whether `marksman` is working correctly. You can easily invoke the tests using `pytest`.

If you do not have pytest installed, install it via `pip`.

```shell
pip install pytest
```

Now run the following:

```shell
pytest --pyargs marksman
```

If the above command fails, use the full path to `marksman`.

## API Reference

As `marksman` is written purely in python, it can easily be imported by other Python programs and easily extended. Read the full API Reference which is published from the docstrings.
