
# Challenge 1: Matching with *

The first glob we'll learn is `*`.
When it encounters a `*` character in any argument, the shell will treat it as a "wildcard" and try to replace that argument with any files that match the pattern.
It's easier to show you than explain:

```sh
hacker@dojo:~$ touch file_a
hacker@dojo:~$ touch file_b
hacker@dojo:~$ touch file_c
hacker@dojo:~$ ls
file_a  file_b  file_c
hacker@dojo:~$ echo Look: file_*
Look: file_a file_b file_c
```

Of course, though in this case, the glob resulted in multiple arguments, it can just as simply match only one.
For example:

```sh
hacker@dojo:~$ touch file_a
hacker@dojo:~$ ls
file_a
hacker@dojo:~$ echo Look: file_*
Look: file_a
```

When zero files are matched, by default, the shell leaves the glob unchanged:

```sh
hacker@dojo:~$ touch file_a
hacker@dojo:~$ ls
file_a
hacker@dojo:~$ echo Look: nope_*
Look: nope_*
```

The `*` matches any part of the filename except for `/` or a leading `.` character.
For example:

```sh
hacker@dojo:~$ echo ONE: /ho*/*ck*
ONE: /home/hacker
hacker@dojo:~$ echo TWO: /*/hacker
TWO: /home/hacker
hacker@dojo:~$ echo THREE: ../*
THREE: ../hacker
```

Now, practice this yourself!
Starting from your home directory, change your directory to `/challenge`, but use globbing to keep the argument you pass to `cd` to at most four characters!
Once you're there, run `/challenge/run` for the flag!

## Solution:

After the terminal comes up, the user needs to change into the `/challenge` directory from the home directory using `*` globbing by entering `cd /ch*`. The user can then run the `/challenge/run` program to capture the flag.

#### Commands run: 

```sh
This challenge resets your working directory to /home/hacker unless you change directory properly...
$ cd /ch*
$ ./run
```

## Flag: 

```
pwn.college{okjhYIIHTozcYjmHNBC4HDQEbmB.QXxIDO0wSOxAzNzEzW}
```

# Challenge 2: Matching with ?

Next, let's learn about `?`.
When it encounters a `?` character in any argument, the shell will treat it as a **single-character** wildcard.
This works like `*`, but only matches _one_ character.
For example:

```sh
hacker@dojo:~$ touch file_a
hacker@dojo:~$ touch file_b
hacker@dojo:~$ touch file_cc
hacker@dojo:~$ ls
file_a  file_b  file_cc
hacker@dojo:~$ echo Look: file_?
Look: file_a file_b
hacker@dojo:~$ echo Look: file_??
Look: file_cc
```

Now, practice this yourself!
Starting from your home directory, change your directory to `/challenge`, but use the `?` character instead of `c` and `l` in the argument to `cd`!
Once you're there, run `/challenge/run` for the flag!

## Solution:

After the terminal comes up, the user needs to change into the `/challenge` directory from the home directory without using `c` and `l`. The user must instead use `?` globbing by entering `cd /?ha??enge`. The user can then run the `/challenge/run` program to capture the flag. 

#### Commands run: 

```sh
This challenge resets your working directory to /home/hacker unless you change directory properly...
$ cd ?ha??enge
$ ./run
```

## Flag: 

```
pwn.college{chpJPzRsbyaw3h7yogLv3dCyJgP.QXyIDO0wSOxAzNzEzW}
```

# Challenge 3: Matching with []

Next, we will cover `[]`.
The square brackets are, essentially, a limited form of `?`, in that instead of matching any character, `[]` is a wildcard for some subset of potential characters, specified within the brackets.
For example, `[pwn]` will match the character `p`, `w`, or `n`.
For example:

```sh
hacker@dojo:~$ touch file_a
hacker@dojo:~$ touch file_b
hacker@dojo:~$ touch file_c
hacker@dojo:~$ ls
file_a  file_b  file_c
hacker@dojo:~$ echo Look: file_[ab]
Look: file_a file_b
```

Try it here!
We've placed a bunch of files in `/challenge/files`.
Change your working directory to `/challenge/files` and run `/challenge/run` with a single argument that bracket-globs into `file_b`, `file_a`, `file_s`, and `file_h`!

