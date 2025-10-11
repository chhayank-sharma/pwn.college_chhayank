
# Challenge 1: Chaining with Semicolons

The easiest way to chain commands is `;`.
In most contexts, `;` separates commands in a similar way to how Enter separates lines.
So, this:

```console
hacker@dojo:~$ echo COLLEGE > pwn
hacker@dojo:~$ cat pwn
COLLEGE
hacker@dojo:~$
```

Is roughly the same as this:

```console
hacker@dojo:~$ echo COLLEGE > pwn; cat pwn
COLLEGE
hacker@dojo:~$
```

Basically, when you hit Enter, your shell executes your typed command and, after that command terminates, gives you the prompt to input another command.
The semicolon is analogous, just without the prompt and with you entering both commands before anything is executed.

Give it a try now! In this level, you must run `/challenge/pwn` and then `/challenge/college`, chaining them with a semicolon.

## Solution:

In this challenge, we need to run `/challenge/pwn` and `/challenge/college` using just one command by using a `;` to seperate them. This will print the flag to the terminal.

#### Commands run: 

```sh
$ /challenge/pwn; /challenge/college
```

## Flag: 

```
pwn.college{k-m32JH0YOSW7rF17WYsbCL24EQ.QX1UDO0wSOxAzNzEzW}
```

# Challenge 2: Building on Success

