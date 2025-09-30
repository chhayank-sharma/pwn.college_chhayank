
# Challenge 1: Redirecting output

First, let's look at redirecting stdout to files.
You can accomplish this with the `>` character, as so:

```sh
hacker@dojo:~$ echo hi > asdf
```

This will redirect the output of `echo hi` (which will be `hi`) to the file `asdf`.
You can then use a program such as `cat` to output this file:

```sh
hacker@dojo:~$ cat asdf
hi
```

In this challenge, you must use this output redirection to write the word `PWN` (all uppercase) to the filename `COLLEGE` (all uppercase).

## Solution:

After the terminal comes up, the user needs to use output redirection using `>` to write the text `PWN` to a file `COLLEGE` in the home directory. To do this, the `echo` command will be used and its output will be written into the file. This will print the flag.

#### Commands run: 

```sh
$ echo PWN > COLLEGE
```

## Flag: 

```
pwn.college{cAFNqGo0AsAcEYOWrB-60CdSbw2.QX0YTN0wSOxAzNzEzW}
```

# Challenge 2: Redirecting more output

Aside from redirecting the output of `echo`, you can, of course, redirect the output of any command.
In this level, `/challenge/run` will once more give you a flag, but _only_ if you redirect its output to the file `myflag`.
Your flag will, of course, end up in the `myflag` file!

You'll notice that `/challenge/run` will still happily print to your terminal, despite you redirecting stdout.
That's because it communicates its instructions and feedback over standard error, and only prints the flag over standard out!

## Solution:

After the terminal comes up, the user needs to use output redirection through `>` to write the output of the `/challenge/run` program to a file `myflag` in the home directory. Then, the file can be simply read using the `cat` command to capture the flag.

#### Commands run: 

```sh
$ /challenge/run > myflag
$ cat myflag
```

## Flag: 

```
pwn.college{IxCIGIrmuZk6qXRkGoBaSxMxKHO.QX1YTN0wSOxAzNzEzW}
```

# Challenge 3: Appending output

A common use-case of output redirection is to save off some command results for later analysis.
Often times, you want to do this in _aggregate_: run a bunch of commands, save their output, and `grep` through it later.
In this case, you might want all that output to keep appending to the same file, but `>` will create a new output file every time, deleting the old contents.

You can redirect input in _append_ mode using `>>` instead of `>`, as so:

```sh
hacker@dojo:~$ echo pwn > outfile
hacker@dojo:~$ echo college >> outfile
hacker@dojo:~$ cat outfile
pwn
college
hacker@dojo:$
```

To practice, run `/challenge/run` with an append-mode redirect of the output to the file `/home/hacker/the-flag`.
The practice will write the first half of the flag to the file, and the second half to `stdout` if `stdout` is redirected to the file.
If you properly redirect in append-mode, the second half will be appended to the first, but if you redirect in _truncation_ mode (`>`), the second half will _overwrite_ the first and you won't get the flag!

Go for it now!

## Solution:

In this challenge, the `/challenge/run` program will write the flag in two stages. It will write the first part directly to the file. Then, it will write the second part to the stdout. To get the flag, you need to redirect stdout to the file `the-flag` in the home directory in append mode using `>>` instead of `>`. If append mode is not used, the first part will be overwritten and the flag will not be captured.

#### Commands run: 

```sh
$ /challenge/run >> the-flag
$ cat the-flag
 | 
\|/ This is the first half:
 v 
pwn.college{M_-k_wmkS7E2y3736E0NwO2ICsG.QX3ATO0wSOxAzNzEzW}
                              ^
     that is the second half /|\
                              |
```

## Flag: 

```
pwn.college{M_-k_wmkS7E2y3736E0NwO2ICsG.QX3ATO0wSOxAzNzEzW}
```

# Challenge 4: Redirecting errors

Just like standard output, you can also redirect the error channel of commands.
Here, we'll learn about *File Descriptor numbers*.
A File Descriptor (FD) is a number that *describes* a communication channel in Linux.
You've already been using them, even though you didn't realize it.
We're already familiar with three:

- FD 0: Standard Input
- FD 1: Standard Output
- FD 2: Standard Error