## Solution:

After the terminal comes up, the user needs to use `[]` globbing to run the /`/challenge/run` program with `file_b`, `file_a`, `file_s`, and `file_h` located in the `/challenge/files` directory as arguments. This will print the flag.

#### Commands run: 

```sh
$ cd /challenge/files
$ ../run file_[abhs]
```

## Flag: 

```
pwn.college{omcaYQtSzDBitFvG817dSc2kv7n.QXzIDO0wSOxAzNzEzW}
```

# Challenge 4: Matching paths with []

Globbing happens on a _path_ basis, so you can expand entire paths with your globbed arguments.
For example:

```sh
hacker@dojo:~$ touch file_a
hacker@dojo:~$ touch file_b
hacker@dojo:~$ touch file_c
hacker@dojo:~$ ls
file_a  file_b  file_c
hacker@dojo:~$ echo Look: /home/hacker/file_[ab]
Look: /home/hacker/file_a /home/hacker/file_b
```

Now it's your turn.
Once more, we've placed a bunch of files in `/challenge/files`.
Starting from your home directory, run `/challenge/run` with a single argument that bracket-globs into the absolute paths to the `file_b`, `file_a`, `file_s`, and `file_h` files!

## Solution:

After the terminal comes up, the user needs to use `[]` globbing to run the /`/challenge/run` program with `file_b`, `file_a`, `file_s`, and `file_h` located in the `/challenge/files` directory as arguments but this time using thier absolute paths instead. This will print the flag.

#### Commands run: 

```sh
$ /challenge/run /challenge/files/file_[absh]
```

## Flag: 

```
pwn.college{wb_MdoPJpT2Xcw8WNrNVoGqTIDf.QX0IDO0wSOxAzNzEzW}
```

# Challenge 5: Multiple globs

So far, you've specified one glob at a time, but you can do more!
Bash supports the expansion of multiple globs in a single word.
For example:

```sh
hacker@dojo:~$ cat /*fl*
pwn.college{YEAH}
hacker@dojo:~$
```

What happens above is that the shell looks for all files in `/` that start with _anything_ (including nothing), then have an `f` and an `l`, and end in _anything_ (including `ag`, which makes `flag`).

Now you try it.
We put a few happy, but diversely-named files in `/challenge/files`.
Go `cd` there and run `/challenge/run`, providing a single argument: a short (3 characters or less) globbed word with two `*` globs in it that covers every word that contains the letter `p`.

## Solution:

After the terminal comes up, the user needs to change to the `/challenge/files` directory. then, the user must come up with a single, short (3 characters or less) glob that will match all files containing the letter `p`. This can be done by using the glob `*p*`. The user must then run the `/challenge/run` program with this glob as the argument to capture the flag.

#### Commands run: 

```sh
$ cd /challenge/files
$ ../run *p*
```

## Flag: 

```
pwn.college{8k-BfNApLLkIKr-uvDgJ7AvIu5o.0lM3kjNxwSOxAzNzEzW}
```

# Challenge 6: Mixing globs

Now, let's put the previous levels together!
We put a few happy, but diversely-named files in `/challenge/files`.
Go `cd` there and, using the globbing you've learned, write a single, short (6 characters or less) glob that (when passed as an argument to `/challenge/run`) will match the files "challenging", "educational", and "pwning"!

## Solution:

After the terminal comes up, the user needs to change to the `/challenge/files` directory. then, the user can use ls to list all the files in the directory and must come up with a single, short (6 characters or less) glob that will match the files `challenging`, `educational`, and `pwning`. The files in the directory all start with a different alphabet each. So, `[cep]*` will be a valid solution. The user must then run the `/challenge/run` program with this glob as the argument to capture the flag.

