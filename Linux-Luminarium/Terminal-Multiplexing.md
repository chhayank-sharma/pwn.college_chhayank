
# Challenge 1: Launching Screen

Let's dive right in!

`screen` is a program that creates virtual terminals inside your terminal.
It's somewhat like having multiple browser tabs, but for your command line!

Starting screen is super simple:

```sh
hacker@dojo:~$ screen
```

That's it!
You're now inside a screen session.
It looks _exactly_ like a terminal, but there are new capabilities there, waiting to be discovered.

For this challenge, we've hooked things up so that just launching screen will get you the flag.
Easy!

----
**NOTE:**
When you're done with your command line, type `exit` or press `Ctrl-D` to leave the screen session.
Then screen will terminate and return you to your _original_ shell.

## Solution:

In this challenge, simply running the `screen` command will give us the flag.

#### Commands run: 

```sh
$ screen
```

Press `Enter`

## Flag: 

```
pwn.college{M8C1X3VPDIhr59uTPYs5fu4bRFE.0VN4IDOxwSOxAzNzEzW}
```

# Challenge 2: Detaching and Attaching

Now we'll start digging in with the magic of _detaching_!

Imagine you're working on something important over a remote connection, and your connection drops.
With a normal terminal (outside of this awesome dojo environment), everything's gone.
With screen, your work keeps running, and you can _reattach_ later!

You can also _detach_ on purpose, which we'll do in this challenge.
You detach by pressing `Ctrl-A`, followed by `d` (for **d**etach).
This leaves your session running in the background while you return to your normal terminal.

```sh
hacker@dojo:~$ screen
[doing some work...]
[Press Ctrl-A, then d]
[detached from 12345.pts-0.hostname]
hacker@dojo:~$ 
```

To **r**eattach, you can use the `-r` argument to `screen`:

```sh
hacker@dojo:~$ screen -r
```

For this challenge, you'll need to:

1. Launch screen
2. Detach from it.
3. Run `/challenge/run` (this will secretly send the flag to your detached session!)
4. Reattach to see your prize

----
**FUN FACT:**
`Ctrl-A` is `screen`'s activation key for all of its shortcuts in its default configuration.
All `screen` functionality is activated by some command combination starting with `Ctrl-A`.

**HINT:**
Remember: Hold Ctrl and press A, then release both and press d.

**HINT:**
If you see `[detached from...]`, you did it right!

## Solution:

In this challenge, we need to run `screen` and then detach it by pressing `Ctrl+A` followed by `D`. If we now run `/challenge/run`, it will print the flag onto the detached screen. To read it, we must reatach the screen by running `screen -r`. Doing this properly should allow us to capture the flag.

#### Commands run: 

```sh
$ screen
```

Press `Enter`
Press `Ctrl+A` followed by `D`

```sh
[detached from 178.pts-0.terminal-multiplexing~detaching-and-attaching]

$ /challenge/run
Found detached screen session: 178.pts-0.terminal-multiplexing~detaching-and-attaching
Sending flag to your screen session...

Flag sent! Now reattach to your screen session with:

  screen -r

You'll find the flag waiting for you there!

$ screen -r
```

## Flag: 

```
pwn.college{EdxNzA3VC3eyYTlIsBtIvoK_r2K.0lN4IDOxwSOxAzNzEzW}
```

# Challenge 3: Finding Sessions

Time for some screen detective work!

If you become an avid screen user, you will inevitably end up with multiple sessions running.
How do you find the right one to reattach to?

Well, we can list them:

```sh
hacker@dojo:~$ screen -ls
There are screens on:
        23847.mysession   (Detached)
        23851.goodwork    (Detached)
        23855.morework    (Detached)
3 Sockets in /run/screen/S-hacker.
```

The identifiers of the sessions are the PID of each respective screen process, a dot, and the name of the screen session.
To attach to a specific one, you use its name or its PID by giving it as an argument to `screen -r`.

```sh
hacker@dojo:~$ screen -r goodwork
```

