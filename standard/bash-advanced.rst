.. _bash-advanced:

*************
Advanced Bash
*************

.. contents::
   :depth: 3

.. note:: Some of the material in this tutorial was adapted from Chris Paciorek's
   `2014 Statistics 243 lecture notes on Bash
   <https://github.com/berkeley-stat243/stat243-fall-2014/blob/master/units/unit2-bash.pdf>`_
   and his `2014 Statistics 243 lecture notes on using R
   <https://github.com/berkeley-stat243/stat243-fall-2014/blob/master/units/unit4-usingR.pdf>`_.

   Before reading this, you will want to be familiar with the material in
   the "Basics of UNIX" tutorial and screencast here:
   http://statistics.berkeley.edu/computing/training/tutorials

The Interactive Shell
=====================

The shell is an interactive computer programming environment. More
specifically, it is a read-evaluate-print loop (REPL) environment.  R and
Python also provide REPL environments. A REPL reads a single expression or
input, parses and evaluates it, prints the results, and then loops.

.. tip::
   I will use a ``$`` prompt for bash, a ``>`` prompt for R, and a ``>>>``
   for Python, and a ``In [#]:`` prompt for IPython. By convention, a
   regular user's prompt in bash is ``$``, while the root (or administrative)
   user's prompt is ``#``.  However, it is common practice to never log
   on as the root user.  If you need to run a command with root priveleges,
   you should use the ``sudo`` command (see the section on *Logging In*
   below for more details).

When you are working in a terminal window (i.e., a window with the command line
interface), you’re interacting with a shell.  There are multiple shells (*sh*,
*bash*, *csh*, *tcsh*, *zsh*, *fish*).  I'll assume you are using *bash*, as
this is the default for Mac OS X, the BCE VM, the SCF machines and most Linux
distributions.  However, the basic ideas are applicable to any Unix shell.

The shell is an amazingly powerful programming environment.
From it you can interactively monitor and control almost any aspect of the OS
and more importantly you can automate it. As you will see, **bash** has a very
extensive set of capabalities intended to make both interactive as well as
automated control simple, effective, and customizable.

.. note::
   It can be difficult to distinguish what is shell-specific and
   what is just part of UNIX. Some of the material here is not
   bash-specific but general to UNIX.

   Reference: Newham and Rosenblatt, Learning the bash Shell, 2nd ed.

Logging In
----------

* :ref:`su` -- run a shell with substitute user and group IDs
* :ref:`sudo` -- execute a command as another user

You should already be able to access a terminal from the BCE VM.
However, it is occassionally useful to operate as a different user.  For
instance, you may need to change file permissions or install software.
As you work through this tutorial, we will see examples of this.

.. tip::
   Most bash commands have electronic manual pages, which are accessible
   directly from the commandline.  You will be more efficient and effective
   if you become accustomed to using these ``man`` pages.  To view the ``man``
   page for the command ``su``, for instance, you would type::

     $ man su

   Compare this output to the this :ref:`su` page.

Variables
---------

* :ref:`echo` -- display a line of text
* :ref:`which` -- shows the full path of (shell) commands.
* :ref:`man` -- format and display the on-line manual pages
* :ref:`printenv` -- print all or part of environment

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

In the last example, ``/bin/bash`` should be whatever the path to the bash shell
is, which you can figure out using ``which bash``.

To declare a variable, just assign a value to its reference.  
For example, if you want to make a new variable with the name
``counter`` with the value ``1``::

  $ counter=1

Since bash uses spaces to parse the expression you give it as input,
it is important to note the lack of spaces around the equal sign.
Try typing the command with and without spaces and note what happens.

You can also enclose the variable name in curly brackets, which comes in
handy when you're embedding a variable within a line of code to make sure
the shell knows where the variable name ends::

  $ base=/home/jarrod/
  $ echo $basesrc
  $ echo ${base}src

Make sure you understand the difference in behavior in the last two lines.

There are also special shell variables called environment variables that help
to control the shell's behavior. These are generally named in all caps. Type
``printenv`` to see them. You can create your own environment variable as
follows::

  $ export base=/home/jarrod/


The ``export`` command ensures that other shells created by the current shell
(for example, to run a program) will inherit the variable.  Without the export
command, any shell variables that are set will only be modified within the
current shell. More generally, if you want a variable to always be accessible,
you should include the definition of the variable with an ``export`` command in
your ``.bashrc`` file.

You can control the appearance of the bash prompt using the ``PS1``
variable::

  $ echo $PS1

To modify it so that it puts the username, hostname, and current working
directory in the prompt::

  $ export PS1='[\u@\h \W]\$ '
  [user1@local1 ~]$ 


**Maybe something about PATH**

Commands
--------

* :ref:`ls` -- list directory contents

While each command has its own syntax, there are some rules usually
followed. Generally, a command line consists of 4 things:

#. command
#. command options
#. arguments
#. line acceptance

Exercise
~~~~~~~~
 
Consider the following examples using the ``ls`` command::

    $ ls --all -l
    $ ls -a -l
    $ ls -al

Use ``man ls`` to see what the command options do.  Is there any difference
in what the three versions of the command invocation above return as
the result?  What happens if you add a filename to the end of the command?

Tab completion
~~~~~~~~~~~~~~
      
When working in the shell, it is often unnecessary to type out an entire
command or file name, because of a feature known as tab completion. When you
are entering a command or filename in the shell, you can, at any time, hit the
tab key, and the shell will try to figure out how to complete the name of the
command or filename you are typing. If there is only one command in the search
path and you’re using tab completion with the first token of a line, then the
shell will display its value and the cursor will be one space past the
completed name. If there are multiple commands that match the partial name, the
shell will display as much as it can. In this case, hitting tab twice will
display a list of choices, and redisplay the partial command line for further
editing. Similar behavior with regard to filenames occurs when tab completion
is used on anything other than the first token of a command.

.. note::
  Note that R does tab completion for objects (including functions) and
  filenames.


Command History and Editing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :ref:`history` -- lists the history of entered commands

By using the up and down arrows, you can scroll through commands that
you have entered previously. So if you want to rerun the same command,
or fix a typo in a command you entered, just scroll up to it and hit
enter to run it or edit the line and then hit enter.

To list the history of the commands you entered, use the ``history`` command::

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
        

The behavior of the **history** command is controlled by a couple of shell
variables::

    $ echo $HISTFILE
    $ echo $HISTSIZE
      
You can also rerun previous commands as follows::

  $ !-n # runs the ``\ ``n``\ ``th previous command
  $ !gi # runs the last command that started with 'gi'

The first example runs the nth previous command and the second one runs the
last command that started with 'gi'.

**Table. Command History Expansion**

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

If you're not sure what command you're going to recall, you can append
``:p`` at the end of the text you type to do the recall, and the result
will be printed, but not executed. For example::

  $ !gi:p

You can then use the up arrow key to bring back that statement for editing or
execution.

You can also search for commands by doing ``Ctrl-r`` and typing a string of
characters to search for in the search history. You can hit return to submit,
``Ctrl-c`` to get out, or ``ESC`` to put the result on the regular command line
for editing.

Command Substitution
~~~~~~~~~~~~~~~~~~~~

You may occassionally need to substitute the results of a command for use by
another command.  For example, if you wanted to use the directory listing
returned by ``ls`` as the argument to another command, you would type
``$(ls)`` in the location you want the result of ``ls`` to appear.

Exercise
~~~~~~~~

Try the following commands::
 
  $ ls -l echo
  $ which echo
  $ ls -l which echo
  $ ls -l $(which echo)

Make sure you understand why each command behaves as it does.

Shortcuts
---------

* :ref:`alias` -- set aliases
* :ref:`clear` -- clear the terminal screen

Aliases -- command shortcuts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Aliases allow you to use an abbreviation for a command, to create new
functionality or to insure that certain options are always used when you
call an existing command. For example, I’m lazy and would rather type
``q`` instead of ``exit`` to terminate a shell window. You could create
the alias as follow::

  $ alias q=exit

As another example, suppose you find the ``-F`` option of ``ls`` (which
displays ``/`` after directories, ``\`` after executable files
and ``@`` after links) to be very useful. The command ::

  $ alias ls=ls -F

will insure that the ``-F`` option will be used whenever you use ``ls``.
If you need to use the unaliased version of something for which you’ve
created an alias, precede the name with a backslash (``\``). For
example, to use the normal version of ``ls`` after you’ve created the
alias described above::

  $ \ls

The real power of aliases is only achieved when they are automatically
set up whenever you log in to the computer or open a new shell window.
To achieve that goal with aliases (or any other bash shell commands),
simply insert the commands in the file ``.bashrc`` in your home directory.

**See the ``example.bashrc`` file in the repository for some of what’s in my
``.bashrc`` file.**

Keyboard shorcuts
~~~~~~~~~~~~~~~~~

Note that you can use emacs-like control sequences (``Ctrl-a``, ``Ctrl-e``,
``Ctrl-k``) to navigate and delete characters, just as you can at the prompt in
the shell usually.

**Table. Keyboard Shortcuts**

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

In Unix, almost "Everything is a file." This means that a very wide variety
of input and output resources (e.g., documents, directories, keyboards,
harddrives, network devices) are streams of bytes available through the
filesystem interface. This means that the basic file management tools
are extremely powerful in Unix.  Not only can you use these tools to work
with files, but you can often use them to monitor and control many aspects
of your computer.

Files
-----

* :ref:`stat` -- display file or filesystem status
* :ref:`file` --  determine file type
* :ref:`type` -- For each *name*, indicate how it would be
                         interpreted if used as a command name.
* :ref:`ln` -- make links between files
* :ref:`chmod` -- change file access permissions

A file typically consist of these attributes:

-  Name.
-  Type.
-  Location.
-  Size.
-  Protection.
-  Time, date, and user identification.

Listing file attributes with ``ls``::

    $ ls -l
   
Getting more information with ``stat``::
 
    $ stat manual.xml

Finding out what type of file you have::
    
    $ file manual.xml

.. tip:: 
    The ``file`` command relies on many sources
    of information to determine what a file contains. The easiest part
    to explain is *magic*. Specifically, the ``file`` command examines
    the content of the file and compares it with information found in
    the ``/usr/share/magic/`` directory.


Creating symbolic links with ``ln``::

    $ ln -s db2html-dir unix_users_guide

Changing file attributes with ``chmod``::

   $ chmod g+w manual.xml
        
      

Navigation
----------

* :ref:`cd` -- Change the current working directory to
                     *directory*.
* :ref:`pwd` -- print name of current/working directory

Efficient navigation of the filesystem from the shell is an essential aspect of
mastering Unix.  Use ``pwd`` to list your current working directory.  If you
just enter ``cd`` at a prompt, your current working directory will change to
your home directory.  You can also refer to your home directory using the tilde
``~``.  For example, if you wanted to change your current directory to the
subdirectory ``src`` in your home directory from any other current directory,
you could type::

  $ cd ~/src

Also if you want to return to the previous directory, you could type::

  $ cd -

You can use the ``pushd``, ``popd``, and ``dirs`` commands if you would
like to keep a stack of previous working directories rather than just
the last one.

Filename Globbing
-----------------

The shell will expand certain special characters to match patterns of
filenames, before passing those filenames on to a program. Note that the
programs themselves don’t know anything about wildcards; it is the shell that
does the expansion, so that programs don’t see the wildcards.  Table 1 shows
some of the special characters that the shell uses for expansion:

**Table. Filename Wildcards**

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
``{frag1,frag2,frag3,...}``    Brace expansion: create strings frag1, frag2, and
                               frag3, etc.
============================== ==================================================

Here are some examples of using wildcards:

-  List all files ending with a digit::

   $ ls *[0-9]

-  Make a copy of *filename* as *filename.old*::

   $ cp filename{,.old}

-  Remove all files beginning with *a* or *z*::

   $ rm [az]*

-  List all the R code files with a variety of suffixes::

   $ ls *.{r,q,R}

The ``echo`` command can be used to verify that a wildcard expansion will
do what you think it will::

  $ echo cp filename{,.old} # returns cp filename filename.old

If you want to suppress the special meaning of a wildcard in a shell command,
precede it with a backslash (``\``). Note that this is a general rule of thumb
in many similar situations when a character has a special meaning but you just
want to treat it as a character.

Exercise
~~~~~~~~

Figure out how to use the :ref:`mkdir` command and brace expansion
to create the following directory structure in one short command::

  $ tree temp/
  temp/
  ├── proj1
  │   ├── code
  │   └── data
  ├── proj2
  │   ├── code
  │   └── data
  └── proj3
      ├── code
      └── data
  
  9 directories, 0 files 

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

Basic utilities
---------------

Since files are such an essential aspect of Unix and working from the shell is
the primary way to work with Unix, there are a large number of useful commands
and tools to view and manipulate files.  

* :ref:`cat` -- concatenate files and print on the standard output
* :ref:`cp`-- copy files and directories
* :ref:`diff`-- find differences between two files
* :ref:`head` -- output the first part of files
* :ref:`less` -- opposite of more
* :ref:`more` --  file perusal filter for crt viewing
* :ref:`mv` -- move (rename) files
* :ref:`paste` -- merge lines of files
* :ref:`rm` -- remove files or directories
* :ref:`rmdir` -- remove empty directories
* :ref:`sort` -- sort lines of text files.
* :ref:`split` -- split a file into pieces
* :ref:`tac` -- concatenate and print files in reverse
* :ref:`tail` -- output the last part of files
* :ref:`touch` -- change file timestamps
* :ref:`uniq` --  remove duplicate lines from a sorted file

**Exercise**

You've already seen some of the above commands.  Follow the links above and
while you are reading the abbreviated man pages consider how you might use
these commands.

Finding Files
-------------

* :ref:`find` --  search for files in a directory hierarchy

Finding files by name, modification time, and type::

    $ find . -name '*.txt'   # find files named *.txt
    $ find . mtime -2        # find files modified less than 2 days ago
    $ find . type l          # find links

Streams, Pipes, and Redirects
-----------------------------

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
~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~

Note that *cmd* may include options and arguments as seen in the
previous section.

Operations where output from one command is used as input to another command
(via the ``|`` operator) are known as pipes; they are made especially useful by
the convention that many UNIX commands will accept their input through the
standard input stream when no file name is provided to them.

Here’s an example of finding out how many unique entries there are in
the 2rd column of a data file whose fields are separated by commas::

  $ cut -d',' -f2 cpds.csv | sort | uniq | wc
  $ cut -d',' -f2 cpds.csv | sort | uniq > countries.txt

To see if there are any “S” values in certain fields (fixed width) of a
set of files (note I did this on 22,000 files (5 Gb or so) in about 5
minutes on my desktop; it would have taken much more time to read the
data into R):

| ``$ cut -b29,37,45,53,61,69,77,85,93,101,109,117,125,133,141,149,`` 
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

| ``$ ls -t *.{R,r} | head -4``
| and we can search for the required pattern using *grep*. Putting these
  together with the backtick operator we can solve the problem using

| ``$ grep pdf `ls -t *.{R,r} | head -4```
| Note that piping the output of the *ls* command into *grep* would not
  achieve the desired goal, since *grep* reads its filenames from the
  command line, not standard input.

You can also redirect output as the arguments to another program using
the *xargs* utility. Here’s an example:

``$ ls -t *.{R,r} | head -4 | xargs grep pdf``

And you can redirect output into a shell variable (see section 9) using
backticks in a similar manner to that done above:

``$ files=ls -t *.{R,r} | head -4 # NOTE - don’t put any spaces around the =``

``$ echo $files``

``$ grep pdf $files``

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

* :ref:`wc` --  print the number of bytes, words, and lines in
  files

**Example 3-1. A simple pipe to **wc****

::

        $ echo "hey there" | wc -w
              2
      

The **xargs** and **tee** Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :ref:`xargs` --  build and execute command lines from
  standard input
* :ref:`tee` -- read from standard input and write to standard
  output and files

Regular Expressions
===================

Regular expressions (regexp) are a domain-specific language for finding patterns and are
one of the key functionalities in scripting languages such as Perl and Python,
as well as the UNIX utilities ``sed``, ``awk``, and ``grep`` as we will see
below. I'll just cover the use of regular expressions in bash, but once you
know that, it would be easy to use them elsewhere (Python, R, etc.).  At the
level we’ll consider them, the syntax is quite similar.

Overview and core syntax
------------------------

The basic idea of regular expressions is that they allow us to find matches of
strings or patterns in strings, as well as do substitution.  Regular
expressions are good for tasks such as:

-  extracting pieces of text - for example finding all the links in an
   html document;
-  creating variables from information found in text;
-  cleaning and transforming text into a uniform format;
-  mining text by treating documents as data; and
-  scraping the web for data.

Regular expressions are constructed from three things:

#. *Literal characters* are matched only by the characters themselves,
#. *Character classes* are matched by any single member in the class, and
#. *Modifiers* operate on either of the above or combinations of them.

Note that the syntax is very concise, so it’s helpful to break down individual
regular expressions into the component parts to understand them. Since regexp
are their own language, it’s a good idea to build up a regexp in pieces as a
way of avoiding errors just as we would with any computer code. It is also
helpful to search for common regexp online before trying to craft your own.
For instance, if you wanted to use a regexp that matches valid email addresses,
you would need to match anything that complies with the `RFC 822
<http://www.ietf.org/rfc/rfc0822.txt?number=822>`_ grammar. If you look over that
document, you will quickly realize that implementing a correct regular expression
to validate email addresses is extremely complex. So if you are writing a website
that validates email addresses, it is best to look for a bug-vetted implementation
rather than rolling your own. 

The special characters (meta-characters) used for defining regular expressions
are: ``* . ^ $ + ? ( ) [ ] { } | \`` . To use these characters literally as
characters, we have to 'escape' them. In bash, you escape these characters by
placing a  single backslash before the character you want to escape.  In R, we
have to use two backslashes instead of a single backslash because R uses a
single backslash to symbolize certain control characters, such as ``\\n`` for
newline.

Character sets and character classes
------------------------------------

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

If we want to search for any one of a set of characters, we use a
character set, such as ``[13579]`` or ``[abcd]`` or ``[0-9]`` (where the
dash indicates a sequence) or ``[0-9a-z]`` or ``[ \t]``. To indicate any
character not in a set, we place a ^ just inside the first bracket:
``[^abcd]``. The period stands for any character.

There are a bunch of named character classes so that we don’t have write out
common sets of characters. The syntax is ``[:CLASS:]`` where *CLASS* is one of
the following values "alnum", "alpha", "ascii", "blank", "cntrl", "digit",
"graph", "lower", "print", "punct", "space", "upper", "word" or "xdigit".

To learn more about regular expressions, you can type::

  $ man 7 regex

To make a character set with a character class you
need two square brackets, e.g. the digit class: ``[[:digit:]]``. Or we
can make a combined character set such as ``[[:alnum:]_]``. E.g., the
latter would be useful in looking for email addresses. 

::

    ## [1] FALSE  TRUE  TRUE

Here are some more examples showing a wide range of string
functionality:

::

    ## [1] FALSE  TRUE  TRUE

::

    ## [[1]]
    ##      start end
    ## 
    ## [[2]]
    ##      start end
    ## [1,]     9   9
    ## 
    ## [[3]]
    ##      start end
    ## [1,]     5   5
    ## [2,]    12  12

::

    ## [[1]]
    ## character(0)
    ## 
    ## [[2]]
    ## character(0)
    ## 
    ## [[3]]
    ## [1] "Juan "

::

    ## [1] "John"            "Jennifer pierce"
    ## [3] "Juan carlos rey"

**Challenge**: how would we find a spam-like pattern with digits or
non-letters inside a word? E.g., I want to find V1agra or Fancy
repl!c@ted watches.

Location-specific matches
-------------------------

**Position anchors**

=========  ====================================================================
Operators  Description
=========  ====================================================================
``^``      Match the beginning of a line.
``$``      Match the end of a line.
=========  ====================================================================

To find a pattern at the beginning of the string, we use ``^`` (note this was
also used for negation, but in that case occurs only inside square brackets)
and to find it at the end we use ``$``.

::

    ## [1] FALSE FALSE  TRUE

::

    ## [1] FALSE FALSE FALSE

What does this match: ``^[^[:lower:]]$`` ?

Repetitions, Grouping, and References
-------------------------------------

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

Now suppose I wanted to be able to detect phone numbers, email addresses, etc.
I often need to be able to deal with repetitions of character sets.

I can indicate repetitions as indicated in these examples:

-  ``[[:digit:]]*`` – any number of digits (zero or more)
-  ``[[:digit:]]+`` – at least one digit
-  ``[[:digit:]]?`` – zero or one digits
-  ``[[:digit:]]{1,3}`` – at least one and no more than three digits
-  ``[[:digit:]]{2,}`` – two or more digits

An example is that ``\\[.*\\]`` is the pattern of any number of
characters (*.\**) separated by square brackets.

So a search for US/Canadian/Caribbean phone numbers might become:

::

    ## [[1]]
    ## [1] "919-543-3300"
    ## 
    ## [[2]]
    ## character(0)
    ## 
    ## [[3]]
    ## character(0)
    ## 
    ## [[4]]
    ## [1] "919.554.3800"

**Challenge**: How would I extract an email address from an arbitrary
text string?

We often want to be able to look for multi-character patterns and to be able to
refer back to the patterns that are found. Both are accomplished with
parentheses. For example, the phone number detection problem could have been
done a bit more compactly (and more generally, in case the area code is omitted
or a 1 is included) as:

::

    ## [[1]]
    ## [1] "919-543-3300"
    ## 
    ## [[2]]
    ## character(0)
    ## 
    ## [[3]]
    ## character(0)
    ## 
    ## [[4]]
    ## [1] "1.919.554.3800"
    ## 
    ## [[5]]
    ## [1] "337.4355"

Parentheses are also used with a pipe (\|) to indicate any one of a set
of multi-character sequences, such as ``(http|ftp)``.

::

    ##      start end
    ## [1,]    13  19
    ## [2,]    NA  NA
    ## [3,]     1   6

It’s often helpful to be able to save a pattern as a variable and refer back to
it. Here’s an example that might have been helpful in dealing with the extra
commas in the comma-delimited FEC elections data file in PS1:

::

    ## [1] "\"H4NY07011\",\"ACKERMAN GARY L.\",\"H\",\"$13242\",,,"

We can have multiple sets of parentheses, referred to using ``\\1``,
``\\2``, etc.

**Challenge**: Suppose a text string has dates in the form “Aug-3”,
“May-9”, etc. and I want them in the form “3 Aug”, “9 May”, etc. How
would I do this search/replace?

Greedy matching
~~~~~~~~~~~~~~~

It turns out the pattern matching is ’greedy’ - it looks for the longest
match possible.

Suppose we want to strip out html tags as follows:

::

    ## [1] "Do an internship  course."

What went wrong?

One solution is to append a ? to the repetition syntax to cause the
matching to be non-greedy. Here’s an example.

``  ``

::

    ## [1] "Do an internship  in place  of  one  course."

However, one can often avoid greedy matching by being more clever.

**Challenge**: How could we change our regexp to avoid the greedy
matching without using the “?”?

Regular expressions in other contexts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Regular expression can be used in a variety of places. E.g., to split by
any number of white space characters

::

    ## a dog    jumped
    ## over     the moon.

::

    ## [[1]]
    ## [1] "a"      "dog"    "jumped" "over"   "the"   
    ## [6] "moon."

::

    ## [[1]]
    ## [1] "a"            "dog"          "jumped\nover"
    ## [4] "the"          "moon."


.. tip:: **Globs vs. Regex:** 
    Be sure you understand the difference between filename globbing (see
    `the Section called *Filename Globbing* in Chapter 2 <basic-file-management.html#FILENAMEGLOBS>`_)
    and regular expressions.


``ed``, ``grep``, ``sed``, ``awk``, and ``perl``
------------------------------------------------

* :ref:`grep` -- print lines matching a pattern
* :ref:`tr` -- translate or delete characters

Before the text editor, there was the line editor.  Rather than presenting you
with the entire text as a text editor does, a line editor only displays lines
of text when it is requested to.  The original Unix line editor is called ``ed``.
You will likely never use ``ed`` directly, but you will very likely use commands
that are its ancestor.  For example, the commands ``grep``, ``sed``, ``awk``,
and ``vim`` are all based directly on ``ed`` (e.g., ``grep`` is a ``ed`` command
that is now available as a standalone command, while ``sed`` is a streaming
version of ``ed``) or inherit much of its syntax (e.g., ``awk`` and ``vim``
both heavily borrow from the ``ed`` syntax).  Since ``ed`` was written when
computing resources were very constrained compared to today, this means that
the syntax of these commands can be terse.  However, it also means that learning
the syntax for one of these tools will be rewarded when you need to learn the
syntax of another of these tools.

The simplest of these tools is ``grep``.  As I mentioned, ``ed`` only displays
lines of text when requested.  One common task was to print all the lines in
a file matching a specific regular expression.  The command in ``ed`` that
does this is ``g/<re>/p``, which stands for globally match all lines containing
the regular express ``<re>`` and print them out.  Consider the following example::

  $ cat file1.txt 
  This is the first line.
  Followed by a this line.
  And then ...
  $ grep is file1.txt 
  This is the first line.
  Followed by a this line.

Translating lowercase to UPPERCASE with ``tr``::

    $ echo 'user1'  | tr 'a-z' 'A-Z'
    USER1
        
Exercise
~~~~~~~~

Explain what the following regular expression matches::

  $ grep '^[^T]*is.*$' file1.txt
      

**sed** and **awk**
~~~~~~~~~~~~~~~~~~~


Printing lines of text with ``sed``::

    $ sed -n '1,9p' file.txt       # prints out lines 1-9 of file.txt 
    $ sed -n '/^#/p' file.txt       # prints out lines starting with # of file.txt 

The first command prints out lines 1-9 of ``file.txt``, while the second one
prints out lines starting with ``#`` of ``file.txt``.
  
Deleting lines of text with ``sed``::

    $ sed -e '1,9d' file.txt
    $ sed -e '/^;/d' -e '/^$/d' file.txt

The first line deletes lines 1-9 of ``file.txt``. What do you think the second
line does?

Text substitution with ``sed``::

    $ sed 's/old_pattern/new_pattern/' file.txt > new_file.txt
    $ sed 's/old_pattern/new_pattern/g' file.txt > new_file.txt

The first line replaces only 1st instance in a line, while the second line
replaces all instances in a line (i.e., globally).
 
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
~~~~~~~~

Text substitution with ``perl``::

    $ perl -pi -e 's/old_pattern/new_pattern/g' file.txt
    $ perl -pi -e 's/old_pattern/new_pattern/g' $(find . -name \*.html)

The ``i`` option tells ``perl`` to do the global substitution in place.
You can also substitute the ``/`` with another character. For
example::

    $ perl -pi -e 's:old_pattern:new_pattern:g' file.txt
      
Summing columns with ``perl``::

    $ perl -lane 'print $F[0] + $F[1]' file.txt

This will sum columns 1 and 2 of ``file.txt``.





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

* :ref:`ps` --  report process status
* :ref:`pstree` -- display a tree of processes
* :ref:`top` -- display top CPU processes

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

* :ref:`kill` -- terminate a process
* :ref:`killall` --  kill processes by name

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

* :ref:`bg` -- background
* :ref:`fg` -- foreground
* :ref:`jobs` -- list the active jobs
* :ref:`nohup` -- Run a command immune to hangups, with
  output to a non-tty

Starting a job
~~~~~~~~~~~~~~

When you run a command in a shell by simply typing its name, you are
said to be running in the foreground. When a job is running in the
foreground, you can’t type additional commands into that shell session,
but there are two signals that can be sent to the running job through
the keyboard. To interrupt a program running in the foreground, use
``Ctrl-c``; to quit a program, use ``Ctrl-\``. While modern windowed systems
have lessened the inconvenience of tying up a shell with foreground
processes, there are some situations where running in the foreground is
not adequate.

The primary need for an alternative to foreground processing arises when
you wish to have jobs continue to run after you log off the computer. In
cases like this you can run a program in the background by simply
terminating the command with an ampersand (``&``). However, before putting
a job in the background, you should consider how you will access its
results, since *stdout* is not preserved when you log off from the
computer. Thus, redirection (including redirection of *stderr*) is
essential when running jobs in the background. As a simple example,
suppose that you wish to run an R script, and you don’t want it to
terminate when you log off. (Note that this can also be done using
``R CMD BATCH``, so this is primarily an illustration.)

| ``$ R --no-save < code.R > code.Rout 2>&1 &``
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

  $ ps -aux

Among the output after the header (shown here) might appear a line
that looks like this::

  USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
  paciorek 11998 97.0 39.1 1416644 1204824 pts/16 R+ Jul27 1330:01 /usr/lib64/R/bin/exec/R

In this example, the *ps* output tells us that this R job has a PID of
*11998*, that it has been running for 1330 minutes (!), is using 97%
of CPU and 39% of memory, and that it started on July 27. You could
then issue the command::

  $ kill 11998

or, if that doesn’t work::

  $ kill -9 11998

to terminate the job. Another useful command in this regard is
*killall*, which accepts a program name instead of a process id, and
will kill all instances of the named program::

  $ killall R

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

  $ nice -19 R CMD BATCH --no-save code.R code.Rout &

If you forget and just submit the job without nicing, you can reduce
the priority by doing::

  $ renice +19 11998

where *11998* is the PID of your job.

On many larger UNIX cluster computers, all jobs are submitted via a job
scheduler and enter a queue, which handles the issue of prioritization
and jobs conflicting. Syntax varies by system and queueing software, but
may look something like this for submitting an R job:

``$ bsub -q long R CMD BATCH --no-save code.R code.Rout # just an example; this will not work on the SCF network``


bg,fg,jobs,Ctrl-C,Ctrl-Z

**screen**

Shell programming
=================

Shell scripts are files containing shell commands (commonly with the extension
``.sh``) To run a shell script called ``file.sh``, you would type ``source
./file.sh`` or ``. ./file.sh``. Note that if you just typed ``file.sh``, the
operating system will generally have trouble finding the script and recognizing
that it is executable. To be sure that the operating system knows what shell to
use to interpret the script, the first line of the script should be
``#!/bin/bash`` (in the case that you're using the bash shell). Also, if you
set ``file.sh`` to be executable (i.e., to have the 'x' flag set) you can
execute it by just typing ``./file.sh``.

Functions
---------

You can define your own utilities by creating a shell function. This
allows you to automate things that are more complicated than you can do
with an alias. One nice thing about shell functions is that the shell
automatically takes care of function arguments for you. It places the
arguments given by the user into local variables in the function called
(in order): ``$1 $2 $3`` etc. It also fills ``$#`` with the number of
arguments given by the user. Here’s an example of using arguments in a
function that saves me some typing when I want to copy a file to the SCF
filesystem::

  function putscf() {
     scp $1 paciorek@radagast.berkeley.edu:~/$2 ``
  }

To use this function, I just do the following to copy *unit1.pdf* from
the current directory on whatever non-SCF machine I’m on to the
directory *~/teaching/243* on SCF::

  $ putscf unit1-unix.pdf Desktop/.

Of course you’d want to put such functions in your ``.bashrc`` file.

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

We've covered most of what you are likely to need to know about the shell. I
tend to only use bash scripts for simple tasks that require only a few lines of
bash commands and very little control flow (i.e., conditional statements,
loops).  For more complicated OS tasks, it is often preferable to use Python.
You can also do a fair amount of what you need from within R using the
``system()`` function. This will enable you to avoid dealing with a lot of
shell programming syntax (but you’ll still need to know how to use UNIX
utilities, wildcards, and pipes to be effective). 

Documentation tools
===================

**markdown**, **restructured text**, latex

**pandoc**

Please see the "Introduction to LaTeX" tutorial and screencast
here: http://statistics.berkeley.edu/computing/training/tutorials

