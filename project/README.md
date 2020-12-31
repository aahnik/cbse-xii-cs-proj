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

Please [read this](https://github.com/aahnik/cbse-xii-cs-proj/blob/main/project/docs/cli_for_beginners.md) if you are new to command-line-interfaces.


![marksman --help](https://user-images.githubusercontent.com/66209958/103416978-e303c580-4bae-11eb-9d52-027e9ab41a5d.gif)

> **Tip**: You can use the alias `mm` instead of typing the long `marksman`. Its already set for you when you install.




## CRUD

CRUD stands for Create,Read,Update,Delete. These are the fundamental operations we can perform on a database. `marksman` supports all these operations, through its CLI.

You can CRUD the students, exams and marks entries using `marksman`.

To use the CRUD action, first read its usage.

![marksman crud --help](https://user-images.githubusercontent.com/66209958/103417096-5d344a00-4baf-11eb-96e7-953bde0d0851.gif)

Suppose you want to CRUD students, here is an example.

![marksman crud students](https://user-images.githubusercontent.com/66209958/103417147-8654da80-4baf-11eb-865d-cd545972f3ce.gif)

If you have noticed the above gif carefully, you can observe that when you run the `crud` action with `students` as the option, you are first asked the roll number of the student. If a student with that roll exists, you are shown its details. You also have further options to see more data or update or delete the student.

If the student, with the roll number you entered does not exist, then you will be given the choice to create the student.

If you don't enter any roll number, then `marksman` will display all students in the database and exit.

In the same fashion you can also `crud` exams and marks entries. See more examples of crud in action.

## Email

You can run `marksman email --help` to see how to use the email action. To configure settings for your emailing, read [Configuration](#configuration).

![marksman email --help](https://user-images.githubusercontent.com/66209958/103417378-7db0d400-4bb0-11eb-8cb5-21a18896124d.gif)

Now you have seen, how to use the `email` action, below is an example usage.

![marksman email real](https://user-images.githubusercontent.com/66209958/103419666-ec465f80-4bb9-11eb-8881-7b13c5cf9005.gif)

The result is this:

![imageedit_3_4309512313](https://user-images.githubusercontent.com/66209958/103419928-23694080-4bbb-11eb-9d1f-a86df2f5da42.jpg)

You can also use a custom template for the email message. If no template is found the default will be used.

For using a custom template, create a file called `marksman_email_template.md` and put in the directory from which you are running `marksman`.

You can insert variables in your template like this `::var::`.

Here is a sample template.

```text

Hi ::name::, you have scored ::marks:: in ::exam::.

Highest marks is ::highest::
Average marks is ::average::
Your rank is ::rank::

Please find the attached graph of your performance analysis.

Best Regards,
::inst::

```

The list of supported variables are as follows:

List of variables passed to the template:

  1. name
  2. roll
  3. email
  4. exam
  5. marks
  6. rank
  7. highest
  8. average
  9. inst ( name of institute )

As this template is in a markdown file, you can use any valid markdown formatting.


## Visualize

Data visualization is essential in taking important decisions. We can have a lot of data, but if we cannot make meaningful conclusions from it, then it is useless.

In `marksman` you have the data of marks of all students. `marksman` allows you to easily visualize the performance of the entire batch or of an individual student using simple graphs.

You can learn to use the `visualize` action by using the `--help` flag.

![marksman vis --help](https://user-images.githubusercontent.com/66209958/103417562-23fcd980-4bb1-11eb-8e63-14779290bd49.gif)


Let us see an example, where the teacher can visualize the results of an exam for the entire batch.

![marksman visualize batch](https://user-images.githubusercontent.com/66209958/103417592-4858b600-4bb1-11eb-9e7b-599d00d3e132.gif)

You can also visualize the result of one particular student in that exam. Just use the `--r` flag to supply the roll number of the student to `marksman`. See the example below for clarity.

![marksman visualize student](https://user-images.githubusercontent.com/66209958/103417672-a5ed0280-4bb1-11eb-8d14-a1749f116157.gif)



## Utils

`marksman` provides certain additional utilities to make your life easy. If you want to experiment with `marksman`, without actually putting any data your self, then `marksman` can help you by filling some dummy data. You can also import or export your data from or to CSV file formats.

To learn about the `utils` action, use the `--help` flag.

![marksman utils --help](https://user-images.githubusercontent.com/66209958/103417790-1f84f080-4bb2-11eb-9396-3215170e7a4b.gif)

As you can see that `utils` can accept either of the three arguments:
1. `dummy` : fill the database with fake students, exams and marks for testing purposes.
2. `import` : insert data into the database from CSV files ( of specific format )
3. `export` : write existing data to CSV files

Lets see some examples, for full clarity.

Filling dummy data is a piece of cake. Just run `marksman utils dummy`

![marksman dummy](https://user-images.githubusercontent.com/66209958/103417879-82768780-4bb2-11eb-8689-d7c052c4cfbb.gif)

Now when it comes to importing data from CSV files, it must be in a specific format.

Here is a brief description of the convention that is supported by `marksman`:

| Data | Filename | CSV Headers |
|--|--|--|
| Students | `students.csv` | `roll,name,email` |
| Exams | `exams.csv` | `uid,name` |
| Marks | `marks.csv` | `student,exam,marks` |

All three files must be kept in the same folder. For the CSV file for marks, `student` column should contain the roll, and `exam` the uid.

It is not compulsory to have all the three files for the `import`. Marksman will take whatever data you give it.

See the following example for understanding better.

![marksman import](https://user-images.githubusercontent.com/66209958/103418235-d0d85600-4bb3-11eb-8888-26a78ff76d95.gif)

You can use the `export` option to write the data in the database to `CSV` files.
The exported files will have the same format as shown above.

![marksman utils export](https://user-images.githubusercontent.com/66209958/103418308-13019780-4bb4-11eb-9c3b-3c4c7cd69144.gif)


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
`marksman` will also ask you if you want to save it. If you say yes, `marksman` will save that setting in the global scope ( `~/.marksman/.env` file). In this way, `marksman` can exempt you from manually editing the configs. You can always manually edit them when you want.


## API Reference

As `marksman` is written purely in python, it can easily be imported and extended by other Python programs.

Read the full [API Reference](https://aahnik.github.io/cbse-xii-cs-proj/marksman/) which is published from the docstrings.