In this challenge, we've created three screen sessions for you.
One of them contains the flag.
The other two are decoys!

You'll need to check each one until you find it.
Don't forget to detach (Ctrl-A d) before trying the next session!

## Solution:

In this challenge, 3 `screen` sessions have been created out of which only 1 contains the flag. we must use `screen -ls` to list all the sessiona and then reattach them one by one till we find the flag.

#### Commands run: 

```sh
$ screen -ls
There are screens on:
        184.pts-1.terminal-multiplexing~launching-screen        (Remote or dead)
        144.session_38e731f0d6c62980    (Detached)
        147.session_592f60c9f8b971df    (Detached)
        150.session_dec8922f52ae7929    (Detached)
4 Sockets in /home/hacker/.screen.

$ screen -r session_38e731f0d6c62980 
```

No flag found, Press `Ctrl+A` followed by `D`

```sh
[detached from 144.session_38e731f0d6c62980]

$ screen -r 147.session_592f60c9f8b971df
```

No flag found, Press `Ctrl+A` followed by `D`

```sh
[detached from 147.session_592f60c9f8b971df]

$ screen -r 150.session_dec8922f52ae7929

```

## Flag: 

```
pwn.college{4mXty82Oy3dAVi5IDK8N6341NNM.01N4IDOxwSOxAzNzEzW}
```

# Challenge 4: Switching Windows

Okay, so far, `screen` is just a weird sort of terminal-with-a-terminal.
But it can be much more!

Inside a single screen session, you can have multiple windows, like your browser has multiple tabs.
This can be super handy for organizing different tasks!

These windows are handled with different keyboard shortcuts, all starting with `Ctrl-A`:

- `Ctrl-A c` - Create a new window
- `Ctrl-A n` - Next window  
- `Ctrl-A p` - Previous window
- `Ctrl-A 0` through `Ctrl-A 9` - Jump directly to window 0-9
- `Ctrl-A "` - bring up a selection menu of all of the windows

For this challenge, we've set up a screen session with two windows:

- Window 0 has... well, you'll have to switch there to find out!
- Window 1 has a welcome message

Attach to the session with `screen -r`, then use one of the key combinations above to switch to Window 1.
Go get that flag!

## Solution:

In this challenge, a `screen` session has been setup with 2 windows. When we run `screen -r`, it will reattach us to window 1. to capture the flag, we must switch to windows 0 by pressing `Ctrl+A` followed by `0`.

#### Commands run: 

```sh
$ screen -r
```

```sh
 cat <<MSG
Welcome to the window switching challenge!
You are currently in window 1.
The flag is hidden in window 0.
Use Ctrl-A 0 to switch to window 0!
MSG
hacker@terminal-multiplexing~switching-windows:~$  cat <<MSG
> Welcome to the window switching challenge!
> You are currently in window 1.
> The flag is hidden in window 0.
> Use Ctrl-A 0 to switch to window 0!
> MSG
Welcome to the window switching challenge!
You are currently in window 1.
The flag is hidden in window 0.
Use Ctrl-A 0 to switch to window 0!
hacker@terminal-multiplexing~switching-windows:~$
```

Press `Ctrl+A` followed by `0`

```sh
hacker@terminal-multiplexing~switching-windows:~$  cat <<MSG
> Excellent work! You found window 0!
> Here is your flag: pwn.college{AMEpgENp6UF89Hd5w4iZcW8R5kC.0FO4IDOxwSOxAzNzEzW}
> MSG
Excellent work! You found window 0!
Here is your flag: pwn.college{AMEpgENp6UF89Hd5w4iZcW8R5kC.0FO4IDOxwSOxAzNzEzW}
hacker@terminal-multiplexing~switching-windows:~$
```

## Flag: 

```
pwn.college{AMEpgENp6UF89Hd5w4iZcW8R5kC.0FO4IDOxwSOxAzNzEzW}
```

# Challenge 5: Detaching and Attaching(tmux)

Let's try the same thing with `tmux`!

