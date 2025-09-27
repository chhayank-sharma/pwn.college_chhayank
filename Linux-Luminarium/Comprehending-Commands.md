
# Challenge 1: cat: not the pet, but the command!

One of the most critical Linux commands is `cat`.
`cat` is most often used for reading out files, like so:

```console
hacker@dojo:~$ cat /challenge/DESCRIPTION.md
One of the most critical Linux commands is `cat`.
`cat` is most often used for reading out files, like so:
```

`cat` will con**cat**enate (hence the name) multiple files if provided multiple arguments.
For example:

```sh
hacker@dojo:~$ cat myfile
This is my file!
hacker@dojo:~$ cat yourfile
This is your file!
hacker@dojo:~$ cat myfile yourfile
This is my file!
This is your file!
hacker@dojo:~$ cat myfile yourfile myfile
This is my file!
This is your file!
This is my file!
```

Finally, if you give no arguments at all, `cat` will read from the terminal input and output it.
We'll explore that in later challenges...

In this challenge, I will copy the flag to the `flag` file in your home directory (where your shell starts).
Go read it with `cat`!

## Solution:

Here, the flag has been written to a file in our home directory. After the terminal comes up, the user needs to use the cat command to capture it.

#### Commands run: 

```sh
$ cat flag
```

## Flag: 

```
pwn.college{0NuR6I4XCLKvCZzafxBOXxg-QAK.QXxcTN0wSOxAzNzEzW}
```

# Challenge 2: catting absolute paths

In the last level, you did `cat flag` to read the flag out of your home directory!
You can, of course, specify `cat`'s arguments as absolute paths:

```
hacker@dojo:~$ cat /challenge/DESCRIPTION.md
In the last level, you did `cat flag` to read the flag out of your home directory!
You can, of course, specify `cat`'s arguments as absolute paths:
...
```

In this directory, I will not copy it to your home directory, but I will make it readable.
You can read it with `cat` at its absolute path: `/flag`.

----
**FUN FACT:**
`/flag` is where the flag _always_ lives in pwn.college, but unlike in this challenge, you typically can't access that file directly.

## Solution:

Here, the flag has been written to a file in our home directory. After the terminal comes up, the user needs to use the cat command to capture it.

#### Commands run: 

```sh
$ cat /flag
```

## Flag: 

```
pwn.college{MbhM7ZVQXVyYvvsrLIzO2Yn2Wl7.QX5ETO0wSOxAzNzEzW}
```

# Challenge 3: more catting practice

You can specify all sorts of paths as arguments to commands, and we'll practice some more with `cat`.
In this level, I'll put the flag in some crazy directory, and I will not allow you to change directories with `cd`, so no `cat flag` for you.
You must retrieve the flag by absolute path, wherever it is.

## Solution:

```
You cannot use the 'cd' command in this level, and must retrieve the flag by 
absolute path. Plus, I hid the flag in a different directory! You can find it 
in the file /lib/gcc/x86_64-linux-gnu/flag. Go cat it out **without** cding 
into that directory!
```

After the terminal comes up, the user needs to 

#TODO complete this

#### Commands run: 

```sh
$ cat /lib/gcc/x86_64-linux-gnu/flag
```

## Flag: 

```
pwn.college{U0qc6dmLyy6Q557dVVT7iH6os2d.QXwITO0wSOxAzNzEzW}
```

# Challenge 4: grepping for a needle in a haystack

Sometimes, the files that you might `cat` out are too big.
Luckily, we have the `grep` command to search for the contents we need!
We'll learn it in this challenge.

There are many ways to `grep`, and we'll learn one way here:

```sh
hacker@dojo:~$ grep SEARCH_STRING /path/to/file
```

Invoked like this, `grep` will search the file for lines of text containing `SEARCH_STRING` and print them to the console.

In this challenge, I've put a hundred thousand lines of text into the `/challenge/data.txt` file.
`grep` it for the flag!

HINT: The flag always starts with the text `pwn.college`.

## Solution:

After the terminal comes up, the user needs to use the grep commmand to search for the flag in the `/challenge/data.txt` file and print it. The flag will always start with pwn.college so we can grep for that to get the flag.

#### Commands run: 

```sh
$ cd /challenge
$ grep pwn.college data.txt
```
OR
```sh
$ cd /challenge
$ cat data.txt | grep pwn.college
```

## Flag: 

```
pwn.college{Uq2vtwIccJsGAIPTAG1HZ1CK8wL.QX3EDO0wSOxAzNzEzW}
```

# Challenge 5: comparing files

When looking for changes between similar files, eyeballing them might not be the most efficient approach!
This is where the `diff` command becomes invaluable.

`diff` compares two files line by line and shows you exactly what's different between them.
For example:

```sh
hacker@dojo:~$ cat file1
hello
world
hacker@dojo:~$ cat file2
hello
universe
hacker@dojo:~$ diff file1 file2
2c2
< world
---
> universe
```

The output tells us that line 2 changed (`2c2`), with `world` in the first file (`<`) being replaced by `universe` in the second file (`>`).

Sometimes, when new lines are added, you'll see something like:

```sh
hacker@dojo:~$ cat old
pwn
hacker@dojo:~$ cat new
pwn
college
hacker@dojo:~$ diff old new
1a2
> college
```

This tells us that after line 1 in the first file, the second file has an additional line (`1a2` means "after line 1 of file1, add line 2 of file2").

Now for your challenge!
There are two files in `/challenge`:
- `/challenge/decoys_only.txt` contains 100 fake flags
- `/challenge/decoys_and_real.txt` contains all 100 fake flags plus the one real flag

Use `diff` to find what's different between these files and get your flag!

## Solution:

After the terminal comes up, the user needs to use the diff command to find the real flag stored in `/challenge/decoys_and_real.txt`. The diff command will print only the lines which are different between `/challenge/decoys_only.txt` and `/challenge/decoys_and_real.txt` which will remove all the fake flags from the output.

#### Commands run: 

```sh
$ cd /challenge
$ diff decoys_only.txt decoys_and_real.txt
```

## Flag: 

```
pwn.college{0UrVbbjR-0aGE68LB2XpzrDYx84.01MwMDOxwSOxAzNzEzW}
```

### Notes: 

- The output of the grep command will be of the form
```
31a32
> pwn.college{0UrVbbjR-0aGE68LB2XpzrDYx84.01MwMDOxwSOxAzNzEzW}
```
- Here 31a32 means that we can get file2 from file1 if we add line 32 of file2 after line 31 of file1.

# Challenge 6: listing files

o far, we've told you which files to interact with.
But directories can have lots of files (and other directories) inside them, and we won't always be here to tell you their names.
You'll need to learn to **l**i**s**t their contents using the `ls` command!

`ls` will list files in all the directories provided to it as arguments, and in the current directory if no arguments are provided.
Observe:

```sh
hacker@dojo:~$ ls /challenge
run
hacker@dojo:~$ ls
Desktop    Downloads  Pictures  Templates
Documents  Music      Public    Videos
hacker@dojo:~$ ls /home/hacker
Desktop    Downloads  Pictures  Templates
Documents  Music      Public    Videos
hacker@dojo:~$
```

In this challenge, we've named `/challenge/run` with some random name!
List the files in `/challenge` to find it.

## Solution:

After the terminal comes up, the user needs to list the files in the `/challenge` directory to find the flag file and then run it to capture the flag.

#### Commands run: 

```sh
$ cd /challenge
$ ls
$ ./12847-renamed-run-13201
```

## Flag: 

```
pwn.college{Irw9_RDMnYwE26HvrtHyx9kR4qh.QX4IDO0wSOxAzNzEzW}
```

# Challenge 7: touching files

Of course, you can also _create_ files!
There are several ways to do this, but we'll look at a simple command here.
You can create a new, blank file by _touching_ it with the `touch` command:

```sh
hacker@dojo:~$ cd /tmp
hacker@dojo:/tmp$ ls
hacker@dojo:/tmp$ touch pwnfile
hacker@dojo:/tmp$ ls
pwnfile
hacker@dojo:/tmp$
```

It's that simple!
In this level, please create two files: `/tmp/pwn` and `/tmp/college`, and run `/challenge/run` to get your flag!

## Solution:

After the terminal comes up, the user needs to make two files using the `touch` command: `/tmp/pwn` and `/tmp/college`. Then, on running `/challenge/run`, the flag will get printed.

#### Commands run: 

```sh
$ touch /tmp/pwn
$ touch /tmp/college
$ /challenge/run
```

## Flag: 

```
pwn.college{ULWEYX_B_00oT4JtEFhNALIv3GJ.QXwMDO0wSOxAzNzEzW}
```

# Challenge 8: removing files

Files are all around you.
Like candy wrappers, there'll eventually be too many of them.
In this level, we'll learn to clean up!

In Linux, you **r**e**m**ove files with the `rm` command, as so:

```sh
hacker@dojo:~$ touch PWN
hacker@dojo:~$ touch COLLEGE
hacker@dojo:~$ ls
COLLEGE     PWN
hacker@dojo:~$ rm PWN
hacker@dojo:~$ ls
COLLEGE
hacker@dojo:~$
```

Let's practice.
This challenge will create a `delete_me` file in your home directory!
Delete it, then run `/challenge/check`, which will make sure you've deleted it and then give you the flag!

## Solution:

After the terminal comes up, the user needs to delete the `delete_me` file in the home directory and then run `/challenge/check` which will check for the file and print the flag if the file is not there.

#### Commands run: 

```sh
$ rm delete_me
$ /challenge/check
```

## Flag: 

```
pwn.college{Qqtk_XDrRLg218wWymmRvEBpTQB.QX2kDM1wSOxAzNzEzW}
```

# Challenge 9: moving files

You can also _move_ files around with the `mv` command.
The usage is simple:

```sh
hacker@dojo:~$ ls
my-file
hacker@dojo:~$ cat my-file
PWN!
hacker@dojo:~$ mv my-file your-file
hacker@dojo:~$ ls
your-file
hacker@dojo:~$ cat your-file
PWN!
hacker@dojo:~$
```

This challenge wants you to move the `/flag` file into `/tmp/hack-the-planet` (do it)!
When you're done, run `/challenge/check`, which will check things out and give the flag to you.

## Solution:

After the terminal comes up, the user needs to use the mv command to move the `/flag` file into `/tmp/hack-the-planet`. Then, on running `/challenge/check`, the flag will be printed.

#### Commands run: 

```sh
$ mv /flag /tmp/hack-the-planet
$ /challenge/check
```

## Flag: 

```
pwn.college{AszIPahdi3sF9tEs8clzS7ItOeQ.0VOxEzNxwSOxAzNzEzW}
```

# Challenge 10: hidden files

Interestingly, `ls` doesn't list _all_ the files by default.
Linux has a convention where files that start with a `.` don't show up by default in `ls` and in a few other contexts.
To view them with `ls`, you need to invoke `ls` with the `-a` flag, as so:

```sh
hacker@dojo:~$ touch pwn
hacker@dojo:~$ touch .college
hacker@dojo:~$ ls
pwn
hacker@dojo:~$ ls -a
.college        pwn
hacker@dojo:~$
```

Now, it's your turn!
Go find the flag, hidden as a dot-prepended file in `/`.

## Solution:

After the terminal comes up, the user needs to move into the root directory and run `ls -a` to find the hidden file. Afterwards, the flag can be obtained by using the cat command on the hidden file.

#### Commands run: 

```sh
$ cd /
$ ls -a
$ cat .flag-32420226245210
```

## Flag: 

```
pwn.college{QKdFs0MAwSfU3ZL--MH0QQwgph6.QXwUDO0wSOxAzNzEzW}
```

# Challenge 11: An Epic File System Quest

With your knowledge of `cd`, `ls`, and `cat`, we're ready to play a little game!

We'll start it out in `/`.
Normally:

```sh
hacker@dojo:~$ cd /
hacker@dojo:/$ ls
bin   challenge  etc   home  lib32  libx32  mnt  proc  run   srv  tmp  var
boot  dev        flag  lib   lib64  media   opt  root  sbin  sys  usr
```

That's a lot of contents!
One day, you will be quite familiar with them, but already, you might recognize the `flag` file and the `challenge` directory.

In this challenge, I have *hidden the flag*!
Here, you will use `ls` and `cat` to follow my breadcrumbs and find it!
Here's how it'll work:

0. Your first clue is in `/`. Head on over there.
1. Look around with `ls`. There'll be a file named HINT or CLUE or something along those lines!
2. `cat` that file to read the clue!
3. Depending on what the clue says, head on over to the next directory (or don't!).
4. Follow the clues to the flag!

Good luck!

## Solution:

In this challenge, the user will be sent on a wild goose chase to find the flag. The user must start from the root directory and find the clue using `ls`. This clue will lead to the location of the next clue. This will repeat a few times till the actual flag is finally found. The user must be carefull of `trapped`, `delayed`, and `hidden` clues which will have special conditions attatched to them.
- For `trapped` clues, the user must use absolute paths to find and print them without `cd`ing into thier directory.
- For `delayed` clues, the user will have to `cd` into thier directories to be able to print them.
- For `hidden` clues, the user must find them using `ls -a` and print them.

#### Commands run: 

```sh
$ cd /
$ ls
CLUE  bin  boot  challenge  dev  etc  flag  home  lib  lib32  lib64  libx32  media  mnt  nix  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
$ cat CLUE
Lucky listing!
The next clue is in: /usr/share/racket/pkgs/picturing-programs/picturing-programs/private/pictures
$ cd /usr/share/racket/pkgs/picturing-programs/picturing-programs/private/pictures
$ ls
GIST  bloch.png  calendar.png  mad_hacker.png  qbook.png  schemelogo.png  small_hieroglyphics.png  stick-figure.png
$ cat GIST
Congratulations, you found the clue!
The next clue is in: /usr/share/maxima-sage/5.42.2/share/lisp-utils

Watch out! The next clue is **trapped**. You\'ll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
$ ls /usr/share/maxima-sage/5.42.2/share/lisp-utils
MESSAGE-TRAPPED  defsystem.lisp
$ cat /usr/share/maxima-sage/5.42.2/share/lisp-utils/MESSAGE-TRAPPED 
Tubular find!
The next clue is in: /opt/pwndbg/.venv/lib/python3.8/site-packages/colored_traceback/auto/__pycache__

The next clue is **delayed** --- it will not become readable until you enter the directory with 'cd'.
$ cd /opt/pwndbg/.venv/lib/python3.8/site-packages/colored_traceback/auto/__pycache__
$ ls
TRACE  __init__.cpython-38.pyc
$ cat TRACE 
Great sleuthing!
The next clue is in: /usr/share/javascript/mathjax/unpacked/jax/output/SVG/fonts/TeX/Main/Italic

The next clue is **hidden** --- its filename starts with a '.' character. You\'ll need to look for it using special options to 'ls'.
$ cd /usr/share/javascript/mathjax/unpacked/jax/output/SVG/fonts/TeX/Main/Italic
$ ls -a
.  ..  .SECRET  BasicLatin.js  CombDiacritMarks.js  GeneralPunctuation.js  GreekAndCoptic.js  LatinExtendedA.js  LatinExtendedB.js  LetterlikeSymbols.js  Main.js
$ cat .SECRET 
Yahaha, you found me!
The next clue is in: /opt/linux/linux-5.4/include/config/strict/kernel
$ cd /opt/linux/linux-5.4/include/config/strict/kernel
$ ls
DISPATCH  rwx.h
$ cat DISPATCH 
Lucky listing!
The next clue is in: /opt/linux/linux-5.4/drivers/crypto/qat/qat_c3xxx

The next clue is **hidden** --- its filename starts with a '.' character. You\'ll need to look for it using special options to 'ls'.
$ cd /opt/linux/linux-5.4/drivers/crypto/qat/qat_c3xxx
$ ls -a
.  ..  .INSIGHT  Makefile  adf_c3xxx_hw_data.c  adf_c3xxx_hw_data.h  adf_drv.c
$ cat .INSIGHT 
Congratulations, you found the clue!
The next clue is in: /opt/kropr/target/release/.fingerprint/ropr-169c976d26298d15

Watch out! The next clue is **trapped**. You\'ll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
$ ls /opt/kropr/target/release/.fingerprint/ropr-169c976d26298d15
MEMO-TRAPPED  bin-ropr  bin-ropr.json  dep-bin-ropr  invoked.timestamp
$ cat /opt/kropr/target/release/.fingerprint/ropr-169c976d26298d15/MEMO-TRAPPED 
Yahaha, you found me!
The next clue is in: /opt/linux/linux-5.4/include/linux/iio/adc

The next clue is **delayed** --- it will not become readable until you enter the directory with 'cd'.
$ cd /opt/linux/linux-5.4/include/linux/iio/adc
$ ls
NOTE  ad_sigma_delta.h  stm32-dfsdm-adc.h
$ cat NOTE 
CONGRATULATIONS! Your perserverence has paid off, and you have found the flag!
It is: pwn.college{caGDxrefDTYwslR-_8O1RUNqx3U.QX5IDO0wSOxAzNzEzW}

```

## Flag: 

```
pwn.college{caGDxrefDTYwslR-_8O1RUNqx3U.QX5IDO0wSOxAzNzEzW}
```

# Challenge 12: making directories

We can create files.
How about directories?
You **m**a**k**e **dir**ectories using the `mkdir` command.
Then you can stick files in there!

Watch:

```sh
hacker@dojo:~$ cd /tmp
hacker@dojo:/tmp$ ls
hacker@dojo:/tmp$ ls
hacker@dojo:/tmp$ mkdir my_directory
hacker@dojo:/tmp$ ls
my_directory
hacker@dojo:/tmp$ cd my_directory
hacker@dojo:/tmp/my_directory$ touch my_file
hacker@dojo:/tmp/my_directory$ ls
my_file
hacker@dojo:/tmp/my_directory$ ls /tmp/my_directory/my_file
/tmp/my_directory/my_file
hacker@dojo:/tmp/my_directory$
```

Now, go forth and create a `/tmp/pwn` directory and make a `college` file in it!
Then run `/challenge/run`, which will check your solution and give you the flag!

## Solution:

After the terminal comes up, the user needs to make a directory `/tmp/pwn/` using the `mkdir` command and them, make a file `/tmp/pwn/college` using the `touch` command. Then, on running `/challenge/run`, the flag will get printed.

#### Commands run: 

```sh
$ mkdir /tmp/pwn
$ touch /tmp/pwn/college
$ /challenge/run
```

## Flag: 

```
pwn.college{U1DKeT1Uc17x4vwzBO2ndL5mZXJ.QXxMDO0wSOxAzNzEzW}
```

# Challenge 13: finding files

So now we know how to list, read, and create files.
But how do we find them?
We use the `find` command!

The `find` command takes optional arguments describing the search criteria and the search location.
If you don't specify a search criteria, `find` matches every file.
If you don't specify a search location, `find` uses the current working directory (`.`).
For example:

```sh
hacker@dojo:~$ mkdir my_directory
hacker@dojo:~$ mkdir my_directory/my_subdirectory
hacker@dojo:~$ touch my_directory/my_file
hacker@dojo:~$ touch my_directory/my_subdirectory/my_subfile
hacker@dojo:~$ find
.
./my_directory
./my_directory/my_subdirectory
./my_directory/my_subdirectory/my_subfile
./my_directory/my_file
hacker@dojo:~$
```

And when specifying the search location:

```sh
hacker@dojo:~$ find my_directory/my_subdirectory
my_directory/my_subdirectory
my_directory/my_subdirectory/my_subfile
hacker@dojo:~$
```

And, of course, we can specify the criteria!
For example, here, we filter by name:

```sh
hacker@dojo:~$ find -name my_subfile
./my_directory/my_subdirectory/my_subfile
hacker@dojo:~$ find -name my_subdirectory
./my_directory/my_subdirectory
hacker@dojo:~$
```

You can search the whole filesystem if you want!

```sh
hacker@dojo:~$ find / -name hacker
/home/hacker
hacker@dojo:~$
```

Now it's your turn.
I've hidden the flag in a random directory on the filesystem.
It's still called `flag`.
Go find it!

Several notes. First, there are other files named `flag` on the filesystem.
Don't panic if the first one you try doesn't have the actual flag in it.
Second, there're plenty of places in the filesystem that are not accessible to a normal user.
These will cause `find` to generate errors, but you can ignore those; we won't hide the flag there!
Finally, `find` can take a while; be patient!

## Solution:

After the terminal comes up, the user needs to use the `find` command in the root directory to search for the flag. Then, the user must go over all the found `flag` files and directories till the actual flag is found.

#### Commands run: 

```sh
$ find / -name flag
find: ‘/root’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
find: ‘/tmp/tmp.4mK6TfTSUV’: Permission denied
/usr/local/lib/python3.8/dist-packages/pwnlib/flag
/usr/share/javascript/mathjax/unpacked/jax/output/HTML-CSS/fonts/flag
find: ‘/var/cache/apt/archives/partial’: Permission denied
find: ‘/var/cache/ldconfig’: Permission denied
find: ‘/var/cache/private’: Permission denied
find: ‘/var/log/private’: Permission denied
find: ‘/var/log/apache2’: Permission denied
find: ‘/var/log/mysql’: Permission denied
find: ‘/var/lib/apt/lists/partial’: Permission denied
find: ‘/var/lib/mysql-keyring’: Permission denied
find: ‘/var/lib/php/sessions’: Permission denied
find: ‘/var/lib/private’: Permission denied
find: ‘/var/lib/mysql-files’: Permission denied
find: ‘/var/lib/mysql’: Permission denied
find: ‘/run/mysqld’: Permission denied
find: ‘/run/sudo’: Permission denied
find: ‘/proc/tty/driver’: Permission denied
find: ‘/proc/1/task/1/fd’: Permission denied
find: ‘/proc/1/task/1/fdinfo’: Permission denied
find: ‘/proc/1/task/1/ns’: Permission denied
find: ‘/proc/1/fd’: Permission denied
find: ‘/proc/1/map_files’: Permission denied
find: ‘/proc/1/fdinfo’: Permission denied
find: ‘/proc/1/ns’: Permission denied
find: ‘/proc/7/task/7/fd’: Permission denied
find: ‘/proc/7/task/7/fdinfo’: Permission denied
find: ‘/proc/7/task/7/ns’: Permission denied
find: ‘/proc/7/fd’: Permission denied
find: ‘/proc/7/map_files’: Permission denied
find: ‘/proc/7/fdinfo’: Permission denied
find: ‘/proc/7/ns’: Permission denied
/opt/pwndbg/.venv/lib/python3.8/site-packages/pwnlib/flag
/nix/store/7ns27apnvn4qj4q5c82x0z1lzixrz47p-radare2-5.9.8/share/radare2/5.9.8/flag
/nix/store/5z3sjp9r463i3siif58hq5wj5jmy5m98-python3.12-pwntools-4.13.1/lib/python3.12/site-packages/pwnlib/flag
/nix/store/5n5lp1m8gilgrsriv1f2z0jdjk50ypcn-rizin-0.7.3/share/rizin/flag
/nix/store/h88mxp2mbgyj06vypwmqpy05idhwimnp-python3.13-pwntools-4.14.1/lib/python3.13/site-packages/pwnlib/flag
/nix/store/s8b49lb0pqwvw0c6kgjbxdwxcv2bp0x4-radare2-5.9.8/share/radare2/5.9.8/flag
/nix/store/bnlabj2vsbljhp597ir29l51nrqhm89w-rizin-0.7.4/share/rizin/flag
/nix/store/1hyxipvwpdpcxw90l5pq1nvd6s6jdi5m-python3.12-pwntools-4.14.1/lib/python3.12/site-packages/pwnlib/flag
/nix/store/5qz6hgb1qzpvjrsw20wyiylx5zw8b9bk-pwntools-4.14.0/lib/python3.13/site-packages/pwnlib/flag
$ cat /usr/local/lib/python3.8/dist-packages/pwnlib/flag
cat: /usr/local/lib/python3.8/dist-packages/pwnlib/flag: Is a directory
$ cat /usr/share/javascript/mathjax/unpacked/jax/output/HTML-CSS/fonts/flag
pwn.college{IjVztEBjM40VKz1SiFFsMsg3FMW.QXyMDO0wSOxAzNzEzW}
```

## Flag: 

```
pwn.college{IjVztEBjM40VKz1SiFFsMsg3FMW.QXyMDO0wSOxAzNzEzW}
```

# Challenge 14: linking files

If you use Linux (or computers) for any reasonable length of time to do any real work, you will eventually run into some variant of the following situation: you want two programs to access the same data, but the programs expect that data to be in two different locations.
Luckily, Linux provides a solution to this quandary: _links_.

Links come in two flavors: _hard_ and _soft_ (also known as _symbolic_) links.
We'll differentiate the two with an analogy:

- A **hard** link is when you address your apartment using multiple addresses that all lead directly to the same place (e.g., `Apt 2` vs `Unit 2`).
- A **soft** link is when you move apartments and have the postal service automatically forward your mail from your old place to your new place.

In a filesystem, a file is, conceptually, an address at which the contents of that file live.
A hard link is an alternate address that indexes that data --- accesses to the hard link and accesses to the original file are completely identical, in that they immediately yield the necessary data.
A soft/symbolic link, instead, contains the original file name.
When you access the symbolic link, Linux will realize that it is a symbolic link, read the original file name, and then (typically) automatically access that file.
In most cases, both situations result in accessing the original data, but the mechanisms are different.

Hard links sound simpler to most people (case in point, I explained it in one sentence above, versus two for soft links), but they have various downsides and implementation gotchas that make soft/symbolic links, by far, the more popular alternative.

In this challenge, we will learn about symbolic links (also known as _symlinks_).
Symbolic links are created with the `ln` command with the `-s` argument, like so:

```sh
hacker@dojo:~$ cat /tmp/myfile
This is my file!
hacker@dojo:~$ ln -s /tmp/myfile /home/hacker/ourfile
hacker@dojo:~$ cat ~/ourfile
This is my file!
hacker@dojo:~$
```

You can see that accessing the symlink results in getting the original file contents!
Also, you can see the usage of `ln -s`.
Note that the original file path comes _before_ the link path in the command!

A symlink can be identified as such with a few methods.
For example, the `file` command, which takes a filename and tells you what type of file it is, will recognize symlinks:

```sh
hacker@dojo:~$ file /tmp/myfile
/tmp/myfile: ASCII text
hacker@dojo:~$ file ~/ourfile
/home/hacker/ourfile: symbolic link to /tmp/myfile
hacker@dojo:~$
```

Okay, now you try it!
In this level the flag is, as always, in `/flag`, but `/challenge/catflag` will instead read out `/home/hacker/not-the-flag`.
Use the symlink, and fool it into giving you the flag!

## Solution:

After the terminal comes up, the user needs to make a symbolic link between `/flag` and `/home/hacker/not-the-flag`. This will make it so that the flag becomes accessible to the `/challenge/catflag` program which can then be run to capture the flag.

#### Commands run: 

```sh
$ ln -s /flag /home/hacker/not-the-flag
$ /challenge/catflag
```

## Flag: 

```
pwn.college{Aql2q_TthBhhaur_F3jLBxNXC2B.QX5ETN1wSOxAzNzEzW}
```