When you redirect process communication, you do it by FD number, though some FD numbers are implicit.
For example, a `>` without a number implies `1>`, which redirects FD 1 (Standard Output).
Thus, the following two commands are equivalent:

```sh
hacker@dojo:~$ echo hi > asdf
hacker@dojo:~$ echo hi 1> asdf
```

Redirecting errors is pretty easy from this point.
If you have a command that might produce data via standard error (such as `/challenge/run`), you can do:

```sh
hacker@dojo:~$ /challenge/run 2> errors.log
```

That will redirect standard error (FD 2) to the `errors.log` file.
Furthermore, you can redirect multiple file descriptors at the same time!
For example:

```sh
hacker@dojo:~$ some_command > output.log 2> errors.log
```

That command will redirect output to `output.log` and errors to `errors.log`.

Let's put this into practice!
In this challenge, you will need to redirect the output of `/challenge/run`, like before, to `myflag`, and the "errors" (in our case, the instructions) to `instructions`.
You'll notice that nothing will be printed to the terminal, because you have redirected everything!
You can find the instructions/feedback in `instructions` and the flag in `myflag` when you successfully pull this off!

## Solution:

In this challenge, we have been given the task of redirecting the `sdout` and `sterr` of the program `/challenge/run` to two files `myflag` and `instructions` in the home directory using a single command. We can do this using `1>` and `2>` where `1>` will be used to redirect `stdout` and `2>` will be used to redirect `stderr`. The flag will then be stored in the `myflag` file and can be simply captured.

#### Commands run: 

```sh
$ /challenge/run  1>  myflag 2>  instructions
$ cat instructions 
[INFO] WELCOME! This challenge makes the following asks of you:
[INFO] - the challenge will check that output is redirected to a specific file path : myflag
[INFO] - the challenge will check that error output is redirected to a specific file path : instructions
[INFO] - the challenge will output a reward file if all the tests pass : /flag

[HYPE] ONWARDS TO GREATNESS!

[INFO] This challenge will perform a bunch of checks.
[INFO] If you pass these checks, you will receive the /flag file.

[TEST] You should have redirected my stdout to a file called myflag. Checking...

[PASS] The file at the other end of my stdout looks okay!

[TEST] You should have redirected my stderr to instructions. Checking...

[PASS] The file at the other end of my stderr looks okay!
[PASS] Success! You have satisfied all execution requirements.
$ cat myflag
```

## Flag: 

```
pwn.college{cNbcMVYr0Qu3_PnWo6vuwAGVNg3.QX3YTN0wSOxAzNzEzW}
```

# Challenge 5: Redirecting input

Just like you can redirect _output_ from programs, you can redirect input _to_ programs!
This is done using `<`, as so:

```sh
hacker@dojo:~$ echo yo > message
hacker@dojo:~$ cat message
yo
hacker@dojo:~$ rev < message
oy
```

You can do interesting things with a lot of different programs using input redirection!
In this level, we will practice using `/challenge/run`, which will require you to redirect the `PWN` file to it and have the `PWN` file contain the value `COLLEGE`!
To write that value to the `PWN` file, recall the prior challenge on output redirection from `echo`!

## Solution:

After the terminal comes up, the user needs to store `COLLEGE` into a file `PWN` in the home directory using output redirection on the `echo` command. Then, the contents of the `PWN` file must be passed as input to the `/challenge/run` program. This can be done using input redirection with the help of `<`. This will then print the flag.

#### Commands run: 

```sh
$ echo COLLEGE > PWN
$ /challenge/run < PWN
```

## Flag: 

```
pwn.college{oFfMNADiHdEWcXTpdh8ifquX8mT.QXwcTN0wSOxAzNzEzW}
```

# Challenge 6: Grepping stored results

You know how to run commands, how to redirect their output (e.g., `>`), and how to search through the resulting file (e.g., `grep`).
Let's put this together!

In preparation for more complex levels, we want you to:

1. Redirect the output of `/challenge/run` to `/tmp/data.txt`.
2. This will result in a hundred thousand lines of text, with one of them being the flag, in `/tmp/data.txt`.
3. `grep` that for the flag!

## Solution:

After the terminal comes up, the user needs to use output redirection to store the output of `/challenge/run` into a file `/tmp/data.txt`. This will cause alot of data being written into that file, including the flag. We can now use `grep` to capture the flag.

#### Commands run: 

```sh
$ /challenge/run > /tmp/data.txt
$ grep pwn.college /tmp/data.txt
```

## Flag: 

```
pwn.college{kHqE_i2U48vCIv3DjBrn7qKudID.QX4EDO0wSOxAzNzEzW}
```

# Challenge 7: Grepping live output

It turns out that you can "cut out the middleman" and avoid the need to store results to a file, like you did in the last level.
You can do this by using the `|` (pipe) operator.
Standard output from the command to the left of the pipe will be connected to (_piped into_) the standard input of the command to the right of the pipe.
For example:

```sh
hacker@dojo:~$ echo no-no | grep yes
hacker@dojo:~$ echo yes-yes | grep yes
yes-yes
hacker@dojo:~$ echo yes-yes | grep no
hacker@dojo:~$ echo no-no | grep no
no-no
```

Now try it for yourself! `/challenge/run` will output a hundred thousand lines of text, including the flag.
`grep` for the flag!

## Solution:

After the terminal comes up, the user needs to 

#### Commands run: 

```sh
$ /challenge/run | grep pwn.college
```

## Flag: 

```
pwn.college{w-sRI7FQ9KNMrvVP6_lddrOSv5L.QX5EDO0wSOxAzNzEzW}
```

# Challenge 8: Grepping errors

You know how to redirect errors to a file, and you know how to pipe output to another program, such as `grep`.
But what if you wanted to `grep` through errors directly?

The `>` operator redirects a given file descriptor to a file, and you've used `2>` to redirect fd 2, which is standard error.
The `|` operator redirects _only standard output_ to another program, and there is no `2|` form of the operator!
It can _only_ redirect standard output (file descriptor 1).

Luckily, where there's a shell, there's a way!

The shell has a `>&` operator, which redirects a file descriptor _to another file descriptor_.
This means that we can have a two-step process to `grep` through errors: first, we redirect standard error to standard output (`2>& 1`) and then pipe the now-combined stderr and stdout as normal (`|`)!

Try it now!
Like the last level, this level will overwhelm you with output, but this time on standard error.
`grep` through it to find the flag!

## Solution:

In this challenge, the user will need to grep through the `stderr` of the output of the `/challenge/run` program to get the flag. Here, this is achieved using `2>&1` which will basically pipe the `stderr` to the `stdout` and then pipe the now combined `stdout` to whatever is on the right. However, it should be kept in mind that this will cause `stdout` and `stderr` to be mixed together. Doing this properly will cause the flag to be printed.

#### Commands run: 

```sh
$ /challenge/run 2>&1 | grep pwn.college
```

## Flag: 

```
pwn.college{ACm3YzipVHwPCZ7TM9DGKBHf-zd.QX1ATO0wSOxAzNzEzW}
```

# Challenge 9: Filtering with grep -v

The `grep` command has a very useful option: `-v` (invert match).
While normal `grep` shows lines that MATCH a pattern, `grep -v` shows lines that do NOT match a pattern:

```sh
hacker@dojo:~$ cat data.txt
hello hackers!
hello world!
hacker@dojo:~$ cat data.txt | grep -v world
hello hackers!
hacker@dojo:~$
```

Sometimes, the only way to filter to just the data you want is to filter _out_ the data you _don't_ want.
In this challenge, `/challenge/run` will output the flag to stdout, but it will also output over 1000 decoy flags (containing the word `DECOY` somewhere in the flag) mixed in with the real flag.
You'll need to filter _out_ the decoys while keeping the real flag!

Use `grep -v` to filter out all the lines containing "DECOY" and reveal the real flag!

## Solution:

In this challenge, the `/challenge/run` program will output the flag with 1000's of decoy flags to its `stdout`. To get the real flag, we need to filter out the decoy flags using `grep -v`. The decoy flags will all contain the text `DECOY`. If done correctly, it should print the flag.

#### Commands run: 

```sh
$ /challenge/run | grep -v DECOY
```

## Flag: 

