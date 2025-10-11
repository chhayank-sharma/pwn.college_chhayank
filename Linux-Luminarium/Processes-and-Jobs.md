
# Challenge 1: Listing Processes

First, we will learn to list running processes using the `ps` command.
Depending on whom you ask, `ps` either stands for "process snapshot" or "process status", and it lists processes.
By default, `ps` just lists the processes running in your terminal, which honestly isn't very useful:

```sh
hacker@dojo:~$ ps
    PID TTY          TIME CMD
    329 pts/0    00:00:00 bash
    349 pts/0    00:00:00 ps
hacker@dojo:~$
```

In the above example, we have the shell (`bash`) and the `ps` process itself, and that's all that's running on that specific terminal.
We also see that each process has a numerical identifier (the _Process ID_, or PID), which is a number that uniquely identifies every running process in a Linux environment.
We also see the terminal on which the commands are running (in this case, the designation `pts/0`), and the total amount of _cpu time_ that the process has eaten up so far (since these processes are very undemanding, they have yet to eat up even 1 second!).

In the majority of cases, this is all that you'll see with a default `ps`.
To make it useful, we need to pass a few arguments.

As `ps` is a very old utility, its usage is a bit of a mess.
There are two ways to specify arguments.

**"Standard" Syntax:** in this syntax, you can use `-e` to list "every" process and `-f` for a "full format" output, including arguments.
These can be combined into a single argument `-ef`.

**"BSD" Syntax:** in this syntax, you can use `a` to list processes for all users, `x` to list processes that aren't running in a terminal, and `u` for a "user-readable" output.
These can be combined into a single argument `aux`.

These two methods, `ps -ef` and `ps aux`, result in slightly different, but cross-recognizable output.

Let's try it in the dojo:

```sh
hacker@dojo:~$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
hacker         1       0  0 05:34 ?        00:00:00 /sbin/docker-init -- /bin/sleep 6h
hacker         7       1  0 05:34 ?        00:00:00 /bin/sleep 6h
hacker       102       1  1 05:34 ?        00:00:00 /usr/lib/code-server/lib/node /usr/lib/code-server --auth=none -
hacker       138     102 11 05:34 ?        00:00:07 /usr/lib/code-server/lib/node /usr/lib/code-server/out/node/entr
hacker       287     138  0 05:34 ?        00:00:00 /usr/lib/code-server/lib/node /usr/lib/code-server/lib/vscode/ou
hacker       318     138  6 05:34 ?        00:00:03 /usr/lib/code-server/lib/node --dns-result-order=ipv4first /usr/
hacker       554     138  3 05:35 ?        00:00:00 /usr/lib/code-server/lib/node /usr/lib/code-server/lib/vscode/ou
hacker       571     554  0 05:35 pts/0    00:00:00 /usr/bin/bash --init-file /usr/lib/code-server/lib/vscode/out/vs
hacker       695     571  0 05:35 pts/0    00:00:00 ps -ef
hacker@dojo:~$
```

You can see here that there are processes running for the initialization of the challenge environment (`docker-init`), a timeout before the challenge is automatically terminated to preserve computing resources (`sleep 6h` to timeout after 6 hours), the VSCode environment (several `code-server` helper processes), the shell (`bash`), and my `ps -ef` command.
It's basically the same thing with `ps aux`:

```
hacker@dojo:~$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
hacker         1  0.0  0.0   1128     4 ?        Ss   05:34   0:00 /sbin/docker-init -- /bin/sleep 6h
hacker         7  0.0  0.0   2736   580 ?        S    05:34   0:00 /bin/sleep 6h
hacker       102  0.4  0.0 723944 64660 ?        Sl   05:34   0:00 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       138  3.3  0.0 968792 106272 ?       Sl   05:34   0:07 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       287  0.0  0.0 717648 53136 ?        Sl   05:34   0:00 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       318  3.3  0.0 977472 98256 ?        Sl   05:34   0:06 /usr/lib/code-server/lib/node --dns-result-order=
hacker       554  0.4  0.0 650560 55360 ?        Rl   05:35   0:00 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       571  0.0  0.0   4600  4032 pts/0    Ss   05:35   0:00 /usr/bin/bash --init-file /usr/lib/code-server/li
hacker      1172  0.0  0.0   5892  2924 pts/0    R+   05:38   0:00 ps aux
hacker@dojo:~$
```

