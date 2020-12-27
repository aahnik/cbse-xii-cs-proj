# marksman

CLI Tool to manage marks of students efficiently.

[![MIT license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/aahnik/cbse-xii-cs-proj/blob/main/project/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![telegram-chat](https://img.shields.io/badge/chat-@aahnikdaw-blue?logo=telegram)](https://telegram.me/aahnikdaw)
[![PyPI](https://img.shields.io/pypi/v/marksman)](https://pypi.org/project/marksman/)

## Features

- [**CRUD**](#crud) ( create / read / update / delete )
- [**Email**](#crud) ( email results to students )
- [**Visualize**](#visualize) ( visualize the data )
- [**Utils**](#utils) ( fill dummy data / import from csv / export csv )

## Getting Started

You must have Python 3.9 installed on your system.

Install easily via `pip`, Python's official Package Manager.

```shell
pip install marksman
```

>Note: Linux and Mac users might have to use `pip3` to invoke pip


<details>
<summary> Read this if you are new to command-line-interfaces. </summary>

</details>

<details>
<summary> Usage </summary>

Open your terminal and run `marksman --help` and you will get the following output.

```shell

usage: marksman [-h] [-l] [-v] {crud,email,visualize,utils} ...

CLI Tool to manage marks of students efficiently

optional arguments:
  -h, --help            show this help message and exit
  -l, --loud            increase output verbosity
  -v, --version         show programs version number and exit

actions:
  {crud,email,visualize,utils}
                        actions you can take
    crud                Do crud operations
    email               Email results to students
    visualize           Visualize the results
    utils               Additional utility tools for marksman

For tutorials and documentation visit https://git.io/JL1iI 

```
> **Tip**: You can use the alias `mm` instead of typing the long `marksman`. Its already set for you when you install.

</details>


## CRUD

Description of the crud 

<details>
<summary> Usage </summary>

Running `marksman crud --help` will give this.

```shell

usage: marksman crud [-h] {students,exams,marks}

positional arguments:
  {students,exams,marks}
                        Choose what data you want to crud

optional arguments:
  -h, --help            show this help message and exit
```

</details>



<details>
<summary> Examples </summary>

</details>


## Email

<details>
<summary> Usage </summary>

Running `marksman email --help` will give this.

```shell

usage: marksman email [-h] exam

positional arguments:
  exam        exam uid

optional arguments:
  -h, --help  show this help message and exit
```

</details>

<details>
<summary> Examples </summary>

</details>

## Visualize

<details>
<summary> Usage </summary>

Running `marksman visualize --help` will give this.

```shell

usage: marksman visualize [-h] [--r ROLL] exam

positional arguments:
  exam        exam uid

optional arguments:
  -h, --help  show this help message and exit
  --r ROLL    roll number of student (default=0 for all)
```

</details>

<details>
<summary> Examples </summary>

</details>

## Utils

<details>
<summary> Usage </summary>

Running `marksman utils --help` will give this.

```shell

usage: marksman utils [-h] {dummy,import,export}

positional arguments:
  {dummy,import,export}
                        Choose the task you want to perform

optional arguments:
  -h, --help            show this help message and exit
```

</details>


<details>
<summary> Examples </summary>

</details>

## Configuration

You can configure



## API Reference

As `marksman` is written purely in python, it can easily be imported and extended by other Python programs.

Read the [full API Reference]() which is published from the docstrings.

