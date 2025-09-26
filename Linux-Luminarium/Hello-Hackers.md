
# Challenge 1: Intro to Commands

In this challenge, you will invoke your first command!
When you type a command and hit enter, the command will be invoked, as so:

```sh
hacker@dojo:~$ whoami
hacker
hacker@dojo:~$
```

Here, the user executed the `whoami` command, which simply prints the username (`hacker`) to the terminal.
When the command terminates, the shell once again displays the prompt, ready for the next command.

In this level, invoke the `hello` command to get the flag!
Keep in mind: commands in Linux are case sensitive: `hello` is different from `HELLO`.

## Solution:

After the terminal comes up, the user needs to invoke the `hello` command, which prints the flag.

#### Commands run: 

```sh
$ hello
```

## Flag: 

```
pwn.college{4W0jWHmZXg2zH1H9h0QPT03RWEg.QX3YjM1wSOxAzNzEzW}
```

### Notes:

- The `$` at the end of the prompt signifies that hacker is not an administrative user.
- commands in Linux are case sensitive: hello is different from HELLO.

# Challenge 2: Intro to Arguments

Let's try something more complicated: a command with _arguments_, which is what we call additional data passed to the command.
When you type a line of text and hit enter, the shell actually parses your input into a command and its _arguments_.
The first word is the command, and the subsequent words are arguments.
Observe:

```sh
hacker@dojo:~$ echo Hello
Hello
hacker@dojo:~$
```

In this case, the command was `echo`, and the argument was `Hello`.
`echo` is a simple command that "echoes" all of its arguments back out onto the terminal, like you see in the session above.

Let's look at `echo` with multiple arguments:

```sh
hacker@dojo:~$ echo Hello Hackers!
Hello Hackers!
hacker@dojo:~$
```

In this case, the command was `echo`, and `Hello` and `Hackers!` were the two arguments to `echo`.
Simple!

In this challenge, to get the flag, you must run the `hello` command (NOT the `echo` command) with a single argument of `hackers`.
Try it now!

## Solution:

After the terminal comes up, the user needs to invoke `hello` command with argument `hackers`.

#### Commands run: 

```sh
$ hello hackers
```

## Flag: 

```
pwn.college{8B1_F8_2xjSXrgbHj8vRpvIdNZV.QX4YjM1wSOxAzNzEzW}
```

### Notes:

- When you type a line of text and hit enter, the shell actually parses your input into a command and its arguments. The first word is the command, and the subsequent words are arguments.
- `echo` is a simple command that "echoes" all of its arguments back out onto the terminal.

# Challenge 3: Command History

You're going to type a lot of commands, and typing everything from scratch can be annoying.
Luckily, the shell saves a _history_ of every command you invoke.

You can scroll through those saved commands with the up/down arrow keys, and we'll practice that in this challenge.
This challenge will inject the flag into your history.
Bring up a terminal, hit the up arrow, and grab it!
In other challenges, the history will contain the log of the commands you've run, so if you need to run a similar command again, you can use the arrow keys to scroll through and find it!


## Solution:

Here the flag is already in our command history (immediate previous command).

#### Commands run:

press the `up arrow` to scroll to last command

## Flag: 

```
pwn.college{I2z_WjFyEaqyxrjWvgBalpr-XBT.0lNzEzNxwSOxAzNzEzW}
```

### Notes:

- We can scroll through the commands we have run using the arrow keys.