`tmux` (terminal multiplexer) is screen's younger, more modern cousin.
It does all the same things but with some different key bindings.
The biggest difference?
Instead of `Ctrl-A`, tmux uses `Ctrl-B` as its command prefix.

So to detach from tmux, you press `Ctrl-B` followed by `d`.

```console
hacker@dojo:~$ tmux
[doing some work...]
[Press Ctrl-B, then d]
[detached (from session 0)]
hacker@dojo:~$ 
```

The commands also differ:
- `tmux ls` - List sessions
- `tmux attach` or `tmux a` - Reattach to session

For this challenge:
1. Launch tmux
2. Detach from it.
3. Run `/challenge/run` (this will send the flag to your detached session!)
4. Reattach to see your prize

## Solution:

In this challenge, we need to run `tmux` and then detach it by pressing `Ctrl+B` followed by `D`. If we now run `/challenge/run`, it will print the flag onto the detached screen. To read it, we must reatach the screen by running `tmux attach`. Doing this properly should allow us to capture the flag.

#### Commands run: 

```sh
$ tmux
```

Press `Ctrl+B` followed by `D`

```sh
[detached (from session 0)]

$ /challenge/run 
Found detached tmux session: 0
Sending flag to your tmux session...

Flag sent! Now reattach to your tmux session with:
  tmux attach

You'll find the flag waiting for you there!

$ tmux attach
```

## Flag: 

```
pwn.college{U4rFcLrJv3XmwM2TMSne_PkX50A.0VO4IDOxwSOxAzNzEzW}
```

# Challenge 6: Switching Windows(tmux)

Let's learn to navigate windows in tmux!

Just like screen, tmux has windows.
The key combos are different, but the concept is the same:

- `Ctrl-B c` - Create a new window
- `Ctrl-B n` - Next window  
- `Ctrl-B p` - Previous window
- `Ctrl-B 0` through `Ctrl-B 9` - Jump to window 0-9
- `Ctrl-B w` - See a nice window picker

Tmux shows your windows at the bottom in a status bar that looks like:
```
[0] 0:bash* 1:bash
```

The `*` shows your current window, and each entry also shows the process that the window was created to run.

We've created a tmux session with two windows:
- Window 0 has the flag!
- Window 1 has your warm welcome.

Go get that flag!

## Solution:

In this challenge, a `tmux` session has been setup with 2 windows. When we run `tmux attach`, it will reattach us to window 1. to capture the flag, we must switch to windows 0 by pressing `Ctrl+B` followed by `0`.

#### Commands run: 

```sh
$ tmux attach
```

```sh
 cat <<MSG
Welcome to the tmux window switching challenge!
You are currently in window 1.
The flag is hidden in window 0.
Use Ctrl-B 0 to switch to window 0!
MSG
hacker@terminal-multiplexing~switching-windows-tmux:~$  cat <<MSG
> Welcome to the tmux window switching challenge!
> You are currently in window 1.
> The flag is hidden in window 0.
> Use Ctrl-B 0 to switch to window 0!
> MSG
Welcome to the tmux window switching challenge!
You are currently in window 1.
The flag is hidden in window 0.
Use Ctrl-B 0 to switch to window 0!
hacker@terminal-multiplexing~switching-windows-tmux:~$ 
```

Press `Ctrl+B` followed by `0`

```sh
hacker@terminal-multiplexing~switching-windows-tmux:~$  cat <<MSG
> Excellent work! You found window 0!
> Here is your flag: pwn.college{w92FGzQeW-CO_RCaVVt5ehfXaPx.0FM5IDOxwSOxAzNzEzW}
> MSG
Excellent work! You found window 0!
Here is your flag: pwn.college{w92FGzQeW-CO_RCaVVt5ehfXaPx.0FM5IDOxwSOxAzNzEzW}
hacker@terminal-multiplexing~switching-windows-tmux:~$ 
```

## Flag: 

```
pwn.college{w92FGzQeW-CO_RCaVVt5ehfXaPx.0FM5IDOxwSOxAzNzEzW}
```
