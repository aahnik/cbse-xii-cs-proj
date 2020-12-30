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

In modern times most applications have a Graphical User Interface ( GUI ).

To use a GUI app we can easily see stuff on the screen and click or give input wherever required.

But in the early days of computing, computers were mostly text-based, ie input used to be provided through the keyboard and the output ( some plain text ) was displayed on the screen.

Command-line applications are run from the Terminal.
In all Unix based OS like Mac or Linux, the terminal is installed by default. For Windows you have a [command prompt](https://en.wikipedia.org/wiki/Cmd.exe). You can also install the [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) (which has much more features than the command prompt)

Let us familiarize ourselves with some basic terminology.

A command-line application has basically 3 things:
1. name : name by which you call the app
2. positional arguments: required inputs for app
3. optional arguments: optional configurations for running the app

The usage of a command-line application is expressed by a syntax where certain symbols have special meanings. Lets see some common expressions:
1. `|` : or
2. `[]` : optional argument
3. `{}` : any one of

A command-line app is called by its name from the terminal. Open your terminal and write some commands and press enter. You will see the output displayed.

You can issue a command like this:

```shell
program [arguments]
```

Here program is the name of the app, and `[]` symbolizes that the arguments are optional.
The arguments are obviously different for every application.

**Lets understand better by taking some examples:**

Open you terminal and enter `ls` ( for Unix-based OS ) or `dir` for Windows.

You will see the contents of you current directory as output.

Now if you want to clear your terminal, enter `clear` or `cls` (Windows).

Till this point the applications we used, did not take any argument.

Now lets take the example of copying a file:

*Continue reading, but use `copy` for Windows instead of `cp`.*

In the following example the file `a.txt` will be copied to the `Documents` directory.
```shell
cp a.txt Documents
```

In the above example `a.txt` and `Documents` are positional arguments.

Now run `cp --help`, you will know all the positional and optional arguments that `cp` accepts. Here `--help` is an optional argument.

Learn more about the [common operations from the command-line](https://www.geeksforgeeks.org/linux-vs-windows-commands/).

>**Note**: File paths in Windows and Unix look different. Search Google or YouTube to learn more.

You will be happy to know that `marksman` is cross-platform and its usage is consistent across all operating systems.

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

You can configure marksman by using certain environment variables.

`marksman` loads the environment variables from the system's environment and from two special files:
1. the `.env` file in `~/.marksman` ( global settings for `marksman` )
2. the `.env` file in the current directory from which you are running `marksman` ( local settings for `marksman` )

The local settings will override the global settings.

>**Note:** `~` means the user directory. It is different for Unix and Windows.
> Windows 10: `~` expands to `<root>\Users\<username>`
> For Linux: `~` expands to `/home/<username>`
> The `~` symbol can be used directly in the terminal, let your OS expand it for you.

List of environment variables supported:

| Variable | Description | Default |
|--|--|--|
| `marksman_db` | the path to store the `.db` file | `~/.marksman/database.db` |
| `marksman_sender` | email address to be used to send emails |  |
| `marksman_auth` | password to login to sender's email account |  |
| `marksman_smtp_host` | url of SMTP host server  | `smtp.gmail.com` |
| `marksman_smtp_port` | SMTP port for sending emails | `587` |
| `marksman_inst` | name of institute which is sending emails |  |

You can write these settings in the `.env` file like this:

```text
marksman_sender=meet.aahnik@gmail.com
marksman_auth=dummypass
```
If you do not provide a value, the default value will be used.

If a value is required, `marksman` will prompt you to to enter it during program execution.
`marksman` will also ask you if you want to save it. If you say yes, `marksman` will save that setting in the global scope ( `~/.marksman/.env` file). In this way, `marksman` can exempt you from manually editing the configs. You can always manually eidt them when you want.





## API Reference

As `marksman` is written purely in python, it can easily be imported and extended by other Python programs.

Read the full [API Reference](https://aahnik.github.io/cbse-xii-cs-proj/marksman/) which is published from the docstrings.

