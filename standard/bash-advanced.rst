.. _bash-advanced:

*************
Advanced Bash
*************

.. contents::
   :depth: 3

.. note:: The content of this tutorial was adapted from Chris Paciorek's
   `Statistics 243 lecture notes on Bash
   <https://github.com/berkeley-stat243/stat243-fall-2014/blob/master/units/unit2-bash.pdf>`_.


.. note::
   This material assumes that you have already worked through
   the "Basics of UNIX" tutorial and screencast here:
   http://statistics.berkeley.edu/computing/training/tutorials

The Interactive Shell
=====================

In order to be of interest to the user, a computer must have a *human interface
component*. A CLI is a text based interface.  The user is given a *prompt* to
indicate the computers reeadiness to accept *input*. The user enters or types a
*command* on the line (or lines) following the prompt. The computer,
consequently, executes or interprets the command and prompts the user when its
finished.

The program which prompts the user and interprets the user's commands is called
a *shell*.  When you are working in a terminal window (i.e., a window with the
command line interface), you’re interacting with a shell.

There are multiple shells (*sh*, *bash*, *csh*, *tcsh*, *zsh*, *fish*).  Since
We'll assume usage of *bash*, as this is the default for Mac OS X, the BCE VM,
the SCF machines and most Linux distributions.  However, the basic ideas are
applicable to any of UNIX's shells.

As you will see the shell is an amazingly powerful programming environment.
From it you can interactively control almost any aspect of the OS and more
importantly you can automate it. As you will see, **bash** has a very extensive
set of capabalities intended to make both interactive as well as automated
control simple, effective, and customizable.

.. note::
   It can be difficult to distinguish what is shell-specific and
   what is just part of UNIX. Some of the material here is not
   bash-specific but general to UNIX.

   Reference: Newham and Rosenblatt, Learning the bash Shell, 2nd ed.

Logging In
----------

**Useful Commands**

* :ref:`command-su` -- run a shell with substitute user and group IDs
* :ref:`command-sudo` -- execute a command as another user

We assume that you already are able to access a terminal from the BCE VM.
However, it is occassionally useful to operate as a different user.  For
instance, you may need to change file permissions or install software.
As you work through this tutorial, we will see examples of this.



Variables
---------

**Useful Commands**

* :ref:`command-echo` -- display a line of text
* :ref:`command-which` -- shows the full path of (shell) commands.
* :ref:`command-man` -- format and display the on-line manual pages
* ``printenv`` -- print all or part of environment

**Standard Variables**

* SHELL, HOME, PS1, PATH

Much of how bash behaves can be customized through the use of variables,
which consists of names that have values assigned to them.  To access
the value currently assigned to a variable, you can prepend the name
with the dollar sign ($).  To print the value you can use the ``echo``
command.

#. | What is my default shell?
   | ``$ echo $SHELL``

#. | To change to bash on a one-time basis:
   | ``$ bash``

#. | To make it your default:
   | ``$ chsh /bin/bash``
   | */bin/bash* should be whatever the path to the bash shell is, which
     you can figure out using ``which bash``

To see how this works, let's work with the 

**Example 2-1. PS1: Prompt String 1**

::

    [user1@local1 src]$ echo $PS1
    [\u@\h \W]\$
      

**Example 2-2. Changing PS1**

::

    [user1@local1 src]$ PS1=$
    $ bash
    [user1@local1 src]$ export PS1=$
    $ bash
    $
      
Shell commands can be saved in a file (with extension *.sh*) and this
file can be executed as if it were a program. To run a shell script
called *file.sh*, you would type ``./file.sh``. Note that if you just
typed\ `` file.sh``, the operating system will generally have trouble
finding the script and recognizing that it is executable. To be sure
that the operating system knows what shell to use to interpret the
script, the first line of the script should be ``#!/bin/bash`` (in the
case that you’re using the bash shell). Also, *file.sh* would need to be
executable (i.e., to have the ’x’ flag set).


**Example 2-3. PATH**

::

    $ echo $PATH
    /bin:/usr/bin:/usr/X11R6/bin:/usr/local/bin
      

**Example 2-4. Finding **echo** with **which****

::

    $ which echo
    /bin/echo
      
We can define shell variables that will help us when writing shell
scripts. Here’s an example of defining a variable:

| ``> myDir=~/stat243-fall-2014/units``
| The shell may not like it if you leave any spaces around the = sign.
  To see the value of a variable we need to precede it by *$*:

``> echo $myDir``

``> cd $myDir``

You can also enclose the variable name in curly brackets, which comes in
handy when we’re embedding a variable within a line of code to make sure
the shell knows where the variable name ends:

``> echo ${myDir}``

``> touch ${myDir}/tmp.txt``

There are also special shell variables called environment variables that
help to control the shell’s behavior. These are generally named in all
caps. Type ``env`` to see them. You can create your own environment
variable as follows:

| ``> export myDir=~/stat243-fall-2014/units``
| The *export* command ensures that other shells created by the current
  shell (for example, to run a program) will inherit the variable.
  Without the export command, any shell variables that are set will only
  be modified within the current shell. More generally, if one wants a
  variable to always be accessible, one would include the definition of
  the variable with an *export* command in your *.bashrc* file.

Here’s an example of an environment variable that controls what your
prompt looks like. We can modify it so that it puts the username,
hostname, and pwd in your prompt. This is handy so you know what machine
you’re on and where in the filesystem you are. [Note that on the VM, PS1
is already set in a very similar manner.]

``> echo $PS1``

::
  > export PS1=\u@\h:\w>

For me, this is one of the most important things to put in my
*.bashrc* file. The **\\** syntax tells bash what to put in the prompt
string: *u* for username, *h* for hostname, and *w* for working
directory.
 

Commands
--------

**Useful Commands**

* :ref:`command-ls` -- list directory contents

While each command has its own syntax, there are some rules usually
followed. Generally, a command line consists of 4 things:

#. command

#. command options

#. arguments

#. line acceptance


**Example 2-6. General Command Syntax**

::

    $ ls --all -l
    total 44
    drwxr-xr-x    2 user1   group1          4096 Feb 26 19:06 .
    drwx------   63 user1   group1         12288 Feb 26 19:04 ..
    -rw-r--r--    1 user1   group1         28251 Feb 26 19:01 manual.xml
    
    $ ls -a -l
    total 44
    drwxr-xr-x    2 user1   group1          4096 Feb 26 19:06 .
    drwx------   63 user1   group1         12288 Feb 26 19:04 ..
    -rw-r--r--    1 user1   group1         28251 Feb 26 19:01 manual.xml
    
    $ ls -al
    total 44
    drwxr-xr-x    2 user1   group1          4096 Feb 26 19:06 .
    drwx------   63 user1   group1         12288 Feb 26 19:04 ..
    -rw-r--r--    1 user1   group1         28251 Feb 26 19:01 manual.xml
    
    $ ls -al manual.xml
    -rw-r--r--    1 user1   group1         28251 Feb 26 19:01 manual.xml
        

Tab completion
~~~~~~~~~~~~~~
      
When working in the shell, it is often unnecessary to type out an entire
command or file name, because of a feature known as tab completion. When
you are entering a command or filename in the shell, you can, at any
time, hit the tab key, and the shell will try to figure out how to
complete the name of the command or filename you are typing. If there is
only one command in the search path and you’re using tab completion with
the first token of a line, then the shell will display its value and the
cursor will be one space past the completed name. If there are multiple
commands that match the partial name, the shell will display as much as
it can. In this case, hitting tab twice will display a list of choices,
and redisplay the partial command line for further editing. Similar
behavior with regard to filenames occurs when tab completion is used on
anything other than the first token of a command.

.. note::
  Note that R does tab completion for objects (including functions) and
  filenames.


Command History and Editing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Useful Commands**  

* :ref:`command-history` -- lists the history of entered commands

**Example 2-7. Examing your command history with **history****

By using the up and down arrows, you can scroll through commands that
you have entered previously. So if you want to rerun the same command,
or fix a typo in a command you entered, just scroll up to it and hit
enter to run it or edit the line and then hit enter.


::

   $ history
     1    echo $PS1
     2    PS1=$
     3    bash
     4    export PS1=$
     5    bash
     6    echo $PATH
     7    which echo
     8    ls --all -l
     9    ls -a -l
     10   ls -al
     11   ls -al manual.xml
        
      

**Example 2-8. Where is the **history** information kept?**

::

    $ echo $HISTFILE
    /group1/user1/.bash_history
    $ echo $HISTSIZE
    1000
      
You can also rerun previous commands as follows:

``> !-n # runs the ``\ ``n``\ ``th previous command``

``> !gi # runs the last command that started with ’gi’``



**Table 2-1. Command History Expansion**

====================   ==========================================================
Designator             Description
====================   ==========================================================
``!!``                 Last command
``!n``                 Command numbered *n* in the history
``!-n``                Command *n* previous
``!string``            Last command starting with *string*
``!?string``           Last command containing *string*
``^string1^string2``   Execute the previous command with *string2*
                       substituted for *string1*
====================   ==========================================================

If you’re not sure what command you’re going to recall, you can append
``:p`` at the end of the text you type to do the recall, and the result
will be printed, but not executed. For example:

| ``> !gi:p``
| You can then use the up arrow key to bring back that statement for
  editing or execution.

You can also search for commands by doing ``C-r`` and typing a string of
characters to search for in the search history. You can hit return to
submit, ``C-c`` to get out, or ``ESC`` to put the result on the regular
command line for editing.

Command Completion and Substitution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 2-9. Command Substitution**

::

        $ ls -l echo
        ls: echo: No such file or directory
        $ ls -l $(which echo)
        -rwxr-xr-x    1 root     root        11704 Mar  7  2002 /bin/echo
      

