
# Challenge 1: Learning From Documentation

The typical need you'll have for documentation is just to figure out how to use all these dang programs, and a specific case of that is figuring out what arguments to specify on the command line.
This module will mostly dig into that concept, as a proxy for figuring out how to use the programs in general.
Through the rest of the module, you'll go through various ways of asking the environment for help for the programs, but first, we'll dig into the concept of reading documentation.

The correct usage of programs depends, in a large part, on the proper specification of arguments to them.
Recall the `-a` of `ls -a` in the `hidden files` challenge of the [Basic Commands](/linux-luminarium/commands) module: that `-a` was an _argument_ that told `ls` to list out hidden files as well as non-hidden files.
Because we _wanted_ to list out hidden files, invoking `ls` with the `-a` argument was the correct way to use it in our scenario.

The program for this challenge is `/challenge/challenge`, and you'll need to invoke it properly in order for it to give you the flag.
Let's pretend that this is its documentation:

> Welcome to the documentation for `/challenge/challenge`! To properly run this program, you will need to pass it the argument of `--giveflag`. Good luck!

Given that knowledge, go get the flag!

## Solution:

After the terminal comes up, the user needs to run the `/challenge/challenge` program with an argument of `--giveflag` as written in the documentation. This will print the flag.

#### Commands run: 

```sh
$ /challenge/challenge --giveflag
```

## Flag: 

```
pwn.college{cwnVQ5fAiKDk84iq5F6DV-r3Iw3.QX0ITO0wSOxAzNzEzW}
```

# Challenge 2: Learning Complex Usage

While using most commands is straightforward, the usage of some commands can get quite complex.
For example, the arguments to commands like `sed` and `awk`, which we're definitely not getting into right now, are entire programs in an esoteric programming language!
Somewhere on the spectrum between `cd` and `awk` are commands that take arguments to their arguments...

This sounds crazy, but you've already encountered this with the `find` level in [Basic Commands](/linux-luminarium/commands).
`find` has a `-name` argument, and the `-name` argument itself takes an argument specifying the name to search for.
Many other commands are analogous.

Here is this level's documentation for `/challenge/challenge`:

> Welcome to the documentation for `/challenge/challenge`! This program allows you to print arbitrary files to the terminal, when given the `--printfile` argument. The argument to the `--printfile` argument is the path of the flag to read. For example, `/challenge/challenge --printfile /challenge/DESCRIPTION.md` will print out the description of the level!

Given that documentation, go get the flag!

## Solution:

After the terminal comes up, the user needs to run the `/challenge/challenge` program with an argument of `--giveflag` followed by a path to the flag file `/flag` as written in the documentation. This will print the flag.

#### Commands run: 

```sh
$ /challenge/challenge --printfile /flag
```

## Flag: 

```
pwn.college{MP6Z0GNqQzJu2JSlQTftQYgoZmu.QX1ITO0wSOxAzNzEzW}
```

# Challenge 3: Reading Manuals

This level introduces the `man` command.
`man` is short for `manual`, and will display (if available) the manual of the command you pass as an argument.
For example, let's say we wanted to learn about the `yes` command (_yes_, this is a real command):

```sh
hacker@dojo:~$ man yes
```

This will display the manual page for `yes`, which will look something like this:

```text
YES(1)                           User Commands                          YES(1)

NAME
       yes - output a string repeatedly until killed

SYNOPSIS
       yes [STRING]...
       yes OPTION

DESCRIPTION
       Repeatedly output a line with all specified STRING(s), or 'y'.

       --help display this help and exit

       --version
              output version information and exit

AUTHOR
       Written by David MacKenzie.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report any translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright  ©  2020  Free Software Foundation, Inc.  License GPLv3+: GNU
       GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free  to  change  and  redistribute  it.
       There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       Full documentation <https://www.gnu.org/software/coreutils/yes>
       or available locally via: info '(coreutils) yes invocation'

GNU coreutils 8.32               February 2022                          YES(1)
```

The important sections are:

```text
NAME(1)                           CATEGORY                          NAME(1)

NAME
        This gives the name (and short description) of the command or
        concept discussed by the page.

SYNOPSIS
        This gives a short usage synopsis. These synopses have a standard
        format. Typically, each line is a different valid invocation of the
        command, and the lines can be read as:

        COMMAND [OPTIONAL_ARGUMENT] SINGLE_MANDATORY_ARGUMENT
        COMMAND [OPTIONAL_ARGUMENT] MULTIPLE_ARGUMENTS...

DESCRIPTION
        Details of the command or concept, with detailed descriptions
        of the various options.

SEE ALSO
        Other man pages or online resources that might be useful.

COLLECTION                        DATE                          NAME(1)
```

You can scroll around the manpage with your arrow keys and PgUp/PgDn.
When you're done reading the manpage, you can hit `q` to quit.

Manpages are stored in a centralized database.
If you're curious, this database lives in the `/usr/share/man` directory, but you never need to interact with it directly: you just query it using the `man` command.
The arguments to the `man` command aren't file paths, but just the names of the entries themselves (e.g., you run `man yes` to look up the `yes` manpage, rather than `man /usr/bin/yes`, which would be the actual path to the `yes` program but would result in `man` displaying garbage).

The challenge in this level has a secret option that, when you use it, will cause the challenge to print the flag.
You must learn this option through the man page for `challenge`!

## Solution:

After the terminal comes up, the user needs to use the `man` command to get the manual page for the challenge program. Then, the user must use the arguments given in the man page to get the flag.

#### Commands run: 

```sh
$ man challenge
```
```
CHALLENGE(1)                                                                       Challenge Commands                                                                      CHALLENGE(1)

NAME
       /challenge/challenge - print the flag!

SYNOPSIS
       challenge OPTION

DESCRIPTION
       Output the flag when called with the right arguments.

       --fortune
              read a fortune

       --version
              output version information and exit

       --tlzfjl NUM
              print the flag if NUM is 033

AUTHOR
       Written by Zardus.

REPORTING BUGS
       The repository for this dojo: <https://github.com/pwncollege/linux-luminarium/>

SEE ALSO
       man(1) bash-builtins(7)

pwn.college                                                                             May 2024                                                                           CHALLENGE(1)
 Manual page challenge(1) line 1/31 (END) (press h for help or q to quit)
```
```sh
 $ /challenge/challenge --tlzfjl 033
```

## Flag: 

```
pwn.college{0RQtlGHz_3f3j-lNhdAjz66Kjy0.QX0EDO0wSOxAzNzEzW}
```

# Challenge 4: Searching Manuals

You can scroll man pages with the arrow keys (and PgUp/PgDn) and search with `/`.
After searching, you can hit `n` to go to the next result and `N` to go to the previous result.
Instead of `/`, you can use `?` to search backwards!

Find the option that will give you the flag by reading the `challenge` man page.

## Solution:

After the terminal comes up, the user needs to use the `man` command to get the manual page for the challenge program. Then, the user must then press the `/` button to search for `flag` and use `n` to go to the next result and `N` to go to the previous result till the required argument is found. Then, the user must use the arguments given in the man page to get the flag.

#### Commands run: 

```sh
$ man challenge
```
*press `n` to go to the next result and `N` to go to the previous result till the argument is found.*
```sh
$ /challenge/challenge --gepgj
```

## Flag: 

```
pwn.college{gK07E2sff_irgRwYSS-2QfxGzjq.QX1EDO0wSOxAzNzEzW}
```

# Challenge 5: Searching For Manuals

This level is tricky: it hides the manpage for the challenge by randomizing its name.
Luckily, all of the manpages are gathered in a searchable database, so you'll be able to search the man page database to find the hidden challenge man page!
To figure out how to search for the right manpage, read the `man` page manpage by doing: `man man`!

---
**HINT 1:** `man man` teaches you advanced usage of the `man` command itself, and you must use this knowledge to figure out how to search for the hidden manpage that will tell you how to use `/challenge/challenge`

**HINT 2:** though the manpage is randomly named, you still actually use `/challenge/challenge` to get the flag!

## Solution:

After the terminal comes up, the user needs to search for the man page title for the `challenge` program by entering `man -k challenge`. The user can run `man man` to learn this. The user can then open the man page for the `challenge` program using the found title and find the argument to print the flag. The flag can then be captured by running `/challenge/challenge` using the required argument.

#### Commands run: 