I didn't do this btw. I did it by trial and error because of my stubbornness to not use `ls` for some reason lol. Then, I thought to use the `[]` glob with the starting characters of each expecting it to not work because it must surely not be that simple but I also thought that there was a great chance that all the files simply started with different alphabets. Here is a glimpse into my psyche:
```sh
hacker@globbing~mixing-globs:~$ cd /challenge/files/
hacker@globbing~mixing-globs:/challenge/files$ echo Find: *n*i*n*
Find: challenging pwning
hacker@globbing~mixing-globs:/challenge/files$ echo Find: *i*n*
Find: amazing challenging educational incredible kind laughing pwning radiant thrilling uplifting
hacker@globbing~mixing-globs:/challenge/files$ echo Find: *i[]n*
Find: *i[]n*
hacker@globbing~mixing-globs:/challenge/files$ echo Find: *i?n*
Find: educational radiant
hacker@globbing~mixing-globs:/challenge/files$ echo Find: *c*
Find: challenging educational fantastic incredible magical nice optimistic victorious
hacker@globbing~mixing-globs:/challenge/files$ echo Find: *c*a
Find: *c*a
hacker@globbing~mixing-globs:/challenge/files$ echo Find: *c*a*
Find: challenging educational magical
hacker@globbing~mixing-globs:/challenge/files$ echo Find: *i[no]*
Find: amazing challenging educational incredible kind laughing pwning thrilling uplifting victorious
hacker@globbing~mixing-globs:/challenge/files$ echo Find: *n[ga]*
Find: amazing challenging educational laughing pwning thrilling uplifting
hacker@globbing~mixing-globs:/challenge/files$ echo Find: *i*[ga]*
Find: amazing challenging delightful educational jovial laughing magical pwning radiant thrilling uplifting xenial
hacker@globbing~mixing-globs:/challenge/files$ echo Find: [cep]*
Find: challenging educational pwning
hacker@globbing~mixing-globs:/challenge/files$ ../run [cep]*
You got it! Here is your flag!
pwn.college{ghxW2NANRgcSAvTQWjbey4TTsys.QX1IDO0wSOxAzNzEzW}
hacker@globbing~mixing-globs:/challenge/files$ ls
amazing    challenging  educational  great  incredible  kind      magical  optimistic  queenly  splendid   uplifting   wonderful  youthful
beautiful  delightful   fantastic    happy  jovial      laughing  nice     pwning      radiant  thrilling  victorious  xenial     zesty
hacker@globbing~mixing-globs:/challenge/files$ 
```

#### Commands run: 

```sh
$ cd /challenge/files
$ ls
$ ../run [cep]*
```

## Flag: 

```
pwn.college{ghxW2NANRgcSAvTQWjbey4TTsys.QX1IDO0wSOxAzNzEzW}
```

# Challenge 7: Exclusionary globbing

Sometimes, you want to filter out files in a glob!
Luckily, `[]` helps you do just this.
If the first character in the brackets is a `!` or (in newer versions of bash) a `^`, the glob inverts, and that bracket instance matches characters that _aren't_ listed.
For example:

```sh
hacker@dojo:~$ touch file_a
hacker@dojo:~$ touch file_b
hacker@dojo:~$ touch file_c
hacker@dojo:~$ ls
file_a  file_b  file_c
hacker@dojo:~$ echo Look: file_[!ab]
Look: file_c
hacker@dojo:~$ echo Look: file_[^ab]
Look: file_c
hacker@dojo:~$ echo Look: file_[ab]
Look: file_a file_b
```

Armed with this knowledge, go forth to `/challenge/files` and run `/challenge/run` with all files that don't start with `p`, `w`, or `n`!

**NOTE:** The `!` character has a different special meaning in bash when it's not the first character of a `[]` glob, so keep that in mind if things stop making sense! `^` does not have this problem, but is also not compatible with older shells.

## Solution:

Here, the user needs to change into the `/challenge/files` directory and come up with a glob that will return all files that don't start with `p`, `w`, or `n`. This can be done by using either `[!pwn]*` or `[^pwn]*`. The user must then run the `/challenge/run` program with this glob as the argument to capture the flag.

#### Commands run: 

```sh
$ cd /challenge/files
$ ../run [^pwn]*
```

## Flag: 

```
pwn.college{IJZvaHU10wSWt84IgitZGhC26kU.QX2IDO0wSOxAzNzEzW}
```

# Challenge 8: Tab completion

As tempting as it might be, using `*` to shorten what must be typed on the commandline can lead to mistakes.
Your glob might expand to unintended files, and you might not spot it until the `rm` command is already running!
No one is safe from this style of error.

