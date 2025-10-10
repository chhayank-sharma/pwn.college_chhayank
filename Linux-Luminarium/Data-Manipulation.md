
# Challenge 1: Translating characters

One of the purposes of piping data is to _modify_ it.
Many Linux commands will help you modify data in really cool ways.
One of these is `tr`, which `tr`anslates characters it receives over standard input and prints them to standard output.

In its most basic usage, `tr` translates the character provided in its first argument to the character provided in its second argument:

```sh
hacker@dojo:~$ echo OWN | tr O P
PWN
hacker@dojo:~$
```

It can also handle multiple characters, with the characters in different positions of the first argument replaced with associated characters in the second argument.

```sh
hacker@dojo:~$ echo PWM.COLLAGE | tr MA NE
PWN.COLLEGE
hacker@dojo:~$
```

Now, you try it!
In this level, `/challenge/run` will print the flag but will swap the casing of all characters (e.g., `A` will become `a` and vice-versa).
Can you undo it with `tr` and get the flag?

## Solution:

In this challenge, `.challenge/run` will print the flag with but with lower case and upper case switched. To get the actual flag, we must use the `tr` command to switch the cases. If done correctly, this will give us the correct flag.

#### Commands run: 

```sh
$ /challenge/run | tr ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```

## Flag: 

```
pwn.college{4Rj8KDVsVIgtMxTQq82F1gI7iLA.01MxEzNxwSOxAzNzEzW}
```

# Challenge 2: Deleting characters

`tr` can also translate characters to nothing (i.e., _delete_ them).
This is done via a `-d` flag and an argument of what characters to delete:

```sh
hacker@dojo:~$ echo PAWN | tr -d A
PWN
hacker@dojo:~$
```

Pretty simple!
Now you give it a try.
I'll intersperse some decoy characters (specifically: `^` and `%`) among the flag characters.
Use `tr -d` to remove them!

## Solution:

In this challenge, `/challenge/run` will print the flag but it will have the characters `^` and `%` interspersed throughout it. To get the actual flag, we must use the `tr` command to remove all instances of `^` and `%`. If done correctly, this will give us the correct flag.

#### Commands run: 

```sh
$ /challenge/run | tr -d ^%
```

## Flag: 

```
pwn.college{k9ynbfSB5fyJccE6rpxmvgk8q9v.0FNxEzNxwSOxAzNzEzW}
```

# Challenge 3: Deleting newlines

A common class of characters to remove is a line separator.
This happens when you have a stream of data that you want to turn into a single line for further processing.
You can specify newlines almost like any other character, by _escaping_ them:

```sh
hacker@dojo:~$ echo "hello_world!" | tr _ "\n"
hello
world!
hacker@dojo:~$
```

