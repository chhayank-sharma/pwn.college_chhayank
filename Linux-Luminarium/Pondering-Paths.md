
# Challenge 1: The Root

Alright, so the filesystem starts at `/`.
Under that, there are a whole mess of other directories, configuration files, programs, and, most importantly, _flags_.
In this level, we've added a program right in `/`, called `pwn`, that will give you the flag.
All you need to do for this level is to invoke this program!

You can invoke a program by providing its path on the command line.
In this case, you'll be giving the exact path, starting from `/`, so the path would be `/pwn`.
This style of path, one that starts with the root directory, is referred to as an "absolute path".

Start the challenge, launch a terminal, invoke the `pwn` program using its absolute path, and Capture that Flag!
Good luck!

## Solution:

After the terminal comes up, the user needs to run the `pwn` program in the root directory using its absolute path which will print the flag.

#### Commands run: 

```sh
$ /pwn
```

## Flag: 

```
pwn.college{YmFRRms07UGdFi1UK_on8HSVRMU.QX4cTO0wSOxAzNzEzW}
```

# Challenge 2: Program and absolute paths

Let's explore a slightly more complicated path!
Except for in the previous level, challenges in pwn.college are in the `challenge` directory and the `challenge` directory is, in turn, right in the root directory (`/`).
The path to the challenge directory is, thus, `/challenge`.
The name of the challenge program in this level is `run`, and it lives in the `/challenge` directory.
Thus, the path to the `run` challenge program is `/challenge/run`.

This challenge again requires you to execute it by invoking its absolute path.
You'll want to execute the `run` file that is in the `challenge` directory that is, in turn, in the `/` directory.
If you invoke the challenge correctly, it will give you the flag.
Good luck!

## Solution:

After the terminal comes up, the user needs to run the `run` program in the challenge directory using its absolute path which will print the flag.

#### Commands run: 

```sh
$ /challenge/run
```

## Flag: 

```
pwn.college{c7IsFUVqip16nbRA9Nty7uwJ1kD.QX1QTN0wSOxAzNzEzW}
```

# Challenge 3: Position thy self

The Linux filesystem has tons of directories with tons of files.
You can navigate around directories by using the `cd` (`c`hange `d`irectory) command and passing a path to it as an argument, as so:

```sh
hacker@dojo:~$ cd /some/new/directory
hacker@dojo:/some/new/directory$
```

This affects the "current working directory" of your process (in this case, the bash shell).
Each process has a directory in which it's currently hanging out.
The reasons for this will become clear later in the module.

As an aside, now you can see what the `~` was in the prompt!
It shows the current path that your shell is located at.

This challenge will require you to execute the `/challenge/run` program from a specific path (which it will tell you).
You'll need to `cd` to that directory before rerunning the challenge program.
Good luck!

## Solution:

After the terminal comes up, the user needs to move to the `/var/` directory and then run the `run` program using its absolute path which will print the flag.

#### Commands run: 

```sh
$ /challenge/run
$ cd /var
$ /challenge/run
```

## Flag: 

```
pwn.college{gDwZ4QuPwNPZETq_Y3Fy-gqxduD.QX2QTN0wSOxAzNzEzW}
```

### Notes:

- Current working directory also affects a programs behaviour

# Challenge 4: Position elsewhere

The Linux filesystem has tons of directories with tons of files.
You can navigate around directories by using the `cd` (`c`hange `d`irectory) command and passing a path to it as an argument, as so:

```sh
hacker@dojo:~$ cd /some/new/directory
hacker@dojo:/some/new/directory$
```

This affects the "current working directory" of your process (in this case, the bash shell).
Each process has a directory in which it's currently hanging out.
The reasons for this will become clear later in the module.

As an aside, now you can see what the `~` was in the prompt!
It shows the current path that your shell is located at.

This challenge will require you to execute the `/challenge/run` program from a specific path (which it will tell you).
You'll need to `cd` to that directory before rerunning the challenge program.
Good luck!