You learned about exit codes in the [Processes](https://pwn.college/linux-luminarium/processes/) module.
Now let's use them to chain commands together!

The `&&` operator allows you to run a second command only if the first command succeeds (in Linux convention, this means it exited with code 0).
This is called the "AND" operator because both conditions must be true: the first command must succeed AND then the second command will run.
That's super useful for complex commandline workflows where certain actions depend on the success of other actions.

Here's the syntax:
```console
hacker@dojo:~$ command1 && command2
```

This means: "Run command1, and IF it succeeds, then run command2."

Some examples:

```console
hacker@dojo:~$ touch /home/hacker/file && echo "this will run"
success
this will run
hacker@dojo:~$ touch /file && echo "this will NOT run"
touch: cannot touch '/file': Permission denied
hacker@dojo:~$
```

That second invocation of `touch` failed because the hacker user does not have write access to `/file`, so the `echo` did not run.

In this challenge, you need to chain the programs `/challenge/first-success` and `/challenge/second` using the `&&` operator. 
Try running each command separately first to see what happens (which is that you will _not_ get the flag).
But if you chain them with `&&`, the flag will appear!

## Solution:

In this challenge, we need to run `/challenge/first-success` and `/challenge/second` using just one command. To do this, we must use `&&` to seperate them which will only run the second command if the first one succeeds. This will print the flag to the terminal.

#### Commands run: 

```sh
$ /challenge/first-success && /challenge/second 
```

## Flag: 

```
pwn.college{oHExTDztb6ScrYxULbUk4htk8qS.0lM0MDOxwSOxAzNzEzW}
```

# Challenge 3: Handling Failure

You just learned about the `&&` operator, which runs the second command only if the first succeeds.
Now let's learn about its opposite: the `||` operator allows you to run a second command only if the first command fails (exits with a non-zero code).
This is called the "OR" operator because either the first command succeeds OR the second command will run.

Here's the syntax:
```console
hacker@dojo:~$ command1 || command2
```

This means: "Run command1, and IF it fails, then run command2."

Some examples:
```console
hacker@dojo:~$ touch /file || echo "touch failed, so this runs"
touch: cannot touch '/file': Permission denied
touch failed, so this runs
hacker@dojo:~$ touch /home/hacker/file || echo "this will NOT run"
hacker@dojo:~$
```

The `||` operator is super useful for providing fallback commands or error handling!

In this challenge, you need to chain `/challenge/first-failure` and `/challenge/second` using the `||` operator.
Go for it!

## Solution:

In this challenge, we need to run `/challenge/first-failure` and `/challenge/second` using just one command. To do this, we must use `||` to seperate them which will only run the second command if the first one fails. This will print the flag to the terminal.

#### Commands run: 

```sh
$ /challenge/first-failure || /challenge/second 
```

## Flag: 

```
pwn.college{gi0QyrnjqPXaXZAf6eD1Wg_JURk.01M0MDOxwSOxAzNzEzW}
```

# Challenge 4: Your First Shell Script

As you combine more and more commands to achieve complex effects, the length of the combined prompt quickly gets really annoying to deal with.
When this happens, you can put these commands in a file, called a _shell script_, and run them by executing the file!
For example, consider our semicolon technique:

```console
hacker@dojo:~$ echo COLLEGE > pwn; cat pwn
COLLEGE
hacker@dojo:~$
```

We can create a shell script called `pwn.sh` (by convention, shell scripts are frequently named with a `sh` suffix):

```sh
echo COLLEGE > pwn
cat pwn
```

And then we can execute by passing it as an argument to a new instance of our shell (`bash`)!
When a shell is invoked like this, rather than taking commands from the user, it reads commands from the file.

```console
hacker@dojo:~$ ls
hacker@dojo:~$ bash pwn.sh
COLLEGE
hacker@dojo:~$ ls
pwn
hacker@dojo:~$
```

You can see that the shell script executed both commands, creating and printing the `pwn` file.

Now, it's your turn!
Same as last level, run `/challenge/pwn` and then `/challenge/college`, but this time in a shell script called `x.sh`, then run it with `bash`!

---
**NOTE:** We haven't yet talked about Linux's amazing array of competent command line file editors.
For now, feel free to use the `Text Editor` application in Desktop mode (`Applications->Accessories->Text Editor`) or the default editor in the VSCode Workspace!

## Solution:

In this challenge, similar to the first challenge, we need to run `/challenge/pwn` and `/challenge/college`. However, this time we must use a shell script `x.sh` to do this. If done properly, it should give us the flag.

#### Commands run: 

```sh
$ echo "/challenge/pwn" > x.sh
$ echo "/challenge/college" >> x.sh
$ cat x.sh
/challenge/pwn
/challenge/college

$ bash x.sh
```

## Flag: 

```
pwn.college{0cgmARUJ9fEdtJSxQsW_PqoJm4E.QXxcDO0wSOxAzNzEzW}
```

# Challenge 5: Redirecting Script Output

Let's try something a bit trickier!
You've piped output between programs with `|`, but so far, this has just been between one command's output and a different command's input.
But what if you wanted to send the output of several programs to one command?
There are a few ways to do this, and we'll explore a simple one here: redirecting output from your script!

As far as the shell is concerned, your script is just another command.
That means you can redirect its input and output just like you did for commands in the [Piping](/linux-luminarium/piping) module!
For example, you can write it to a file:

```console
hacker@dojo:~$ cat script.sh
echo PWN
echo COLLEGE
hacker@dojo:~$ bash script.sh > output
hacker@dojo:~$ cat output
PWN
COLLEGE
hacker@dojo:~$
```

All of the various redirection methods work: `>` for stdout, `2>` for stderr, `<` for stdin, `>>` and `2>>` for append-mode redirection, `>&` for redirecting to other file descriptors, and `|` for piping to another command.

In this level, we will practice piping (`|`) from your script to another program.
Like before, you need to create a script that calls the `/challenge/pwn` command followed by the `/challenge/college` command, and pipe the output of the script into a single invocation of the `/challenge/solve` command!

## Solution:

In this challenge, similar to the last challenge, we need to run `/challenge/pwn` and `/challenge/college` using a shell script. Then, we must redirect the output of that shell script into the `/challenge/solve ` program. This will print the flag to the terminal.

#### Commands run: 

```sh
$ echo "/challenge/pwn" > x.sh
$ echo "/challenge/college" >> x.sh
$ cat x.sh
/challenge/pwn
/challenge/college

$ bash x.sh | /challenge/solve
```

## Flag: 

```
pwn.college{oN_81Z-lqraStIzMz-9foKscsfo.QX4ETO0wSOxAzNzEzW}
```

# Challenge 6: Executable Shell Scripts

You have written your first shell script, but calling it via `bash script.sh` is a pain.
Why do you need that `bash`?

When you invoke `bash script.sh`, you are, of course launching the `bash` command with the `script.sh` argument.
This tells bash to read its commands from `script.sh` instead of standard input, and thus your shell script is executed.

It turns out that you can avoid the need to manually invoke `bash`.
If your shell script file is _executable_ (recall [File Permissions](/linux-luminarium/permissions)), you can simply invoke it via its relative or absolute path!
For example, if you create `script.sh` in your home directory _and make it executable_, you can invoke it via `/home/hacker/script.sh` or `~/script.sh` or (if your working directory is `/home/hacker`) `./script.sh`.

Try that here!
Make a shellscript that will invoke `/challenge/solve`, make it executable, and run it without explicitly invoking `bash`!

## Solution:

In this challenge, we must make a shell script `slv.sh` that will invoke `/challenge/solve`. Then, we have to make it executable using the `chmod` commmand so that we can run it without using `bash`. Doing this properly will allow us to capture the flag.

#### Commands run: 

```sh
$ echo "/challenge/solve" > slv.sh
$ chmod +x slv.sh
$ ./slv.sh
```

## Flag: 

```
pwn.college{sNkcxkBL8PWQt_KVTTmDLmRQgBA.QX0cjM1wSOxAzNzEzW}
```

# Challenge 7: Understanding Shebangs

You're well on your way to your new life as a shell scripter!
However, so far, your shellscripts _can only be launched from the shell_.
Things worked great in the previous level (because you were invoking your script from the `bash` shell), but they won't work if your script was being invoked by, say, a program written in Python (or any other language).

When a program is invoked in Linux, the Linux kernel first inspects the file to determine how it should be run.
This does NOT use the extension (which is why you don't _have_ to name your shell scripts with a `.sh` extension, or your Python scripts with a `.py` extension, or so on).
Rather, Linux looks at the first few bytes of the file for this information.

There are a bunch of different types of programs, but if the program file starts with the characters `#!` (often termed a "[shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))"), Linux treats the file as an _interpreted program_, and the contents of the rest of the line as the path to the _interpreter_.
It then invokes the interpreter with the path to the program file as its only argument.

Consider this shell script:

```bash
#!/bin/bash

echo "Hello Hackers!"
```

This can be executed as:

```console
hacker@dojo:~$ chmod a+x script.sh
hacker@dojo:~$ ./script.sh
Hello Hackers!
hacker@dojo:~$
```

When `./script.sh` was executed, Linux opened the file, read the first line, extracted `/bin/bash` as the interpreter, and executed `/bin/bash ./script.sh` to launch the script!

Note, the shebang line must be the VERY FIRST line of the file - no blank lines or spaces before it!

For this challenge, create a script at `/home/hacker/solve.sh` that has a proper shebang and outputs "hack the planet".
Remember to make it executable, then run `/challenge/run` to verify your script works correctly!

----
**FUN FACT:**
Common shebangs you might see:
- `#!/bin/bash` for bash scripts
- `#!/usr/bin/python3` for Python scripts
- `#!/bin/sh` for POSIX shell scripts --- this is a more primitive predecessor to `bash` with fewer features, but more compatibility to non-Linux systems!

## Solution:

In this challenge, we must make a shell script `solve.sh` in our home directory. The script must start with a proper shebang such as `#!/bin/bash` and must print `"hack the pllanet"`. Then, must make it executable using `chmod` so that it can be run without invoking `bash`. If we have done everything correctly, then running `/challenge/run` will print the flag to the terminal.

#### Commands run: 

```sh
$ nano  solve.sh
```

Enter the script:
```sh
#!/bin/bash
echo "hack the planet"
```
Then press `Ctrl+X`, Press `Y` when it asks if you want to save the modified buffer, And hit `Enter`.

```sh
$ chmod +x solve.sh
$ /challenge/run 
```

## Flag: 

```
pwn.college{YMeaB2v-aVguLrjBTPUY8oX_7wE.0VOzMDOxwSOxAzNzEzW}
```

# Challenge 8: 



## Solution:



#### Commands run: 

```sh
$ 
```

## Flag: 

```
pwn.college{}
```

# Challenge 9: 



## Solution:



#### Commands run: 

```sh
$ 
```

## Flag: 

```
pwn.college{}
```

# Challenge 10: 



## Solution:



#### Commands run: 

```sh
$ 
```

## Flag: 

```
pwn.college{}
```

# Challenge 11: 



## Solution:



#### Commands run: 

```sh
$ 
```

## Flag: 

```
pwn.college{}
```

# Challenge 12: 



## Solution:



#### Commands run: 

```sh
$ 
```

## Flag: 

```
pwn.college{}
```