Here, the backslash (`\`) signifies that the character that follows it is a standin for a character that's hard to input into the shell normally.
The newline, of course, is hard to input because when you typically hit `Enter`, you'll run the command itself.
`\n` is a standin for this newline, and it _must_ be in quotes to prevent the shell interpreter itself from trying to interpret it and pass it to `tr` instead.

Now, let's combine this with deletion.
In this challenge, we'll inject a bunch of newlines into the flag.
Delete them with `tr`'s `-d` flag and the _escaped_ newline specification!

----
**Fun fact!**
Want to _actually_ replace a backslash (`\`) character?
Because `\` is the escape character, you gotta escape it!
`\\` will be treated as a backslash by `tr`.
This isn't relevant to this challenge, but is a fun fact nonetheless!

## Solution:

In this challenge, `/challenge/run` will print the flag but it will have a newline after each character. To get the actual flag, we must remove the newlines using the `tr` command. If done correctly, this will give us the correct flag.

#### Commands run: 

```sh
$ /challenge/run | tr -d "\n"
```

## Flag: 

```
pwn.college{sQeDvh2ONUOBSucT-DV4iVsIk9L.0VNxEzNxwSOxAzNzEzW}
```

# Challenge 4: Extracting the first lines with head

In your Linux journey, you'll experience situations where you need to grab just the early output of very verbose programs.
For this, you'll reach for `head`!
The `head` command is used to display the first few lines of its input:

```sh
hacker@dojo:~$ cat /something/very/long | head
this
is
just
the
first
ten
lines
of
the
file
hacker@dojo:~$
```

By default, it shows the first 10 lines, but you can control this with the `-n` option:

```sh
hacker@dojo:~$ cat /something/very/long | head -n 2
this
is
hacker@dojo:~$
```

This challenge's `/challenge/pwn` outputs a bunch of data, and you'll need to pipe it through `head` to grab just the first 7 lines and then pipe them onwards to `/challenge/college`, which will give you the flag if you do this right!
Your solution will be a long composite command with _two_ pipes connecting three commands. Good luck!

## Solution:

In this challenge, we must use the `head` command to grab the first 7 lines of the output of `/challenge/pwn`. Then, we must pipe into `/challenge/college` to get the flag.

#### Commands run: 

```sh
$ /challenge/pwn | head -n 7 | /challenge/college 
```

## Flag: 

```
pwn.college{APbno5V8Nm0VmCVw6oJ-w48NXWL.0lNxEzNxwSOxAzNzEzW}
```

# Challenge 5: Extracting specific sections of text

Sometimes, you want to grab specific columns of data, such as the first column, the third column, or the 42nd column.
For this, there's the `cut` command.

For example, imagine that you have the following data file:

```sh
hacker@dojo:~$ cat scores.txt
hacker 78 99 67
root 92 43 89
hacker@dojo:~$
```

You could use `cut` to extract specific columns:

```sh
hacker@dojo:~$ cut -d " " -f 1 scores.txt
hacker
root
hacker@dojo:~$ cut -d " " -f 2 scores.txt
78
92
hacker@dojo:~$ cut -d " " -f 3 scores.txt
99
43
hacker@dojo:~$
```

The `-d` argument specifies the column _delimiter_ (how columns are separated).
In this case, it's a space character.
Of course, it has to be in quotes here so that the shell knows that the space is an argument rather than a space separating other arguments!
The `-f` argument specifies the _field_ number (which column to extract).

In this challenge, the `/challenge/run` program will give you a bunch of lines with random numbers and single characters (characters of the flag) as columns.
Use `cut` to extract the flag characters, then pipe them to `tr -d "\n"` (like the previous level!) to join them together into a single line.
Your solution will look something like `/challenge/run | cut ??? | tr ???`, with the `???` filled out.

## Solution:

The `/challenge/run` program in this challenge will print out a bunch of lines with random numbers and single characters (characters of the flag) as columns. We must use the `cut` command to extract the 2nd collumn containing the characters of the flag and the pipe it int the `tr` command to remove all the newlines. This will give us the actual flag.

#### Commands run: 

```sh
$ /challenge/run | cut -d " " -f 2 | tr -d "\n"
```

## Flag: 

```
pwn.college{U2OqcZGd78xoI6uIr3iudvwjpW0.01NxEzNxwSOxAzNzEzW}
```

# Challenge 6: Sorting data

Files (or output lines of commands) aren't always in the order you need them!
The `sort` command helps you organize data.
It reads lines from input (or files) and outputs them in sorted order:

```sh
hacker@dojo:~$ cat names.txt
  hack
  the
  planet
  with
  pwn
  college
hacker@dojo:~$ sort names.txt
  college
  hack
  planet
  pwn
  the
  with
hacker@dojo:~$
```

By default, `sort` orders lines alphabetically.
Arguments can change this:

- `-r`: reverse order (Z to A)
- `-n`: numeric sort (for numbers)
- `-u`: unique lines only (remove duplicates)
- `-R`: random order!

In this challenge, there's a file at `/challenge/flags.txt` containing 100 fake flags, with the real flag mixed among them.
When sorted alphabetically, the real flag will be at the end (we made sure of this when generating fake flags).
Go get it!

## Solution:

In this challenge, `/challenge/flags.txt` contains a bunch of fake flags of which, only one is correct. The fake flags have been made in such a way that the real flag will be at the end when the file is sorted. For this, we can use the `sort` command.

#### Commands run: 

```sh
$ sort /challenge/flags.txt 
```

## Flag: 

```
pwn.college{YXFKVoT8nx1pdZxKnVXPzzDb1Yc.0FM0MDOxwSOxAzNzEzW}
```
