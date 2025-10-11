
# Challenge 1: The PATH Variable

It turns out that the answer to "How does the shell find `ls`?" is fairly simple.
There is a special shell variable, called `PATH`, that stores a bunch of directory paths in which the shell will search for programs corresponding to commands.
If you blank out the variable, things go badly:

```console
hacker@dojo:~$ ls
Desktop    Downloads  Pictures  Templates
Documents  Music      Public    Videos
hacker@dojo:~$ PATH=""
hacker@dojo:~$ ls
bash: ls: No such file or directory
hacker@dojo:~$
```

Without a PATH, bash cannot find the `ls` command.

In this level, you will disrupt the operation of the `/challenge/run` program.
This program will **DELETE** the flag file using the `rm` command.
However, if it can't find the `rm` command, the flag will not be deleted, and the challenge will give it to you!
Thus, you must make it so that `/challenge/run` also can't find the `rm` command!

Keep in mind: `/challenge/run` will be a _child process_ of your shell, so you must apply the concepts you learned in [Shell Variables](https://pwn.college/linux-luminarium/variables/) to mess with its `PATH` variable!
If you don't succeed, and the flag gets deleted, you will need to restart the challenge to try again!

## Solution:

In this challenge, the `/challenge/run` program will try to remove the `/flag` file. To prevent this from happening, we must change the `PATH` variable in such a manner that `/challenge/run` is unable to find the `rm` command. We can do this by simply just setting `PATH` as blank. When the `/challenge/run` program is unable to delete the `/flag` file, it will instead print it and the flag can be captured.

#### Commands run: 

```sh
$ PATH=""
$ /challenge/run
```

## Flag: 

```
pwn.college{oJJoIb9AAqueHiNpvaUTn7ZEwxt.QX2cDM1wSOxAzNzEzW}
```

# Challenge 2: Setting PATH

Okay, so things break when you blank out `PATH`.
But what about doing something _useful_ with `PATH`?

Let's explore how we would, for example, add a new directory of programs to our command repertoire.
Recall that `PATH` stores a list of directories to find commands in and, for commands in nonstandard places, we must typically execute them via their path:

```console
hacker@dojo:~$ ls /home/hacker/scripts
goodscript      badscript       okayscript
hacker@dojo:~$ goodscript
bash: goodscript: command not found
hacker@dojo:~$ /home/hacker/scripts/goodscript
YEAH! This is the best script!
hacker@dojo:~$
```

If you maintain useful scripts that you want to be able to launch by bare name, this is annoying.
However, by adding directories to or replacing directories in this list, you can expose these programs to be launched using their bare name!
For example:

```console
hacker@dojo:~$ PATH=/home/hacker/scripts
hacker@dojo:~$ goodscript
YEAH! This is the best script!
hacker@dojo:~$
```

Let's practice.
This level's `/challenge/run` will run the `win` command via its bare name, but this command exists in the `/challenge/more_commands/` directory, which is not initially in the PATH.
The `win` command is the _only_ thing that `/challenge/run` needs, so you can just overwrite `PATH` with that one directory.
Good luck!

## Solution:

In this challenge, `/challenge/run` needs access to a custom command `win` located in the `/challenge/more_commands` directory. To make `win` accessible to `/challenge/run`, we need to add the `/challenge/more_commands` to the `PATH` variable. In this case, we can simply overwrite the `PATH` variable since `/challenge/run` only relies `win`. Then, we can run `/challenge/run` to capture the flag.

#### Commands run: 

```sh
$ PATH="/challenge/more_commands"
$ /challenge/run
```

## Flag: 

```
pwn.college{kSee8Y6DVkisTORjkzAysXnLpYH.QX1cjM1wSOxAzNzEzW}
```

# Challenge 3: Finding Commands

When you type the name of a command, _something_ inside one of the many directories listed in your `$PATH` variable is what actually gets executed (of course, unless the command is a builtin!).
But _which_ file, precisely?
You can find out with the aptly-named `which` command:

```console
hacker@dojo:~$ which cat
/bin/cat
hacker@dojo:~$ /bin/cat /flag
YEAH
hacker@dojo:~$
```

Mirroring what the shell does when searching for commands, `which` looks at each directory in `$PATH` in order and prints the first file it finds whose name matches the argument you passed.

In this challenge, we added a `win` command somewhere in your `$PATH`, but it won't give you the flag.
Instead, it's in the same directory as a `flag` file that we made readable by you!
You must find `win` (with the `which` command), and `cat` the flag out of that directory!

## Solution:

In this challenge, a `win` command has been added somewhere in the `PATH`. We have to use the `which` command to find where `win` is and then print the `flag` file located in the same directory using the `cat` command. This will give us the flag.

#### Commands run: 

```sh
$ which win
/challenge/paths/19766/win

$ cat /challenge/paths/19766/flag
```

## Flag: 

```
pwn.college{sF53hySREYfb6jrHZ_UHorVarNL.01NzEzNxwSOxAzNzEzW}
```

# Challenge 4: Adding Commands

Recall our example from the previous level:

```console
hacker@dojo:~$ ls /home/hacker/scripts
goodscript      badscript       okayscript
hacker@dojo:~$ PATH=/home/hacker/scripts
hacker@dojo:~$ goodscript
YEAH! This is the best script!
hacker@dojo:~$
```

What we see here, of course, is the `hacker` making the shell more useful for themselves by bringing their own commands to the party.
Over time, you might amass your own elegant tools.
Let's start with `win`!

Previously, the `win` command that `/challenge/run` executed was stored in `/challenge/more_commands`.
This time, `win` does not exist!
Recall the final level of [Chaining Commands](/linux-luminarium/chaining), and make a shell script called `win`, add its location to the `PATH`, and enable `/challenge/run` to find it!

----
**Hint:**
`/challenge/run` runs as `root` and will call `win`. Thus, `win` can simply cat the flag file.
Again, the `win` command is the _only_ thing that `/challenge/run` needs, so you can just overwrite `PATH` with that one directory.
But remember, if you do that, your `win` command won't be able to find `cat`.

You have three options to avoid that:

1. Figure out where the `cat` program is on the filesystem. It _must_ be in a directory that lives in the `PATH` variable, so you can print the variable out (refer to [Shell Variables](/linux-luminarium/variables) to remember how!), and go through the directories in it (recall that the different entries are separated by `:`), find which one has `cat` in it, and invoke `cat` by its absolute path.
2. Set a `PATH` that has the old directories _plus_ a new entry for wherever you create `win`.
3. Use `read` (again, refer to [Shell Variables](/linux-luminarium/variables)) to read `/flag`. Since `read` is a builtin functionality of `bash`, it is unaffected by `PATH` shenanigans.

Now, go and `win`!

## Solution:

In this challenge, `/challenge/run` will try to execute a `win` command. However, that command does not exist. Instead, we must make a shell script named `win` that will print the flag and add it to the `PATH`. In this scenario, we cannot simply overwrite the `PATH` variable. Instead, we can add the location of the `win` shell script to the end of `PATH`. Then, we can run `/challenge/run` to get the flag.

#### Commands run: 

```sh
$ echo "cat /flag" > win
$ chmod +x win
$ PATH=$PATH":/home/hacker"
$ /challenge/run
```

## Flag: 

```
pwn.college{MFewvXQhsFNYYv1xRjlWTQjfmIi.QX2cjM1wSOxAzNzEzW}
```

# Challenge 5: Hijacking Commands

Armed with your knowledge, you can now carry out some shenanigans.
This challenge is almost the same as the first challenge in this module.
Again, this challenge will delete the flag using the `rm` command.
But unlike before, it will _not_ print anything out for you.

How can you solve this?
You know that `rm` is searched for in the directories listed in the `PATH` variable.
You have experience creating the `win` command when the previous challenge needed it.
What else can you create?

## Solution:

In this challenge, `/challenge/run` will try to remove the `/flag` file. To do that, it will call the `rm` command. Unlike before, we cannot simply set `PATH` to blank as this time `/challenge/run` will not print the `/flag` file. Instead, we must make a shell script named `rm` that will print the flag and add it to the beginning of the `PATH`. In this manner, when `/challenge/run` tries to find `rm`, it will find our shell script first. Then, we can run `/challenge/run` to get the flag.

#### Commands run: 

```sh
$ echo "cat /flag" > rm
$ chmod +x rm
$ PATH="/home/hacker:"$PATH
$ /challenge/run
```

## Flag: 

```
pwn.college{MynKNsm4NMYjIKMpwn9q4jCZCYZ.QX3cjM1wSOxAzNzEzW}
```