## Solution:

Same as challenge 4 but current workin directory is changed to `/usr/aarch64-linux-gnu/include/gnu/`

#### Commands run: 

```sh
$ /challenge/run
$ cd /usr/aarch64-linux-gnu/include/gnu/
$ /challenge/run
```

## Flag: 

```
pwn.college{cYgR9pq8giuYS4Z-2FS4DrxOGoS.QX3QTN0wSOxAzNzEzW}
```

# Challenge 5: Position yet elsewhere

The Linux filesystem has tons of directories with tons of files.
You can navigate around directories by using the `cd` (`c`hange `d`irectory) command and passing a path to it as an argument, as so:

```sh
hacker@dojo:~$ cd /some/new/directory
hacker@dojo:/some/new/directory$
```

This affects the "current working directory" of your process (in this case, the bash shell).
Each process has a directory in which it's currently hanging out.
The reasons for this will become clear later in the module.

As an aside, now you can see what the `~` was in the prompt!
It shows the current path that your shell is located at.

This challenge will require you to execute the `/challenge/run` program from a specific path (which it will tell you).
You'll need to `cd` to that directory before rerunning the challenge program.
Good luck!

## Solution:

Same as challenge 4 and 5 but current workin directory is changed to `/usr/share/build-essential`

#### Commands run: 

```sh
$ /challenge/run
$ cd /usr/share/build-essential
$ /challenge/run
```

## Flag: 

```
pwn.college{4j1iiVxuIiQEPr0lUj_dXXVAw6R.QX4QTN0wSOxAzNzEzW}
```

# Challenge 6: implicit relative paths, from /

Now you're familiar with the concept of referring to absolute paths and changing directories.
If you put in absolute paths everywhere, then it really doesn't matter what directory you are in, as you likely found out in the previous three challenges.

However, the current working directory does matter for **relative** paths.

- A relative path is any path that does not start at root (i.e., it does not start with `/`).
- A relative path is interpreted **relative** to your **c**urrent **w**orking **d**irectory (`cwd`).
- Your `cwd` is the directory that your prompt is currently located at.

This means how you specify a particular file, depends on where the terminal prompt is located.

Imagine we want to access some file located at `/tmp/a/b/my_file`.

- If my `cwd` is `/`, then a relative path to the file is `tmp/a/b/my_file`.
- If my `cwd` is `/tmp`, then a relative path to the file is `a/b/my_file`.
- If my `cwd` is `/tmp/a/b/c`, then a relative path to the file is `../my_file`.  The `..` refers to the parent directory.

Let's try it here!
You'll need to run `/challenge/run` using a relative path while having a current working directory of `/`.
For this level, I'll give you a hint.
Your relative path starts with the letter `c` 😊


## Solution:

After the terminal comes up, the user needs to move to the root directory and then run the `run` program using its `implicit` relative path which will print the flag.

#### Commands run: 

```sh
$ cd /
$ challenge/run
```

## Flag: 

```
pwn.college{cNFwVQFZJ9G-BIwQMc7OlfzqIMS.QX5QTN0wSOxAzNzEzW}
```

# Challenge 7: explicit relative paths, from /

Previously, your relative path was "naked": it directly specified the directory to descend into from the current directory.
In this level, we're going to explore more explicit relative paths.

In most operating systems, including Linux, every directory has two implicit entries that you can reference in paths: `.` and `..`.
The first, `.`, refers right to the same directory, so the following absolute paths are all identical to each other:

- `/challenge`
- `/challenge/.`
- `/challenge/./././././././././`
- `/./././challenge/././`

The following relative paths are also all identical to each other:

- `challenge`
- `./challenge`
- `./././challenge`
- `challenge/.`

Of course, if your current working directory is `/`, the above relative paths are equivalent to the above absolute paths.

This challenge will get you using `.` in your relative paths.
Get ready!

## Solution:

After the terminal comes up, the user needs to move to the root directory and then run the `run` program using its `explicit` relative path which will print the flag.