```
pwn.college{QvjdYaHEMvGx170FpV8pwViXb3o.0FOxEzNxwSOxAzNzEzW}
```

# Challenge 10: Duplicating piped data with tee

When you pipe data from one command to another, you of course no longer see it on your screen.
This is not always desired: for example, you might want to see the data as it flows through between your commands to debug unintended outcomes (e.g., "why did that second command not work???").

Luckily, there is a solution!
The `tee` command, named after a "T-splitter" from _plumbing_ pipes, duplicates data flowing through your pipes to any number of files provided on the command line.
For example:

```sh
hacker@dojo:~$ echo hi | tee pwn college
hi
hacker@dojo:~$ cat pwn
hi
hacker@dojo:~$ cat college
hi
hacker@dojo:~$
```

As you can see, by providing two files to `tee`, we ended up with three copies of the piped-in data: one to stdout, one to the `pwn` file, and one to the `college` file.
You can imagine how you might use this to debug things going haywire:

```sh
hacker@dojo:~$ command_1 | command_2
Command 2 failed!
hacker@dojo:~$ command_1 | tee cmd1_output | command_2
Command 2 failed!
hacker@dojo:~$ cat cmd1_output
Command 1 failed: must pass --succeed!
hacker@dojo:~$ command_1 --succeed | command_2
Commands succeeded!
```

Now, you try it!
This process' `/challenge/pwn` must be piped into `/challenge/college`, but you'll need to intercept the data to see what `pwn` needs from you!

## Solution:

In this challenge, the user needs to pipe the output of `/challenge/pwn` into the `/challenge/college` program, but, doing so will make it so that the output of `/challenge/pwn` will not be visible to the user. `/challenge/pwn` acrually requires a secret argument to print the flag to the screen. So, to find the secret argument, we must use the `tee` command to pipe the output into a file `pwnout` which can be read afterwards using `cat` to find the secret argument. Then, `/challenge/pwn` can be run with the secret argument and piped into `/challenge/college` which will print the flag.

#### Commands run: 

```sh
$ /challenge/pwn | tee pwnout | /challenge/college
Processing...
The input to 'college' does not contain the correct secret code! This code 
should be provided by the 'pwn' command. HINT: use 'tee' to intercept the 
output of 'pwn' and figure out what the code needs to be.
$ cat pwnout 
Usage: /challenge/pwn --secret [SECRET_ARG]

SECRET_ARG should be "4YrwZHY4"
$ /challenge/pwn --secret 4YrwZHY4 | /challenge/college
```

## Flag: 

```
pwn.college{4YrwZHY47C7Xc8q733Hs9c0r5uR.QXxITO0wSOxAzNzEzW}
```

# Challenge 11: Process substitution for input

Sometimes you need to compare the output of two commands rather than two files.
You might think to save each output to a file first:

```sh
hacker@dojo:~$ command1 > file1
hacker@dojo:~$ command2 > file2
hacker@dojo:~$ diff file1 file2
```

But there's a more elegant way! Linux follows the philosophy that ["everything is a file"](https://en.wikipedia.org/wiki/Everything_is_a_file).
That is, the system strives to provide file-like access to most resources, including the input and output of running programs!
The shell follows this philosophy, allowing you to, for example, use any utility that takes file arguments on the command line and hook it up to the output of programs, as you learned in the previous few levels.

Interestingly, we can go further, and hook input and output of programs to _arguments_ of commands.
This is done using [Process Substitution](https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html).
For reading from a command (input process substitution), use `<(command)`.
When you write `<(command)`, bash will run the command and hook up its output to a temporary file that it will create.
This isn't a _real_ file, of course, it's what's called a _named pipe_, in that it has a file name:

```sh
hacker@dojo:~$ echo <(echo hi)
/dev/fd/63
hacker@dojo:~$
```

Where did `/dev/fd/63` come from?
`bash` replaced `<(echo hi)` with the path of the named pipe file that's hooked up to the command's output!
While the command is running, reading from this file will read data from the standard output of the command.
Typically, this is done using commands that take input files as arguments:

```sh
hacker@dojo:~$ cat <(echo hi)
hi
hacker@dojo:~$
```