A safer alternative when you are trying to specify a specific target is _tab completion_.
If you hit tab in the shell, it'll try to figure out what you're going to type and automatically complete it.
Auto-completion is super useful, and this challenge will explore its use in specifying files.

This challenge has copied the flag into `/challenge/pwncollege`, and you can freely `cat` that file.
But you can't type the filename: we used some serious trickery to make sure that you _must_ tab-complete it.
Try it out!

```sh
hacker@dojo:~$ ls /challenge
DESCRIPTION.md  pwncollege
hacker@dojo:~$ cat /challenge/pwncollege
cat: /challenge/pwncollege: No such file or directory
hacker@dojo:~$ cat /challenge/pwn<TAB>
pwn.college{HECK YEAH}
hacker@dojo:~$
```

When you hit that tab key, the name will expand and you'll be able to read the file.
Good luck!

## Solution:

In this challenge, the flag has been stored in the file `/challenge/pwncollege`, the user simply needs to use the `cat` command to capture it. However, a restriction has been placed on the user such that the flag won't be printed unless `[Tab]` completion is used. If the user uses `[Tab]` completion to enter the correct command, the flag will be printed.

#### Commands run: 

Enter `cat /c`, press `[Tab]`, enter `p`, press `[Tab]` again, and hit `[Enter]`. The input should look like the following:
```sh
$ cat /challenge/pwncollege​
```

## Flag: 

```
pwn.college{Es3-PtWmWJGpzbUi6pdvmlNQGWp.0FN0EzNxwSOxAzNzEzW}
```

# Challenge 9: Multiiple options for tab completion

Consider the following situation:

```sh
hacker@dojo:~$ ls
flag  flamingo  flowers
hacker@dojo:~$ cat f<TAB>
```

There are multiple options!
What happens?

What happens varies based on the specific shell and its options.
By default `bash` will auto-expand until the first point when there are multiple options (in this case, `fl`).
When you hit tab a _second_ time, it'll print out those options.
Other shells and configurations, instead, will cycle through the options.

This challenge has a `/challenge/files` directory with a bunch of files starting with `pwncollege`.
Tab-complete from `/challenge/files/p` or so, and make your way to the flag!

## Solution:

In this challenge, the flag has been stored in a file in the `/challenge/files` directory and the user has been given the information that the file name starts with a `p`. The user simply needs to use `cd` into the `/challenge/files` directory and then `cat` the correct file to capture the flag. However, a restriction has been placed on the user such that the user is not allowed to use ls to look for the file. The user must start from `cat p` and use `[Tab]` completion to reach the correct file. The flag will then be printed to the terminal.

#### Commands run: 

```sh
$ cd /challenge/files
```
Enter `cat p`, Hit `[Tab]`, The input should have changed to `cat pwn`. Then, hit `[Tab]` twice to see the remaining options. Enter `c` and hit `[Tab]` again so that the input becomes `cat pwncollege-`. After this, enter `flag` manually. `[Tab]` completion won't help you after this point. Then, hit `[Enter]`. The input should look like the following:
```sh
$ cat pwncollege-flag
```

## Flag: 

```
pwn.college{oxsdKykklF96xwcK6Iy6G_9g4gz.0lN0EzNxwSOxAzNzEzW}
```

# Challenge 10: Tab completion on commands

Tab completion is for more than files!
You can also tab-complete commands.
This level has a command that starts with `pwncollege`, and it'll give you the flag.
Type `pwncollege` and hit the tab key to auto-complete it!

----
**NOTE:**
You can auto-complete any command, but be careful: callous auto-completes without double-checking the result can wreak havoc in your shell if you accidentally run the wrong commands!

## Solution:

In this challenge, a command starting with `pwncollege` has been created to print the flag but the full name of the command is kept secret. The user must find the name of that command and run it to capture the flag. If the user enters `pwncollege` and hits `[Tab]`, the name of the command will be entered and the flag can be captured.

#### Commands run: 

Enter `pwncollege` and hit `[Tab]`. The rest of the command will be autocompleted. Then, just hit `[Enter]`. The input should look like the following:
```sh
$ pwncollege-23508
```

## Flag: 

```
pwn.college{sIV3wqs_5HHdKhkVd1qaKnGGu6a.0VN0EzNxwSOxAzNzEzW}
```