```sh
$ man man
```
*press `n` to go to the next result and `N` to go to the previous result till the required argument is found.*
```sh
$ man -k challenge
sbrskoteuf (1)       - print the flag!
$ man sbrskoteuf
```
```
CHALLENGE(1)                                                                       Challenge Commands                                                                      CHALLENGE(1)

NAME
       /challenge/challenge - print the flag!

SYNOPSIS
       challenge OPTION

DESCRIPTION
       Output the flag when called with the right arguments.

       --fortune
              read a fortune

       --version
              output version information and exit

       --sbrsko NUM
              print the flag if NUM is 020

AUTHOR
       Written by Zardus.

REPORTING BUGS
       The repository for this dojo: <https://github.com/pwncollege/linux-luminarium/>

SEE ALSO
       man(1) bash-builtins(7)

pwn.college                                                                             May 2024                                                                           CHALLENGE(1)
 Manual page sbrskoteuf(1) line 1/31 (END) (press h for help or q to quit)
```
```sh
$ /challenge/challenge --sbrsko 020
```

## Flag: 

```
pwn.college{ULs0brDDskTQ2ote0T0ufnKEU8W.QX2EDO0wSOxAzNzEzW}
```

# Challenge 6: Helpful Programs

Some programs don't have a man page, but might tell you how to run them if invoked with a special argument.
Usually, this argument is `--help`, but it can often be `-h` or, in rare cases, `-?`, `help`, or other esoteric values like `/?` (though that latter is more frequently encountered on Windows).

In this level, you will practice reading a program's documentation with `--help`.
Try it out!

## Solution:

The user can enter `/challenge/challenge --help` to find the required arguments which must be used to obtain the flag. The user can then, run the `challenge` program with the required arguments to obtain the print value and then the flag itself.

#### Commands run: 

```sh
$ /challenge/challenge --help
usage: a challenge to make you ask for help [-h] [--fortune] [-v] [-g GIVE_THE_FLAG] [-p]

optional arguments:
  -h, --help            show this help message and exit
  --fortune             read your fortune
  -v, --version         get the version number
  -g GIVE_THE_FLAG, --give-the-flag GIVE_THE_FLAG
                        get the flag, if given the correct value
  -p, --print-value     print the value that will cause the -g option to give you the flag
$ /challenge/challenge -p
The secret value is: 779
$ /challenge/challenge -g 779
```

## Flag: 

```
pwn.college{IW7W79fnecFhYD-gHalUhBUVFUj.QX3IDO0wSOxAzNzEzW}
```

# Challenge 7: Help for Builtins

Some commands, rather than being programs with man pages and help options, are built into the shell itself.
These are called *builtins*.
Builtins are invoked just like commands, but the shell handles them internally instead of launching other programs.
You can get a list of shell builtins by running the *builtin* `help`, as so:

```sh
hacker@dojo:~$ help
```

You can get help on a specific one by passing it to the `help` builtin.
Let's look at a builtin that we've already used earlier, `cd`!

```sh
hacker@dojo:~$ help cd
cd: cd [-L|[-P [-e]] [-@]] [dir]
    Change the shell working directory.
    
    Change the current directory to DIR.  The default DIR is the value of the
    HOME shell variable.
...
```

Some good information!
In this challenge, we'll practice using `help` to look up help for builtins.
This challenge's `challenge` command is a shell builtin, rather than a program.
Like before, you need to lookup its help to figure out the secret value to pass to it!

## Solution:

After the terminal comes up, the user needs to run `help challenge` to get the help page for the `challenge` program which will contain the required argument and secret value to obtain the flag. The user can then run the `challenge` program with the `--secret` argument and the `secret value` to capture the flag.

#### Commands run: 

```sh
$ help challenge
challenge: challenge [--fortune] [--version] [--secret SECRET]
    This builtin command will read you the flag, given the right arguments!
    
    Options:
      --fortune         display a fortune
      --version         display the version
      --secret VALUE    prints the flag, if VALUE is correct

    You must be sure to provide the right value to --secret. That value
    is "QpvRwG_i".
$ challenge --secret QpvRwG_i
```

## Flag: 

```
pwn.college{QpvRwG_ihhPACp1o8OntfaFPTOr.QX0ETO0wSOxAzNzEzW}
```