Of course, you can specify this multiple times:

```sh
hacker@dojo:~$ echo <(echo pwn) <(echo college)
/dev/fd/63 /dev/fd/64
hacker@dojo:~$ cat <(echo pwn) <(echo college)
pwn
college
hacker@dojo:~$
```

Now for your challenge!
Recall what you learned in the `diff` challenge from [Comprehending Commands](/linux-luminarium/commands).
In that challenge, you diffed two files.
Now, you'll diff two sets of command outputs: `/challenge/print_decoys`, which will print a bunch of decoy flags, and `/challenge/print_decoys_and_flag` which will print those same decoys plus the real flag.

Use process substitution with `diff` to compare the outputs of these two programs and find your flag!

## Solution:

In this challenge, we need to use the `diff` command to compare the outputs of the two programs `/challenge/print_decoys` and `/challenge/print_decoys_and_flag` to get the flag. To do this, input process substitution must be done using `<(command)`. This will pipe the output of the command as an argument without having to make an intermediate file. Doing this correctly will print the flag to the screen.

#### Commands run: 

```sh
$ diff <(/challenge/print_decoys) <(/challenge/print_decoys_and_flag)
```

## Flag: 

```
pwn.college{kurIRrruSGmpKRgXSdcZJcBIjeV.0lNwMDOxwSOxAzNzEzW}
```

# Challenge 12: Writing to multiple programs

Now you've learned that process substitution can make command output appear as files for reading with `<(command)`.
But you can also use process substitution for _writing_ to commands!

You can duplicate data to two files with `tee`:

```sh
hacker@dojo:~$ echo HACK | tee THE > PLANET
hacker@dojo:~$ cat THE
HACK
hacker@dojo:~$ cat PLANET
HACK
hacker@dojo:~$
```

And you've used `tee` to duplicate data to a file and a command:

```sh
hacker@dojo:~$ echo HACK | tee THE | cat
HACK
hacker@dojo:~$ cat THE
HACK
hacker@dojo:~$
```

But what about duplicating to two commands?
As `tee` says in its manpage, it's designed to write to files and to standard output:

```text
TEE(1)                           User Commands                          TEE(1)

NAME
       tee - read from standard input and write to standard output and files
```

But wait! You just learned that bash can make commands look like files using process substitution!
For writing to a command (output process substitution), use `>(command)`.
If you write an argument of `>(rev)`, bash will run the `rev` command (this command reads data from standard input, reverses its order, and writes it to standard output!), but hook up its input to a temporary named pipe file.
When commands write to this file, the data goes to the standard input of the command:

```sh
hacker@dojo:~$ echo HACK | rev
KCAH
hacker@dojo:~$ echo HACK | tee >(rev)
HACK
KCAH
```

Above, the following sequence of events took place:

1. `bash` started up the `rev` command, hooking a named pipe (presumably `/dev/fd/63`) to `rev`'s standard input
2. `bash` started up the `tee` command, hooking a pipe to its standard input, and replacing the first argument to `tee` with `/dev/fd/63`. `tee` never even saw the argument `>(rev)`; the shell _substituted_ it before launching `tee`
3. `bash` used the `echo` builtin to print `HACK` into `tee`'s standard input
4. `tee` read `HACK`, wrote it to standard output, and then wrote it to `/dev/fd/63` (which is connected to `rev`'s stdin)
5. `rev` read `HACK` from its standard input, reversed it, and wrote `KCAH` to standard output

Now it's your turn!
In this challenge, we have `/challenge/hack`, `/challenge/the`, and `/challenge/planet`.
Run the `/challenge/hack` command, and duplicate its output as input to both the `/challenge/the` and the `/challenge/planet` commands!
Scroll back through the previous challenges "Duplicating piped data with tee" and "Process substitution for input" if you need a refresher on this method.

----
**Trivia!**

The observant learner will realize that the following are equivalent:

```sh
hacker@dojo:~$ echo hi | rev
ih
hacker@dojo:~$ echo hi > >(rev)
ih
hacker@dojo:~$
```

More than one way to pipe data!
Of course, the second route is way harder to read and also harder to expand.
For example:

```sh
hacker@dojo:~$ echo hi | rev | rev
hi
hacker@dojo:~$ echo hi > >(rev | rev)
hi
hacker@dojo:~$
```

That's just silly!
The lesson here is that, while Process Substitution is a powerful tool in your toolbox, it's a very _specialized_ tool; don't use it for everything!

## Solution:

In this challenge, the aim is to use process substitution to write to 2 different programs at the same time. This can be achieved using the `tee` command to split the output of `/challenge/hack` and then using output process substitution using `>(/challenge/the)` to send the `tee`'d output into `/challenge/the` and it can then be normally piped into `/challenge/planet`. Doing this properly will print the flag to the terminal.

#### Commands run: 

```sh
$ /challenge/hack | tee >(/challenge/the) | /challenge/planet
```

## Flag: 

```
pwn.college{M_t6kbuRq85ZbrWE6fEbHlJFZny.QXwgDN1wSOxAzNzEzW}
```

# Challenge 13: Split-piping stderr and stdout

Now, let's put your knowledge together.
You must master the ultimate piping task: redirect stdout to one program and stderr to another.

The challenge here, of course, is that the `|` operator links the _stdout_ of the left command with the _stdin_ of the right command.
Of course, you've used `2>&1` to redirect stderr into stdout and, thus, pipe stderr over, but this then mixes stderr and stdout.
How to keep it unmixed?

You will need to combine your knowledge of `>()`, `2>`, and `|`.
How to do it is a task I'll leave to you.

In this challenge, you have:

- `/challenge/hack`: this produces data on _stdout_ and _stderr_
- `/challenge/the`: you must redirect `hack`'s _stderr_ to this program
- `/challenge/planet`: you must redirect `hack`'s _stdout_ to this program

Go get the flag!

## Solution:

Holy fucking shit this was hard. Lets break down the solution. Our aim in this challenge is to redirect the `stderr` outputed by `/challenge/hack` to `/challenge/the` and redirect the `stdout` outputed by `/challenge/hack` to `/challenge/planet` in just one command. To do this, we must combine everything that we have learned in the previous challenges. Lets go over it once again, the `>` is used to redirect the output of the command on the left to a file on the right. By default, it is set to `1>` which uses the `stdout` of the previous output but if we use `2>`, we can redirect the `stderr` instead. However, it must be kept in mind that this will only just output to a file. To redirect a command, normally we use `|`. However, there is no such thing as `2|`. So, either we must use `2>&1` to add the `stderr` to `stdout` or we must do `2> >`. We cannot do the first option because that will cause the `stderr` and `stdout` to get mixed so we must do `/challenge/hack 2> >(/challenge/the)` to pipe the `stderr` into `/challenge/the`. Then, we can use the normal `|`(or if you so wish, `> >`) to pipe the `stdout` into `/challenge/planet`. After doing all this, the flag should print to the terminal and can be captured and the final command will look like `/challenge/hack 2> >(/challenge/the) | /challenge/planet`.

Now heres a curveball, we can also rewrite this as `/challenge/hack > >(/challenge/planet) 2> >(/challenge/the)` but not `/challenge/hack | /challenge/planet 2> >(/challenge/the)`. This is because although `|` and `> >` are similar in most cases, they are not actually equivalent. The first one works roughly similar to what we did in `challenge 4` where both the redirectors work on the output of `/challenge/hack`. But, in the second one, the `|` only connects `stdout` of `/challenge/hack` to `/challenge/planet`, and `2> >(/challenge/the)` actually redirects `stderr` of `/challenge/planet`, **not** `/challenge/hack`.

#### Commands run: 

```sh
$ /challenge/hack 2> >(/challenge/the) | /challenge/planet
```

## Flag: 

```
pwn.college{EVvaSqOi-V8Keu1bcqCsWMqdNet.QXxQDM2wSOxAzNzEzW}
```

# Challenge 14: Named pipes

You've learned about pipes using `|`, and you've seen that process substitution creates temporary named pipes (like `/dev/fd/63`).
You can also create your own _persistent_ named pipes that stick around on the filesystem!
These are called **FIFOs**, which stands for First (byte) In, First (byte) Out.

You create a FIFO using the `mkfifo` command:

```sh
hacker@dojo:~$ mkfifo my_pipe
hacker@dojo:~$ ls -l my_pipe
prw-r--r-- 1 hacker hacker 0 Jan 1 12:00 my_pipe
-rw-r--r-- 1 hacker hacker 0 Jan 1 12:00 some_file
hacker@dojo:~$
```

Notice the `p` at the beginning of the permissions - that indicates it's a pipe!
That's markedly different than the `-` that's at the beginning of normal files, such as `some_file` in the above example.

Unlike the automatic named pipes from process substitution:

- You control where FIFOs are created
- They persist until you delete them  
- Any process can write to them by path (e.g., `echo hi > my_pipe`)
- You can see them with `ls` and examine them like files

One problem with FIFOs is that they'll "block" any operations on them until both the read side of the pipe and the write side of the pipe are ready.
For example, consider this:

```sh
hacker@dojo:~$ mkfifo myfifo
hacker@dojo:~$ echo pwn > myfifo
```

To service `echo pwn > myfifo`, bash will open the `myfifo` file in write mode.
However, this operation will hang until something _also_ opens the file in read mode (thus completing the pipe).
That can be in a different sh:

```sh
hacker@dojo:~$ cat myfifo
pwn
hacker@dojo:~$
```

What happened here?
When we ran `cat myfifo`, the pipe had both sides of the connection all set, and _unblocked_, allowing `echo pwn > myfifo` to run, which sent `pwn` into the pipe, where it was read by `cat`.

Of course, this can somewhat be done by normal files: you've learned how to `echo` stuff into them and `cat` them out.
Why use a FIFO instead?
Here are key differences:

1. **No disk storage:** FIFOs pass data directly between processes in memory - nothing is saved to disk
2. **Ephemeral data:** Once data is read from a FIFO, it's gone (unlike files where data persists)
3. **Automatic synchronization:** Writers block until the readers are ready, and vice-versa. This is actually useful! It provides automatic synchronization. Consider the example above: with a FIFO, it doesn't matter if `cat myfifo` or `echo pwn > myfifo` is executed first; each would just wait for the other. With files, you need to make sure to execute the writer before the reader.
4. **Complex data flows:** FIFOs are useful for facilitating complex data flows, merging and splitting data in flexible ways, and so on. For example, FIFOs support multiple readers and writers.

This challenge will be a simple introduction to FIFOs.
You'll need to create a `/tmp/flag_fifo` file and redirect the stdout of `/challenge/run` to it.
If you're successful, `/challenge/run` will write the flag into the FIFO!
Go do it!

----
**HINT:**
The blocking behavior of FIFOs makes it hard to solve this challenge in a single terminal.
You may want to use the Desktop or VSCode mode for this challenge so that you can launch two terminals.

## Solution:

This challenge will require two terminals to be accessible at the same time. For this, one can either use the Desktop or VSCode mode on the pwn.college website. Or, to do it from within the terminal, it is possible to use the `tmux` program. `tmux` is a **t**erminal **mu**ltiple**x**er which allows for running commands in parallel without acess to multiple terminal interfaces. To do it in this manner, simply enter the `tmux` command. This should open a tmux pane within the terminal. Then, to split it into two, press and release the prefix key, which is `Ctrl+b` by default. Then, press `"` to create a new pane horizontally or press `%` to create a new pane vertically. To move between the panes, use the prefix key (`Ctrl+b`) followed by the corresponding arrow key (`Up`, `Down`, `Left`, `Right`).

To solve the challenge, the user must first create a named pipe `/tmp/flag_fifo` using the `mkfifo` command. Then, the output of the `/challenge/run` program can be redirected into it. From a different terminal, running `cat /tmp/flag_fifo` will print the flag to that terminal.

#### Commands run: 

Terminal 1:
```sh
$ mkfifo /tmp/flag_fifo
$ /challenge/run > /tmp/flag_fifo
```
Terminal 2:
```sh
$ cat /tmp/flag_fifo
```

## Flag: 

```
pwn.college{k-DkoYy_iKw_z6uGmo71rPmc-_E.01MzMDOxwSOxAzNzEzW}
```