Shortcuts
---------

**Useful Commands**  

* :ref:`command-clear` -- clear the terminal screen

Aliases -- command shortcuts

Aliases allow you to use an abbreviation for a command, to create new
functionality or to insure that certain options are always used when you
call an existing command. For example, I’m lazy and would rather type
``q`` instead of ``exit`` to terminate a shell window. You could create
the alias as follow

| ``> alias q=exit``
| As another example, suppose you find the *-F* option of *ls* (which
  displays ***/*** after directories, ***\**** after executable files
  and ***@*** after links) to be very useful. The command

::
  > alias ls=ls -F

will insure that the *-F* option will be used whenever you use *ls*.
If you need to use the unaliased version of something for which you’ve
created an alias, precede the name with a backslash (***\\***). For
example, to use the normal version of *ls* after you’ve created the
alias described above, just type

``> \ls``

The real power of aliases is only achieved when they are automatically
set up whenever you log in to the computer or open a new shell window.
To achieve that goal with aliases (or any other bash shell commands),
simply insert the commands in the file *.bashrc* in your home directory.
See the *example.bashrc* file in the repository for some of what’s in my
*.bashrc* file.


Keyboard shorcuts


Note that you can use emacs-like control sequences (``C-a``, ``C-e``,
``C-k``) to navigate and delete characters, just as you can at the
prompt in the shell usually.

**Table 2-2. Keyboard Shortcuts**

============   ==========================================================
Key Strokes    Descriptions
============   ==========================================================
*Ctrl-a*       begin of line
*Ctrl-e*       End of file
*Ctrl-k*       Delete line from cursor forward
*Ctrl-d*       EOF; exit
*Ctrl-c*       Interrupt current command
*Ctrl-z*       Suspend current command
*Ctrl-l*       Clear screen
============   ==========================================================

Basic File Management
=====================

Files
-----

**Useful Commands**  

* :ref:`command-stat` -- display file or filesystem status
* :ref:`command-file` --  determine file type
* :ref:`command-type` -- For each *name*, indicate how it would be
                         interpreted if used as a command name.
* :ref:`command-ln` -- make links between files
* :ref:`command-chmod` -- change file access permissions

A file typically consist of these attributes:

-  Name.

-  Type.

-  Location.

-  Size.

-  Protection.

-  Time, date, and user identification.


Examples: chmod -c -v -R

**Example 2-10. Examining File Attributes with **ls**, **stat**, and **file****

::

    $ ls -l
    total 32
    drwxr-xr-x    3 user1   group1          4096 Mar  3 09:58 db2html-dir
    -rw-r--r--    1 user1   group1         48958 Mar  3 09:58 manual.xml
    
    $ stat manual.xml
      File: "manual.xml"
      Size: 48958           Blocks: 96         IO Block: 4096   Regular File
    Device: 7h/7d   Inode: 2204387     Links: 1
    Access: (0644/-rw-r--r--)  Uid: (  503/  user1)   Gid: (  551/     group1)
    Access: Mon Mar  3 09:58:44 2003
    Modify: Mon Mar  3 09:58:43 2003
    Change: Mon Mar  3 09:58:43 2003
    
    $ file manual.xml
    manual.xml: exported SGML document text
      

.. tip:: **Be aware of Magic:**
    The *file* command relies on many sources
    of information to determine what a file contains. The easiest part
    to explain is *magic*. Specifically, the *file* command examines
    the content of the file and compares it with information found in
    the */usr/share/magic/* directory.


**Example 2-11. Creating Symbolic Links with **ln****

::

    $ ln -s db2html-dir unix_users_guide
    $ ls -l
    total 32
    drwxr-xr-x    3 user1   group1          4096 Mar  3 09:58 db2html-dir
    -rw-r--r--    1 user1   group1         48958 Mar  3 09:58 manual.xml
    lrwxrwxrwx    1 user1   group1            11 Mar  3 10:06 unix_users_guide -> db2html-dir
        
      

**Example 2-12. Changing File Attributes with **chmod****

::

   $ chmod g+w manual.xml
   $ ls -l manual.xml
   -rw-rw-r--    1 user1   group1         49889 Mar  3 10:09 manual.xml
        
      

Navigation
----------

**Useful Commands**  

* :ref:`command-cd` -- Change the current working directory to
                     *directory*.
* :ref:`command-pwd` -- print name of current/working directory

**Example 2-13. Moving Around the Filesystem with **cd**, ~,and **pwd****

::

    $ cd ~
    $ pwd
    /home/user1
    

Manipulation
------------

**Useful Commands**  

* :ref:`command-cat` -- concatenate files and print on the standard output
* :ref:`command-cp`-- copy files and directories
* :ref:`command-diff`-- find differences between two files
* :ref:`command-head` -- output the first part of files
* :ref:`command-less` -- opposite of more
* :ref:`command-more` --  file perusal filter for crt viewing
* :ref:`command-mv` -- move (rename) files
* :ref:`command-paste` -- merge lines of files
* :ref:`command-rm` -- remove files or directories
* :ref:`command-rmdir` -- remove empty directories
* :ref:`command-sort` -- sort lines of text files.
* :ref:`command-split` -- split a file into pieces
* :ref:`command-tac` -- concatenate and print files in reverse
* :ref:`command-tail` -- output the last part of files
* :ref:`command-touch` -- change file timestamps
* :ref:`command-uniq` --  remove duplicate lines from a sorted file

Examples: touch, cp, mv, rename...


::

   $ ls 
   dest.txt
   $ cp dest.txt{,.bak}
   $ ls
   dest.txt  dest.txt.bak

**Example 2-14. Manipulating Files with **touch**, **rm**, and **rmdir****

::

    $ touch index.rst; rm _build; rmdir _build
    rm: `_build' is a directory
    rmdir: `_build': Directory not empty
    
    $ rm -Rf _build
    $ ls -l
    total 56
    -rw-rw-r--    1 user1   group1         50939 Mar  3 10:23 index.rst
    lrwxrwxrwx    1 user1   group1            11 Mar  3 10:06 doc -> db2html-dir
    
  

Filename Globbing
-----------------

The shell will expand certain special characters to match patterns of
file names, before passing those filenames on to a program. Note that
the programs themselves don’t know anything about wildcards; it is the
shell that does the expansion, so that programs don’t see the wildcards.
Table 1 shows some of the special characters that the shell uses for
expansion:

**Table 2-3. File-Naming Wildcards**

============================== ==================================================
Wildcard                       Function
============================== ==================================================
``*``                          Match zero or more characters.
``?``                          Match exactly one character.
``[characters]``               Match any single character from among *characters*
                                 listed between brackets.
``[!characters]``              Match any single character other than *characters*
                                 listed between brackets.
``[a-z]``                      Match any single character from among the range of
                                 characters listed between brackets.
``[!a-z]``                     Match any single character from among the characters
                                 not in the range listed between brackets
``{frag1, frag2, frag3,...}``  Brace expansion: create strings frag1, frag2, and
                                 frag3, etc.
============================== ==================================================

Here are some examples of using wildcards:

-  List all files ending with a digit::

   > ls *[0-9]

-  Make a copy of *filename* as *filename.old*::

   > cp filename{,.old}

-  Remove all files beginning with *a* or *z*::

   > rm [az]*

-  List all the R code files with a variety of suffixes::

   > ls *.{r,q,R}

The *echo* command can be used to verify that a wildcard expansion will
do what you think it will::

  > echo cp filename{,.old} # returns cp filename filename.old

If you want to suppress the special meaning of a wildcard in a shell
command, precede it with a backslash (***\\***). Note that this is a
general rule of thumb in many similar situations when a character has a
special meaning but you just want to treat it as a character.

**Example 2-15. Using brace expansion**

::

   $ echo file{one,two,three}
   fileone filetwo filethree
      

Quoting
-------

**Table 2-4. Quotes**

=================    ====================================
Types of Quoting     Description
=================    ====================================
``' '``              hard quote - no substitution allowed
``" "``              soft quote - allow substitution
``` ```              execute immediately
=================    ====================================


Finally, a note about using single vs. double quotes in shell code. In
general, variables inside double quotes will be evaluated, but variables
not inside double quotes will not be:

| 

| 

| 

::

    ## My name is chris
    ## My name is $name
    ## He said, "My name is chris."

So we’ll generally use double quotes. We can always work with a literal
double quote by escaping it as seen above.



Data Manipulation
=================


Finding Files
-------------

Useful Contents

* :ref:`command-find` --  search for files in a directory hierarchy

**Example 4-1. **find**ing files by name, modification time, and type**

::

    $ find . -name '*.txt'        # find files named *.txt
    $ find . mtime -2             # find files modified less than 2 days ago
    $ find . type l               # find links

Regular Expressions
-------------------

**Table 4-1. Regular Expressions**

Category


**Position anchors**

=========  ====================================================================
Operators  Description
=========  ====================================================================
``^``      Match the beginning of a line.
``$``      Match the end of a line.
=========  ====================================================================

**Character sets**

===============    ====================================================================
Operators          Description
===============    ====================================================================
``[abc]``          Match any single character from from the listed characters
``[a-z]``          Match any single character from the range of characters
``[^abc]``         Match any single character not among listed characters
``[^a-z]``         Match any single character not among listed range of characters
``< word>``        Match *words* bounded by whitespace.
``.``              Match any single character expcept a *newline*
``\``              Turn off (escape) the special meaning of a metacharacter
===============    ====================================================================

**Modifiers**

=============    ====================================================================
Operators        Description
=============    ====================================================================
``*``            Match zero or more of the character that precedes it.
``?``            Match zero or one instace of the preceding *regex*.
``+``            Match one or more instances of the preceding *regex*.
``{n,m}``        Match a range of occurrences of the single character or *regex*
                 that precedes this construct.
``|``            Match the character or expression to the left or right of the
                 vertical bar.
=============    ====================================================================

.. tip:: **Globs vs. Regex:** 
    Be sure you understand the difference between filename globbing (see
    `the Section called *Filename Globbing* in Chapter 2 <basic-file-management.html#FILENAMEGLOBS>`_)
    and regular expressions.


**ed** and **grep**
-------------------

Useful Contents

* :ref:`command-grep` -- print lines matching a pattern
* :ref:`command-tr` -- translate or delete characters

**Example 4-2. Translating lowercase to UPPERCASE with **tr****

::

    $ echo 'user1'  | tr 'a-z' 'A-Z'
    USER1
        
      

**sed** and **awk**
-------------------

**sed** (stream editor) derives from **ed**.

**Example 4-3. Printing lines of text with **sed****

::

    $ sed -n '1,9p' file.txt       # prints out lines 1-9 of file.txt 
    $ sed -n '/^#/p' file.txt       # prints out lines starting with # of file.txt 
      

**Example 4-4. Deleting lines of text with **sed****

::

    $ sed -e '1,9d' file.txt       # deletes lines 1-9 of file.txt 
    $ sed -e '/^;/d' -e '/^$/d' file.txt       # deletes lines  
      

**Example 4-5. Text substitution with **sed****

::

    $ sed 's/old_pattern/new_pattern/' file.txt > new_file.txt       # replaces only 1st instance in a line 
    $ sed 's/old_pattern/new_pattern/g' file.txt > new_file.txt
      

**Example 4-6. Killing **mozilla** with **awk****

::

    $ ps
          PID TTY          TIME CMD
    17043 pts/2    00:00:00 bash
    17073 pts/2    00:00:09 emacs
    17133 pts/2    00:00:02 mozilla-bin
    17140 pts/2    00:00:00 mozilla-bin 
    17141 pts/2    00:00:00 mozilla-bin
    17142 pts/2    00:00:00 mozilla-bin
    17144 pts/2    00:00:00 mozilla-bin
    17146 pts/2    00:00:00 ps
    
    $ ps | grep mozilla
        17133 pts/2    00:00:02 mozilla-bin
    17140 pts/2    00:00:00 mozilla-bin 
    17141 pts/2    00:00:00 mozilla-bin
    17142 pts/2    00:00:00 mozilla-bin
    17144 pts/2    00:00:00 mozilla-bin
    
    $ ps | grep mozilla | awk '{ print $2 }'
        17133
    17140 
    17141
    17142
    17144
    
    $ ps | grep mozilla | awk '{ print $2 }' | xargs kill -9
    [2]+  Killed                  mozilla
        
      

**perl**
--------

**Example 4-7. Text substitution with **perl****

::

    $ perl -pi -e 's/old_pattern/new_pattern/g' file.txt
    $ perl -pi -e 's/old_pattern/new_pattern/g' $(find . -name \*.html)

The i option tells **perl** to do the global substitution in place.
You can also substitute the **/** with another character. For
example:

::

    $ perl -pi -e 's:old_pattern:new_pattern:g' file.txt
      

**Example 4-8. Summing columns with **perl****

::

    $ perl -lane 'print $F[0] + $F[1]' file.txt       # sums column 1 and 2 of file.txt 
      


Streams, Pipes, and Redirects
=============================

UNIX programs that involve input and/or output often operate by reading
input from a stream known as standard input (*stdin*), and writing their
results to a stream known as standard output (*stdout*). In addition, a
third stream known as standard error (*stderr*) receives error messages,
and other information that’s not part of the program’s results. In the
usual interactive session, standard output and standard error default to
your screen, and standard input defaults to your keyboard. You can
change the place from which programs read and write through redirection.
The shell provides this service, not the individual programs, so
redirection will work for all programs. Table 3 shows some examples of
redirection.


Default File Descriptors
------------------------

**Table 3-1. File Descriptors**

============  ============  ===============
Name          I/O           File Descriptor
============  ============  ===============
stdin         input         0
stdout        output        1
stderr        error output  2
user-defined  input/output  3-19
============  ============  ===============

IO Redirection
--------------

Note that *cmd* may include options and arguments as seen in the
previous section.

Operations where output from one command is used as input to another
command (via the \| operator) are known as pipes; they are made
especially useful by the convention that many UNIX commands will accept
their input through the standard input stream when no file name is
provided to them.

Here’s an example of finding out how many unique entries there are in
the 2rd column of a data file whose fields are separated by commas:

``> cut -d’,’ -f2 cpds.csv | sort | uniq | wc``

``> cut -d’,’ -f2 cpds.csv | sort | uniq > countries.txt``

To see if there are any “S” values in certain fields (fixed width) of a
set of files (note I did this on 22,000 files (5 Gb or so) in about 5
minutes on my desktop; it would have taken much more time to read the
data into R):

| ``> cut -b29,37,45,53,61,69,77,85,93,101,109,117,125,133,141,149,`` 
| ``157,165,173,181,189,197,205,213,221,229,237,245,253,261,269 USC*.dly | grep S | less``

A closely related, but subtly different, capability is offered by the
use of backticks (\`). When the shell encounters a command surrounded by
backticks, it runs the command and replaces the backticked expression
with the output from the command; this allows something similar to a
pipe, but is appropriate when a command reads its arguments directly
from the command line instead of through standard input. For example,
suppose we are interested in searching for the text *pdf* in the last 4
R code files (those with suffix *.*\ r or .R) that were modified in the
current directory. We can find the names of the last 4 files ending in
“.R” or “.r” which were modified using

| ``> ls -t *.{R,r} | head -4``
| and we can search for the required pattern using *grep*. Putting these
  together with the backtick operator we can solve the problem using

| ``> grep pdf `ls -t *.{R,r} | head -4```
| Note that piping the output of the *ls* command into *grep* would not
  achieve the desired goal, since *grep* reads its filenames from the
  command line, not standard input.

You can also redirect output as the arguments to another program using
the *xargs* utility. Here’s an example:

``> ls -t *.{R,r} | head -4 | xargs grep pdf``

And you can redirect output into a shell variable (see section 9) using
backticks in a similar manner to that done above:

``> files=ls -t *.{R,r} | head -4 # NOTE - don’t put any spaces around the =``

``> echo $files``

``> grep pdf $files``

**Table 3-2. Common Redirection Operators**

===========================   ===============================================
Redirection Syntax            Function
===========================   ===============================================
``$ cmd > file``              Send *stdout* to *file*            
``$ cmd 1> file``             Same as above
``$ cmd 2> file``             Send *stderr* to *file*
``$ cmd > file 2>&1``         Send both *stdout* and *stderr* to *file*
``$ cmd < file``              Receive *stdin* from *file*
``$ cmd >> file``             Append *stdout* to *file*:
``$ cmd 1>> file``            Same as above
``$ cmd 2>> file``            Append *stderr* to *file*
``$ cmd >> file 2>&1``        Append both *stdout* and *stderr* to *file*
``$ cmd1 | cmd2``             Pipe *stdout* from *cmd1* to *cmd2*
``$ cmd1 2>&1 | cmd2``        Pipe *stdout* and *stderr* from *cmd1* to *cmd2*
``$ cmd1 tee file1 | cmd2``   Pipe *stdout* and *cmd1* to *cmd2* while
                              simultaneously writing it to *file1*
                              using *tee*
===========================   ===============================================

Standard Redirection
~~~~~~~~~~~~~~~~~~~~

Pipes
~~~~~

Useful Contents

* :ref:`command-wc` --  print the number of bytes, words, and lines in
  files

**Example 3-1. A simple pipe to **wc****

::

        $ echo "hey there" | wc -w
              2
      

The **xargs** and **tee** Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Useful Contents

* :ref:`command-xargs` --  build and execute command lines from
  standard input
* :ref:`command-tee` -- read from standard input and write to standard
  output and files



Creating, Monitoring, and Killing Processes
===========================================

Processes
---------

Processes have the following attributes:

-  A lifetime.

-  A PID.

-  A UID.

-  A GID.

-  A parent process.

-  An environment.

-  A current working directory.


Monitoring Processes
--------------------

Useful Contents

* :ref:`command-ps` --  report process status
* :ref:`command-pstree` -- display a tree of processes
* :ref:`command-top` -- display top CPU processes

**Example 3-2. Examining Processes with **ps****

::

        $ ps
          PID TTY          TIME CMD
        29982 pts/1    00:00:00 bash
        30042 pts/1    00:00:00 gvim
        30162 pts/1    00:00:00 ps
        
        $ ps -f
        UID        PID  PPID  C STIME TTY          TIME CMD
        user1   29982 29981  0 17:04 pts/1    00:00:00 /bin/bash
        user1   30042 29982  0 17:05 pts/1    00:00:00 gvim manual.xml
        user1   30161 29982  0 17:11 pts/1    00:00:00 ps -f
        
        $ ps -lf
          F S UID        PID  PPID  C PRI  NI ADDR    SZ WCHAN  STIME TTY          TIME CMD
        000 S user1   29982 29981  0  75   0    -   712 wait4  17:04 pts/1    00:00:00 /bin/bash
        000 S user1   30042 29982  0  75   0    -  2849 schedu 17:05 pts/1    00:00:01 emacs manual.xml
        000 R user1   30238 29982  0  76   0    -   855 -      17:16 pts/1    00:00:00 ps -lf
        
      

**Example 3-3. Examining Processes with **pstree****

::

        $ pstree
        init-+-alarmd
             |-atd
             |-bdflush
             |-crond
             |-cupsd
             |-gkrellm
             |-gpm
             |-7*[kdeinit]
             |-kdeinit-+-kdeinit
             |         |-konsole---bash-+-emacs
             |         |                `-pstree
             |         `-soundwrapper---mozilla-bin---mozilla-bin---4*[mozilla-bin]
             |-kdeinit---cat
             |-kdm-+-X
             |     `-kdm---startkde-+-ksmserver
             |                      `-ssh-agent
             |-sshd
             |-syslogd
             |-xfs
             |-xinetd
             `-ypbind---ypbind
        
      

**Example 3-4. Examining Processes with **top****

::

        $ top
          5:18pm  up 2 days, 13:26,  2 users,  load average: 0.03, 0.03, 0.00
        76 processes: 75 sleeping, 1 running, 0 zombie, 0 stopped
        CPU0 states:  0.4% user,  0.3% system,  0.0% nice, 98.3% idle
        CPU1 states:  0.0% user,  0.4% system,  0.0% nice, 99.1% idle
        Mem:  2068644K av, 1001668K used, 1066976K free,       0K shrd,  218192K buff
        Swap:  401584K av,       0K used,  401584K free                  339532K cached
        
          PID USER     PRI  NI  SIZE  RSS SHARE STAT %CPU %MEM   TIME COMMAND
         1840 root       5 -10  284M  28M  4340 S <   0.9  1.4  10:24 X
        29981 user1    15   0 13504  13M  8120 S     0.7  0.6   0:01 konsole
        30296 user1    15   0  1188 1188   928 R     0.3  0.0   0:00 top
            1 root      15   0   504  504   440 S     0.0  0.0   0:05 init
        
      

Signaling Processes
-------------------

Useful Contents

* :ref:`command-kill` -- terminate a process
* :ref:`command-killall` --  kill processes by name

**Table 3-3. Common Signals**

============= =================================  ====
Signal Number Meaning                            HUP
============= =================================  ====
1             Hangup, reread configuration       INT
2             Interrupt, stop running            KILL
9             Stop immediately                   TERM
15            Terminate nicely                   TSTP
18            Stop executing, ready to continue
============= =================================  ====

.. _tip: **Zombies:**
    Occasionally, a process monitor like **ps** or **top**
    will list a process as a *zombie*. This is a process with has
    gotten stuck while terminating. As you would expect you cannot kill
    a *zombie* as its all ready dead. If an application repeatedly
    becomes a *zombie* when killed, there's a good chance there's an
    underlying bug in the application.


Shell Job Control
-----------------

Useful Contents

* :ref:`command-bg` -- background
* :ref:`command-fg` -- foreground
* :ref:`command-jobs` -- list the active jobs
* :ref:`command-nohup` -- Run a command immune to hangups, with
  output to a non-tty

Starting a job
~~~~~~~~~~~~~~

When you run a command in a shell by simply typing its name, you are
said to be running in the foreground. When a job is running in the
foreground, you can’t type additional commands into that shell session,
but there are two signals that can be sent to the running job through
the keyboard. To interrupt a program running in the foreground, use
``C-c``; to quit a program, use ``C-\``. While modern windowed systems
have lessened the inconvenience of tying up a shell with foreground
processes, there are some situations where running in the foreground is
not adequate.

The primary need for an alternative to foreground processing arises when
you wish to have jobs continue to run after you log off the computer. In
cases like this you can run a program in the background by simply
terminating the command with an ampersand (*&*). However, before putting
a job in the background, you should consider how you will access its
results, since *stdout* is not preserved when you log off from the
computer. Thus, redirection (including redirection of *stderr*) is
essential when running jobs in the background. As a simple example,
suppose that you wish to run an R script, and you don’t want it to
terminate when you log off. (Note that this can also be done using
``R CMD BATCH``, so this is primarily an illustration.)

| ``> R --no-save < code.R > code.Rout 2>&1 &``
| If you forget to put a job in the background when you first execute
  it, you can do it while it’s running in the foreground in two steps.
  First, suspend the job using the ``C-z`` signal. After receiving the
  signal, the program will interrupt execution, but will still have
  access to all files and other resources. Next, issue the ``bg``
  command, which will put the stopped job in the background.

Listing and killing jobs
~~~~~~~~~~~~~~~~~~~~~~~~

Since only foreground jobs will accept signals through the keyboard, if
you want to terminate a background job you must first determine the
unique process id (PID) for the process you wish to terminate through
the use of the *ps* command. For example, to see all the jobs running on
a particular computer, you could use a command like::

  > ps -aux

Among the output after the header (shown here) might appear a line
that looks like this::

  USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
  paciorek 11998 97.0 39.1 1416644 1204824 pts/16 R+ Jul27 1330:01 /usr/lib64/R/bin/exec/R

In this example, the *ps* output tells us that this R job has a PID of
*11998*, that it has been running for 1330 minutes (!), is using 97%
of CPU and 39% of memory, and that it started on July 27. You could
then issue the command::

  > kill 11998

or, if that doesn’t work::

  > kill -9 11998

to terminate the job. Another useful command in this regard is
*killall*, which accepts a program name instead of a process id, and
will kill all instances of the named program::

  > killall R

Of course, it will only kill the jobs that belong to you, so it will
not affect the jobs of other users. Note that the *ps* and *kill*
commands only apply to the particular computer on which they are
executed, not to the entire computer network. Thus, if you start a job
on one machine, you must log back into that same machine in order to
manage your job.

Monitoring jobs and memory use
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *top* command also allows you to monitor the jobs on the system and
in real-time. In particular, it’s useful for seeing how much of the CPU
and how much memory is being used, as well as figuring out a PID as an
alternative to *ps*. You can also renice jobs (see below) and kill jobs
from within top: just type *r* or *k*, respectively, and proceed
from there.

One of the main things to watch out for is a job that is using close to
100% of memory and much less than 100% of CPU. What is generally
happening is that your program has run out of memory and is using
virtual memory on disk, spending most of its time writing to/from disk,
sometimes called *paging* or *swapping*. If this happens, it can be a
very long time, if ever, before your job finishes.

Nicing a job
~~~~~~~~~~~~

The most important thing to remember when starting a job on a machine
that is not your personal machine is how to be a good citizen. This
often involves ’nicing’ your jobs. This is required on the SCF machines,
but the compute servers should automatically nice your jobs. Nicing a
job puts it at a lower priority so that a user working at the keyboard
has higher priority in using the CPU. Here’s how to do it, giving the
job a low priority of 19, as required by SCF::

  > nice -19 R CMD BATCH --no-save code.R code.Rout &

If you forget and just submit the job without nicing, you can reduce
the priority by doing::

  > renice +19 11998

where *11998* is the PID of your job.

On many larger UNIX cluster computers, all jobs are submitted via a job
scheduler and enter a queue, which handles the issue of prioritization
and jobs conflicting. Syntax varies by system and queueing software, but
may look something like this for submitting an R job:

``> bsub -q long R CMD BATCH --no-save code.R code.Rout # just an example; this will not work on the SCF network``


bg,fg,jobs,Ctrl-C,Ctrl-Z

**screen**

Shell programming
=================

Shell commands can be saved in a file (with extension *.sh*) and this
file can be executed as if it were a program. To run a shell script
called *file.sh*, you would type ``./file.sh``. Note that if you just
typed\ `` file.sh``, the operating system will generally have trouble
finding the script and recognizing that it is executable. To be sure
that the operating system knows what shell to use to interpret the
script, the first line of the script should be ``#!/bin/bash`` (in the
case that you’re using the bash shell). Also, *file.sh* would need to be
executable (i.e., to have the ’x’ flag set).

Functions
---------

You can define your own utilities by creating a shell function. This
allows you to automate things that are more complicated than you can do
with an alias. One nice thing about shell functions is that the shell
automatically takes care of function arguments for you. It places the
arguments given by the user into local variables in the function called
(in order): *$1 $2 $3* etc. It also fills *$#* with the number of
arguments given by the user. Here’s an example of using arguments in a
function that saves me some typing when I want to copy a file to the SCF
filesystem::

  function putscf() {
     scp $1 paciorek@radagast.berkeley.edu:~/$2 ``
  }

To use this function, I just do the following to copy *unit1.pdf* from
the current directory on whatever non-SCF machine I’m on to the
directory *~/teaching/243* on SCF::

  > putscf unit1-unix.pdf Desktop/.

Of course you’d want to put such functions in your *.bashrc* file.

If/then/else
------------

We can use if-then-else type syntax to control the flow of a shell
script. For an example, see *niceR()* in the demo code file *niceR.sh*
for this unit.

For more details, look in Newham&Rosenblatt or search online.

For loops
---------

*for* loops in shell scripting are primarily designed for iterating
through a set of files or directories. Here’s an example::

  for file in $(ls *.txt)  
  do
     mv $file ${file/.txt/.R}
     # this syntax replaces .txt with .R in $file``
  done

You could also have done that with ``for file in `ls *.txt```

Another use of *for* loops is automating file downloads: see the demo
code file. And, in my experience, *for* loops are very useful for
starting a series of jobs: see the demo code files in the repository:
*forloopDownload.sh* and *forloopJobs.sh*.

How much shell scripting should I learn?
----------------------------------------

You can do a fair amount of what you need from within R using the
*system()* function. This will enable you to avoid dealing with a lot of
shell programming syntax (but you’ll still need to know how to use UNIX
utilities, wildcards, and pipes to be effective). Example: a fellow
student when I was in grad school programmed a tool in R to extract
concert information from the web for bands appearing in her iTunes
library. Not the most elegant solution, but it got the job done.

For more extensive shell programming, it’s probably worth learning
Python and doing it there rather than using a shell script. In
particular iPython makes it very easy to interact with the operating
system.

Documentation tools
===================

**markdown**, **restructured text**, latex

**pandoc**

Please see the "Introduction to LaTeX" tutorial and screencast
here: http://statistics.berkeley.edu/computing/training/tutorials