#### Commands run: 

```sh
$ cd /
$ ./challenge/run
```

## Flag: 

```
pwn.college{ojkqhDpnHot35tI_AcnXwkVunfg.QXwUTN0wSOxAzNzEzW}
```

# Challenge 8: implicit relative path

In this level, we'll practice referring to paths using `.` a bit more.
This challenge will need you to run it from the `/challenge` directory.
Here, things get slightly tricky.

Linux explicitly avoids automatically looking in the current directory when you provide a "naked" path.
Consider the following:

```sh
hacker@dojo:~$ cd /challenge
hacker@dojo:/challenge$ run
```

This will *not* invoke /challenge/run.
This is actually a safety measure: if Linux searched the current directory for programs every time you entered a naked path, you could accidentally execute programs in your current directory that happened to have the same names as core system utilities!
As a result, the above commands will yield the following error:

```sh
bash: run: command not found
```

We'll explore the mechanisms behind this concept later, but in this challenge, we'll learn how to explicitly use relative paths to launch `run` in this scenario.
The way to do this is to *tell* Linux that you explicitly want to execute a program in the current directory, using `.` like in the previous levels.
Give it a try now!

## Solution:

After the terminal comes up, the user needs to move to the challenges directory and then run the run program using its implicit relative path which will print the flag.

#### Commands run: 

```sh
$ cd /challenge
$ ./run
```

## Flag: 

```
pwn.college{EBVBZMk0jTLi0yhN1brAArtWh8D.QXxUTN0wSOxAzNzEzW}
```

# Challenge 9: home sweet home

Every user has a _home directory_, typically under `/home` in the filesystem.
In the dojo, you are the `hacker` user, and your home directory is `/home/hacker`.
The home directory is typically where users store most of their personal files.
As you make your way through pwn.college, this is where you'll store most of your solutions.

Typically, your shell session will start with your home directory as your current working directory.
Consider the initial prompt:

```sh
hacker@dojo:~$
```

The `~` in this prompt is the current working directory, with `~` being shorthand for `/home/hacker`.
Bash provides and uses this shorthand because, again, most of your time will be spent in your home directory.
Thus, whenever bash sees `~` provided as the start of an argument in a way consistent with a path, it will expand it to your home directory.
Consider:

```sh
hacker@dojo:~$ echo LOOK: ~
LOOK: /home/hacker
hacker@dojo:~$ cd /
hacker@dojo:/$ cd ~
hacker@dojo:~$ cd ~/asdf
hacker@dojo:~/asdf$ cd ~/asdf
hacker@dojo:~/asdf$ cd ~
hacker@dojo:~$ cd /home/hacker/asdf
hacker@dojo:~/asdf$
```

Note that the expansion of `~` is an _absolute_ path, and only the leading `~` is expanded.
This means, for example, that `~/~` will be expanded to `/home/hacker/~` rather than `/home/hacker/home/hacker`.

Fun fact: `cd` will use your home directory as the default destination:

```sh
hacker@dojo:~$ cd /tmp
hacker@dojo:/tmp$ cd
hacker@dojo:~$
```

Now it's your turn to play!
In this challenge, `/challenge/run` will write a copy of the flag to any file you specify as an argument on the commandline, with these constraints:

1. Your argument must be an absolute path.
2. The path must be inside your home directory.
3. Before expansion, your argument must be three characters or less.

Again, you must specify your path as an _argument_ to `/challenge/run` as so:

```sh
hacker@dojo:~$ /challenge/run YOUR_PATH_HERE
```


## Solution:

After the terminal comes up, the user needs to move to run the `/challenge/run` command with a three letter absolute path in the home directory. This will write the flag to that file and also print the flag.

#### Commands run: 

```sh
$ /challenge/run ~/p
$ cat p
```

## Flag: 

```
pwn.college{spEWMa4wISwPiXvR3N-bkcEeJeP.QXzMDO0wSOxAzNzEzW}
```