There are many commonalities between `ps -ef` and `ps aux`: both display the user (`USER` column), the PID, the TTY, the start time of the process (`STIME`/`START`), the total utilized CPU time (`TIME`), and the command (`CMD`/`COMMAND`).
`ps -ef` additionally outputs the _Parent Process ID_ (`PPID`), which is the PID of the process that launched the one in question, while `ps aux` outputs the percentage of total system CPU and Memory that the process is utilizing.
Plus, there's a bunch of other stuff we won't get into right now.

Anyways!
Let's practice.
In this level, I have once again renamed `/challenge/run` to a random filename, and this time made it so that you cannot `ls` the `/challenge` directory!
But I also launched it, so you can find it in the running process list, figure out the filename, and relaunch it directly for the flag!
Good luck!

**NOTE:** Both `ps -ef` and `ps aux` truncate the command listing to the width of your terminal (which is why the examples above line up so nicely on the right side of the screen.
If you can't read the whole path to the process, you might need to enlarge your terminal (or redirect the output somewhere to avoid this truncating behavior)!
Alternatively, you can pass the `w` option _twice_ (e.g., `ps -efww` or `ps auxww`) to disable the truncation.

## Solution:

In this challenge, `/challenge/run` has been renamed to some unknown name and `ls` has beeen blocked. However, an instance of it is running in the background. We can use the `ps` utility to get a list of all the running programs to see the new name of the program. Then, we can run it to obtain the flag.

#### Commands run: 

```sh
$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 17:03 ?        00:00:00 /sbin/docker-init -- /nix/var/nix/profiles/dojo-workspace/bin/dojo-init /run/dojo/bin/sleep 6h
root           7       1  0 17:03 ?        00:00:00 /run/dojo/bin/sleep 6h
root         132       1  0 17:03 ?        00:00:00 /challenge/20443-run-23195
root         135     132  0 17:03 ?        00:00:00 sleep 6h
hacker       146       1  0 17:03 ?        00:00:00 /nix/store/g0q8n7xfjp7znj41hcgrq893a9m0i474-ttyd-1.7.7/bin/ttyd --port 7681 --interface 0.0.0.0 --writable -t disableLeaveAlert true /ru
hacker       160       0  0 17:03 pts/1    00:00:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-interactive-5.2p37/bin/bash /run/dojo/bin/ssh-entrypoint
hacker       166     160  0 17:03 pts/1    00:00:00 /run/dojo/bin/bash --login
hacker       219     166  0 19:06 pts/1    00:00:00 ps -ef

$ /challenge/20443-run-23195
```

or

```sh
$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   1056   640 ?        Ss   17:03   0:00 /sbin/docker-init -- /nix/var/nix/profiles/dojo-workspace/bin/dojo-init /run/dojo/bin/sleep 6h
root           7  0.0  0.0 231708  2560 ?        S    17:03   0:00 /run/dojo/bin/sleep 6h
root         132  0.0  0.0   4132  2560 ?        S    17:03   0:00 /challenge/20443-run-23195
root         135  0.0  0.0   2744  1600 ?        S    17:03   0:00 sleep 6h
hacker       146  0.0  0.0  36972 21760 ?        S    17:03   0:00 /nix/store/g0q8n7xfjp7znj41hcgrq893a9m0i474-ttyd-1.7.7/bin/ttyd --port 7681 --interface 0.0.0.0 --writable -t disableLeav
hacker       160  0.0  0.0 231576  3520 pts/1    Ss   17:03   0:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-interactive-5.2p37/bin/bash /run/dojo/bin/ssh-entrypoint
hacker       166  0.0  0.0 231940  4160 pts/1    S    17:03   0:00 /run/dojo/bin/bash --login
hacker       220  0.0  0.0 233600  3840 pts/1    R+   19:06   0:00 ps aux

$ /challenge/20443-run-23195
```

## Flag: 

```
pwn.college{EFFPG19ADaQCkNrdiOjZ_4xdh5O.QX4MDO0wSOxAzNzEzW}
```

# Challenge 2: Killing Processes

You've launched processes, you've viewed processes, now you will learn to _terminate_ processes!
In Linux, this is done using the aggressively-named `kill` command.
With default options (which is all we'll cover in this level), `kill` will terminate a process in a way that gives it a chance to get its affairs in order before ceasing to exist.

Let's say you had a pesky `sleep` process (`sleep` is a program that simply hangs out for the number of seconds specified on the commandline, in this case, 1337 seconds) that you launched in another terminal, like so:

```sh
hacker@dojo:~$ sleep 1337
```

How do we get rid of it?
You use `kill` to terminate it by passing the process identifier (the `PID` from `ps`) as an argument, like so:

```sh
hacker@dojo:~$ ps -e | grep sleep
 342 pts/0    00:00:00 sleep
hacker@dojo:~$ kill 342
hacker@dojo:~$ ps -e | grep sleep
hacker@dojo:~$
```

Now, it's time to terminate your first process!
In this challenge, `/challenge/run` will refuse to run while `/challenge/dont_run` is running!
You must find the `dont_run` process and `kill` it.
If you fail, `pwn.college` will disavow all knowledge of your mission.
Good luck.

## Solution:

In this challenge, there is a program `/challenge/dont_run` which prevents `/challenge/run` from running. To get the flag, we first need to identify the `PID` of `/challenge/dont_run` using `ps`. Then, we can stop the `/challenge/dont_run` using the `kill` command. Now we can run `/challenge/run` to capture the flag.

#### Commands run: 

```sh
$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 19:15 ?        00:00:00 /sbin/docker-init -- /nix/var/nix/profiles/dojo-workspace/bin/dojo-init /run/dojo/bin/sleep 6h
root           7       1  0 19:15 ?        00:00:00 /run/dojo/bin/sleep 6h
root         135       1  0 19:15 ?        00:00:00 su -c /challenge/.launcher hacker
hacker       136     135  0 19:15 ?        00:00:00 /challenge/dont_run
hacker       137     136  0 19:15 ?        00:00:00 sleep 6h
hacker       139       0  0 19:15 pts/0    00:00:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-interactive-5.2p37/bin/bash /run/dojo/bin/ssh-entrypoint
hacker       145     139  0 19:15 pts/0    00:00:00 /run/dojo/bin/bash --login
hacker       163       1  0 19:15 ?        00:00:00 /nix/store/g0q8n7xfjp7znj41hcgrq893a9m0i474-ttyd-1.7.7/bin/ttyd --port 7681 --interface 0.0.0.0 --writable -t disableLeaveAlert true /ru
hacker       167     163  0 19:15 pts/1    00:00:00 /run/dojo/bin/bash --login
hacker       180     145  0 19:16 pts/0    00:00:00 ps -ef

$ kill 136

$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 19:15 ?        00:00:00 /sbin/docker-init -- /nix/var/nix/profiles/dojo-workspace/bin/dojo-init /run/dojo/bin/sleep 6h
root           7       1  0 19:15 ?        00:00:00 /run/dojo/bin/sleep 6h
hacker       137       1  0 19:15 ?        00:00:00 sleep 6h
hacker       139       0  0 19:15 pts/0    00:00:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-interactive-5.2p37/bin/bash /run/dojo/bin/ssh-entrypoint
hacker       145     139  0 19:15 pts/0    00:00:00 /run/dojo/bin/bash --login
hacker       163       1  0 19:15 ?        00:00:00 /nix/store/g0q8n7xfjp7znj41hcgrq893a9m0i474-ttyd-1.7.7/bin/ttyd --port 7681 --interface 0.0.0.0 --writable -t disableLeaveAlert true /ru
hacker       167     163  0 19:15 pts/1    00:00:00 /run/dojo/bin/bash --login
hacker       181     145  0 19:17 pts/0    00:00:00 ps -ef

$ /challenge/run
```

## Flag: 

```
pwn.college{gBnRsgAAVcW5G-U-1N2_aHm5NOH.QXyQDO0wSOxAzNzEzW}
```

# Challenge 3: Interrupting Processes

You've learned how to kill other processes with the `kill` command, but sometimes you just want to get rid of the process that's clogging up your terminal!
Luckily, terminals have a hotkey for this: `Ctrl-C` (e.g., holding down the `Ctrl` key and pressing `C`) sends an "interrupt" to whatever application is waiting on input from the terminal and, typically, this causes the application to cleanly exit.

Try it here!
`/challenge/run` will refuse to give you the flag until you interrupt it.
Good luck!

---
For the very interested, check out this [article about terminals and "control codes"](https://catern.com/posts/terminal_quirks.html) (such as `Ctrl-C`).

## Solution:

In this challenge, to get the flag, we need to run the `/challenge/run` program and then interrupt it by pressing `Ctrl+C`. This will print the flag.

#### Commands run: 

```sh
$ /challenge/run
```
Then press `Ctrl+C`

## Flag: 

```
pwn.college{4v7WIQSNgBlE62wjJK_z8p-ke9O.QXzQDO0wSOxAzNzEzW}
```

# Challenge 4: Killing Misbehaving Processes

Sometimes, misbehaving processes can interfere with your work.
These processes might need to be killed...

In this challenge, there's a decoy process that's hogging a critical resource - a named pipe (FIFO) at `/tmp/flag_fifo` into which (like in the [Practicing Piping](/linux-luminarium/piping) FIFO challenge) `/challenge/run` wants to write your flag.
You need to `kill` this process.

Your general workflow should be:

1. Check what processes are running.
2. Find `/challenge/decoy` in the list and figure out its process ID.
3. `kill` it.
4. Run `/challenge/run` to get the flag without being overwhelmed by decoys (you don't need to redirect its output; it'll write to the FIFO on its own).

Good luck!

----
**NOTE:**
You might see a few decoy flags show up even after killing the decoy process.
This happens because Linux pipes are _buffered_: conceptually, they have a sort of length through which data flows, and you might kill the decoy process while data is in the pipe.
That data, having already entered the pipe, will proceed to the other end (your `cat`).
If you wait a second, you'll see the decoys stop, and then you can `/challenge/run` and win!


## Solution:

This challenge will require two terminals to be accessible at the same time. For this, one can either use the Desktop or VSCode mode on the pwn.college website. Or, to do it from within the terminal, it is possible to use the `tmux` program. `tmux` is a **t**erminal **mu**ltiple**x**er which allows for running commands in parallel without acess to multiple terminal interfaces. To do it in this manner, simply enter the `tmux` command. This should open a tmux pane within the terminal. Then, to split it into two, press and release the prefix key, which is `Ctrl+b` by default. Then, press `"` to create a new pane horizontally or press `%` to create a new pane vertically. To move between the panes, use the prefix key (`Ctrl+b`) followed by the corresponding arrow key (`Up`, `Down`, `Left`, `Right`).

First, we must use `ps` to find the `PID` of the `/challenge/decoy` program which prevents `/challenge/run` from being able to write to the `flag_fifo` named pipe. We can then kill the `/challenge/decoy` program. After this, we need two terminals. One to write the flag into the named pipe using `/challenge/run`, and another to actually print the flag using the `cat` command. If this is done properly, we should be able to capture the flag.

#### Commands run: 

```sh
$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 19:27 ?        00:00:00 /sbin/docker-init -- /nix/var/nix/profiles/dojo-workspace/bin/dojo-init /run/dojo/bin/sleep 6h
root           7       1  0 19:27 ?        00:00:00 /run/dojo/bin/sleep 6h
root         137       1  0 19:27 ?        00:00:00 /bin/bash /challenge/.init
root         138       1  0 19:27 ?        00:00:00 /bin/bash /challenge/.init
root         139       1  0 19:27 ?        00:00:00 su -c exec /challenge/decoy > /tmp/flag_fifo hacker
root         140     137  0 19:27 ?        00:00:00 sleep 6h
root         141     138  0 19:27 ?        00:00:00 sleep 6h
hacker       142     139  0 19:27 ?        00:00:00 /usr/bin/python /challenge/decoy
hacker       153       1  0 19:27 ?        00:00:00 /nix/store/g0q8n7xfjp7znj41hcgrq893a9m0i474-ttyd-1.7.7/bin/ttyd --port 7681 --interface 0.0.0.0 --writable -t disableLeaveAlert true /ru
hacker       157     153  0 19:28 pts/0    00:00:00 /run/dojo/bin/bash --login
hacker       167       0  0 19:28 pts/1    00:00:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-interactive-5.2p37/bin/bash /run/dojo/bin/ssh-entrypoint
hacker       173     167  0 19:28 pts/1    00:00:00 /run/dojo/bin/bash --login
hacker       183     173  0 19:28 pts/1    00:00:00 ps -ef

$ kill 142

$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 19:27 ?        00:00:00 /sbin/docker-init -- /nix/var/nix/profiles/dojo-workspace/bin/dojo-init /run/dojo/bin/sleep 6h
root           7       1  0 19:27 ?        00:00:00 /run/dojo/bin/sleep 6h
root         137       1  0 19:27 ?        00:00:00 /bin/bash /challenge/.init
root         138       1  0 19:27 ?        00:00:00 /bin/bash /challenge/.init
root         140     137  0 19:27 ?        00:00:00 sleep 6h
root         141     138  0 19:27 ?        00:00:00 sleep 6h
hacker       153       1  0 19:27 ?        00:00:00 /nix/store/g0q8n7xfjp7znj41hcgrq893a9m0i474-ttyd-1.7.7/bin/ttyd --port 7681 --interface 0.0.0.0 --writable -t disableLeaveAlert true /ru
hacker       157     153  0 19:28 pts/0    00:00:00 /run/dojo/bin/bash --login
hacker       167       0  0 19:28 pts/1    00:00:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-interactive-5.2p37/bin/bash /run/dojo/bin/ssh-entrypoint
hacker       173     167  0 19:28 pts/1    00:00:00 /run/dojo/bin/bash --login
hacker       184     173  0 19:28 pts/1    00:00:00 ps -ef

$ tmux
```

Terminal 1:
```sh
$ cat /tmp/flag_fifo
```

Terminal 2:
```sh
/challenge/run
```

## Flag: 

```
│pwn.college{gh8ncio7VmAlYit1MM7QUl3syOF.0FNzMDOxwSOxAzNzEzW}
```

# Challenge 5: Suspending Processes

You have learned to interrupt processes with `Ctrl-C`, but there are less drastic measures you can use to get your terminal back!
You can _suspend_ processes to the background with `Ctrl-Z`.
In this level, we'll explore how this works and, in the next level, we'll figure out how to _resume_ those suspended processes!

This level's `run` wants to see another copy of itself running _and using the same terminal_.
How?
Use the terminal to launch it, then suspend it, then launch another copy while the first is suspended!


## Solution:

In this challenge, we need to have two copies of `/challenge/run` running at the same time in the same terminal session. To do this, we have to start one copy of `/challenge/run`, then we need to suspend it by pressing `Ctrl+Z` and run a second copy of `/challenge/run`. This should allow us to capture the flag.

#### Commands run: 

```sh
$ /challenge/run 
I'll only give you the flag if there's already another copy of me running in 
this terminal... Let's check!

UID          PID    PPID  C STIME TTY          TIME CMD
root         174     135  0 19:39 pts/0    00:00:00 bash /challenge/run
root         176     174  0 19:39 pts/0    00:00:00 ps -f

I don't see a second me!

To pass this level, you need to suspend me and launch me again! You can 
background me with Ctrl-Z or, if you're not ready to do that for whatever 
reason, just hit Enter and I'll exit!
```

Press `Ctrl-Z`

```sh
^Z
[1]+  Stopped                 /challenge/run

$ /challenge/run 
I'll only give you the flag if there's already another copy of me running in 
this terminal... Let's check!

UID          PID    PPID  C STIME TTY          TIME CMD
root         174     135  0 19:39 pts/0    00:00:00 bash /challenge/run
root         181     135  0 19:39 pts/0    00:00:00 bash /challenge/run
root         183     181  0 19:39 pts/0    00:00:00 ps -f

Yay, I found another version of me! Here is the flag:
pwn.college{kjy0n9IjnhSCOICmJZJyOxMD_Wc.QX1QDO0wSOxAzNzEzW}
```

## Flag: 

```
pwn.college{kjy0n9IjnhSCOICmJZJyOxMD_Wc.QX1QDO0wSOxAzNzEzW}
```

# Challenge 6: Resuming Processes

Usually, when you suspend processes, you'll want to resume them at some point.
Otherwise, why not just terminate them?
To resume processes, your shell provides the `fg` command, a builtin that takes the suspended process, resumes it, and puts it back in the foreground of your terminal.

Go try it out!
This challenge's `run` needs you to suspend it, then resume it.
Good luck!

## Solution:

In this challenge, to get the flag, we need to run `/challenge/run`, suspend it by pressing `Ctrl+Z` and then resume it to the foreground using the `fg` command. Doing this will give us the flag.

#### Commands run: 

```sh
$ /challenge/run 
Let's practice resuming processes! Suspend me with Ctrl-Z, then resume me with 
the 'fg' command! Or just press Enter to quit me!
```

Press `Ctrl+Z`

```sh
^Z
[1]+  Stopped                 /challenge/run

$ fg
/challenge/run
I'm back! Here's your flag:
pwn.college{8na82L3ewLcqQh1trkqrspm4ZQ-.QX2QDO0wSOxAzNzEzW}
Don't forget to press Enter to quit me!
```

Press `Enter`
```sh

Goodbye!
```

## Flag: 

```
pwn.college{8na82L3ewLcqQh1trkqrspm4ZQ-.QX2QDO0wSOxAzNzEzW}
```

# Challenge 7: Backgrounding Processes

You've resumed processes in the _foreground_ with the `fg` command.
You can also resume processes in the _background_ with the `bg` command!
This will allow the process to keep running, while giving you your shell back to invoke more commands in the meantime.

This level's `run` wants to see another copy of itself running, _not suspended_, and using the same terminal.
How?
Use the terminal to launch it, then suspend it, then _background_ it with `bg` and launch another copy while the first is running in the background!

---

**ARCANUM:**
If you're interested in some deeper details, check out how to view the differences between suspended and backgrounded properties!
Allow me to demonstrate.
First, let's suspend a `sleep`:

```sh
hacker@dojo:~$ sleep 1337
^Z
[1]+  Stopped                 sleep 1337
hacker@dojo:~$
```

The `sleep` process is now _suspended_ in the background.
We can see this with `ps` by enabling the `stat` column output with the `-o` option:

```sh
hacker@dojo:~$ ps -o user,pid,stat,cmd
USER         PID STAT CMD
hacker       702 Ss   bash
hacker       762 T    sleep 1337
hacker       782 R+   ps -o user,pid,stat,cmd
hacker@dojo:~$ 
```

See that `T`?
That means that the process is suspended due to our `Ctrl-Z`.
The `S` in `bash`'s `STAT` column means that `bash` is sleeping while waiting for input.
The `R` in `ps`'s column means that it's actively running, and the `+` means that it's in the foreground!

Watch what happens when we resume `sleep` in the background:

```sh
hacker@dojo:~$ bg
[1]+ sleep 1337 &
hacker@dojo:~$ ps -o user,pid,stat,cmd
USER         PID STAT CMD
hacker       702 Ss   bash
hacker       762 S    sleep 1337
hacker      1224 R+   ps -o user,pid,stat,cmd
hacker@dojo:~$
```

Boom!
The `sleep` now has an `S`.
It's sleeping while, well, sleeping, but it's not suspended!
It's also in the _background_ and thus doesn't have the `+`.

## Solution:

In this challenge, we need to have two copies of `/challenge/run` running at the same time in the same terminal session but neither should be suspended. To do this, we need to run `/challenge/run`, suspend it by pressing `Ctrl+Z` and then resume it to the background using the `bg` command. Now, the first copy of the `/challenge/run` will be running in the background and we can launch a second copy bu running `/challenge/run` again. Doing this will give us the flag.

#### Commands run: 

```sh
$ /challenge/run
I'll only give you the flag if there's already another copy of me running *and 
not suspended* in this terminal... Let's check!

UID          PID STAT CMD
root         163 S+   bash /challenge/run
root         165 R+   ps -o user=UID,pid,stat,cmd

I don't see a second me!

To pass this level, you need to suspend me, resume the suspended process in the 
background, and then launch a new version of me! You can background me with 
Ctrl-Z (and resume me in the background with 'bg') or, if you're not ready to 
do that for whatever reason, just hit Enter and I'll exit!
```

Press `Ctrl-Z`

```sh
^Z
[1]+  Stopped                 /challenge/run

$ bg
[1]+ /challenge/run &
$ 


Yay, I'm now running the background! Because of that, this text will probably 
overlap weirdly with the shell prompt. Don't panic; just hit Enter a few times 
to scroll this text out.
```

Press `Enter`

```sh
$ /challenge/run
I'll only give you the flag if there's already another copy of me running *and 
not suspended* in this terminal... Let's check!

UID          PID STAT CMD
root         163 S    bash /challenge/run
root         173 S    sleep 6h
root         174 S+   bash /challenge/run
root         176 R+   ps -o user=UID,pid,stat,cmd

Yay, I found another version of me running in the background! Here is the flag:
pwn.college{IHrTz7Ig-zcv6Lagb9evCCBsoD7.QX3QDO0wSOxAzNzEzW}
```

## Flag: 

```
pwn.college{IHrTz7Ig-zcv6Lagb9evCCBsoD7.QX3QDO0wSOxAzNzEzW}
```

# Challenge 8: Foregrounding Processes

Imagine that you have a backgrounded process, and you want to mess with it some more.
What do you do?
Well, you can foreground a backgrounded process with `fg` just like you foreground a suspended process!
This level will walk you through that!

## Solution:

In this challenge, we need to run the `/challenge/run` program, suspend it by pressing `Ctrl+Z` and then resume it to the background using `bg`. After this, we need to foreground it again but without re-suspending it. This can be done by just using the `fg` commmand. This will cause the flag to be printed to the terminal.

#### Commands run: 

```sh
$ /challenge/run
To pass this level, you need to suspend me, resume the suspended process in the 
background, and *then* foreground it without re-suspending it! You can 
background me with Ctrl-Z (and resume me in the background with 'bg') or, if 
you're not ready to do that for whatever reason, just hit Enter and I'll exit!
```

Press `Ctrl+Z`

```sh
^Z
[1]+  Stopped                 /challenge/run

$ bg
[1]+ /challenge/run &
$ 


Yay, I'm now running the background! Because of that, this text will probably 
overlap weirdly with the shell prompt. Don't panic; just hit Enter a few times 
to scroll this text out. After that, resume me into the foreground with 'fg'; 
I'll wait.
```

Press `Enter`

```sh
$ fg
/challenge/run
YES! Great job! I'm now running in the foreground. Hit Enter for your flag!
```

Press `Enter`

```sh

pwn.college{oO7yTmzCf0uiA8yNXmlF-lGHMl2.QX4QDO0wSOxAzNzEzW}
```

## Flag: 

```
pwn.college{oO7yTmzCf0uiA8yNXmlF-lGHMl2.QX4QDO0wSOxAzNzEzW}
```

# Challenge 9: Starting Backgrounded Processes

Of course, you don't have to suspend processes to background them: you can start them backgrounded right off the bat!
It's easy; all you have to do is append a `&` to the command, like so:

```sh
hacker@dojo:~$ sleep 1337 &
[1] 1771
hacker@dojo:~$ ps -o user,pid,stat,cmd
USER         PID STAT CMD
hacker      1709 Ss   bash
hacker      1771 S    sleep 1337
hacker      1782 R+   ps -o user,pid,stat,cmd
hacker@dojo:~$ 
```

Here, `sleep` is actively running in the background, _not_ suspended.
Now it's your turn to practice!
Launch `/challenge/run` backgrounded for the flag!

## Solution:

In this challenge, instead of backgrounding `/challenge/run` after starting it normally, we need to start it in a backgrounded state. This can be done by postfixing `/challenge/run` with the `&` symbol. Doing this properly will print the flag to the terminal.

#### Commands run: 

```sh
$ /challenge/run &
[1] 163
hacker@processes~starting-backgrounded-processes:~$ 


Yay, you started me in the background! Because of that, this text will probably 
overlap weirdly with the shell prompt, but you're used to that by now...

Anyways! Here is your flag!
pwn.college{Ye8h3PiN6NyAJ1B2qLQrBQao8gF.QX5QDO0wSOxAzNzEzW}
```

Press `Enter`

```sh

[1]+  Done                    /challenge/run
```

## Flag: 

```
pwn.college{Ye8h3PiN6NyAJ1B2qLQrBQao8gF.QX5QDO0wSOxAzNzEzW}
```

# Challenge 10: Process Exit Codes

Every shell command, including every program and every builtin, exits with an _exit code_ when it finishes running and terminates.
This can be used by the shell, or the user of the shell (that's you!) to check if the process succeeded in its functionality (this determination, of course, depends on what the process is supposed to do in the first place).

You can access the exit code of the most recently-terminated command using the special `?` variable (don't forget to prepend it with `$` to read its value!):

```sh
hacker@dojo:~$ touch test-file
hacker@dojo:~$ echo $?
0
hacker@dojo:~$ touch /test-file
touch: cannot touch '/test-file': Permission denied
hacker@dojo:~$ echo $?
1
hacker@dojo:~$
```

As you can see, commands that succeed typically return `0` and commands that fail typically return a non-zero value, most commonly `1` but sometimes an error code that identifies a specific failure mode.

In this challenge, you must retrieve the exit code returned by `/challenge/get-code` and then run `/challenge/submit-code` with that error code as an argument.
Good luck!

## Solution:

In this challenge, we need to run `/challenge/get-code` and get its exit code by running `echo $?`.  Then, we need to run `/challenge/submit-code` with that exit code as argument. Doing this properly should give us the flag.

#### Commands run: 

```sh
$ /challenge/get-code 
Exiting with an error code!

$ echo $?
124

$ /challenge/submit-code 124
CORRECT! Here is your flag:
pwn.college{0uR7EvKDXrG-WhQ8wQaA7V5e0Fw.QX5YDO1wSOxAzNzEzW}
```

## Flag: 

```
pwn.college{0uR7EvKDXrG-WhQ8wQaA7V5e0Fw.QX5YDO1wSOxAzNzEzW}
```
