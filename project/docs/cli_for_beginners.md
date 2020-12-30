# Command-line for Beginners

If you are new to command-line interfaces, then please read this article before using `marksman`.

## Introduction

In modern times most applications have a Graphical User Interface ( GUI ).

To use a GUI app we can easily see stuff on the screen and click or give input wherever required.

But in the early days of computing, computers were mostly text-based, ie input used to be provided through the keyboard and the output ( some plain text ) was displayed on the screen.

Command-line applications are run from the Terminal.
In all Unix based OS like Mac or Linux, the terminal is installed by default. For Windows you have a [command prompt](https://en.wikipedia.org/wiki/Cmd.exe). You can also install the [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) (which has much more features than the command prompt)

## Terminology

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

## Examples

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
