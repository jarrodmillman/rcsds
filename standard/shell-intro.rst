.. _intro-shell:

*************************
Introduction to the Shell
*************************

.. contents::

In order to be of interest to the user, a computer must have a
*human interface component*. If you come from the world of Windows
or MacOS, you should be familiar with the
*graphical user interface (GUI)*.
*Windows, Icons, Menus and Pointing device (WIMP)* are the basic
components of a GUI. The are advantages to the GUI--most important,
of which, is the "intuitive" nature of this interface.

In UNIX, there is another interface which reigns supreme: the
*command line interface (CLI)*. If you have ever used DOS, you have
all ready encountered a CLI; but, you probably have not been
convinced of its usefulness. Simply put, a CLI is a text based
interface. The user is given a *prompt* to indicate the computers
reeadiness to accept *input*. The user enters or types a *command*
on the line (or lines) following the prompt. The computer,
consequently, executes or interprets the command and prompts the
user when its finished.

The Interactive Shell
=====================

The program which prompts the user and interprets the user's
commands is called a *shell*. The original UNIX shell was written
by Steve Bourne and called simply **sh**. Today's shells have been
greatly enhanced. Since Linux' default shell is the GNU's **bash**
(or the Bourne Again Shell), I will focus on it. However, the basic
ideas are applicable to any of UNIX's shells.

The shell is an amazingly powerful programming environment--more
powerful than most non-UNIX users are accustomed to. From it you
can interactively control almost any aspect of the OS and more
importantly you can automate it. As you will see, **bash** has a
very extensive set of capabalities intended to make both
interactive as well as automated control simple, effective, and
customizable.

Logging In
----------

**Useful Commands**

* :ref:`command-su` -- run a shell with substitute user and group IDs
* :ref:`command-sudo` -- execute a command as another user

Shell Variables
---------------

**Useful Commands**

* :ref:`command-apropos` -- search the whatis database for strings
* :ref:`command-echo` -- display a line of text
* :ref:`command-which` -- shows the full path of (shell) commands.
* :ref:`command-whereis` -- locate the binary, source, and manual
                            page files for a command
* :ref:`command-whatis` -- search the whatis database for complete
                            words.
* :ref:`command-man` -- format and display the on-line manual pages
                     PS1, PATH, CDPATH

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
      

**Example 2-3. PATH**

::

    $ echo $PATH
    /bin:/usr/bin:/usr/X11R6/bin:/usr/local/bin
      

**Example 2-4. Finding **echo** with **which****

::

    $ which echo
    /bin/echo
      

type-type-all

**Example 2-5. Learning more about **echo** with **whereis**, **whatis**, and **man****

::

    $ whereis echo
    echo: /bin/echo /usr/share/man/man1/echo.1.bz2 /usr/share/man/man3/echo.3x.bz2
    $ whatis echo
    echo                 (1)  - display a line of text
    echo                 (3x)  - curses input options
    echo [builtins]      (1)  - bash built-in commands, see bash(1)
    echo [cbreak]        (3x)  - curses input options
    echo [curs_inopts]   (3x)  - curses input options
    echo [halfdelay]     (3x)  - curses input options
    echo [intrflush]     (3x)  - curses input options
    echo [keypad]        (3x)  - curses input options
    echo [meta]          (3x)  - curses input options
    echo [nocbreak]      (3x)  - curses input options
    echo [nodelay]       (3x)  - curses input options
    echo [noecho]        (3x)  - curses input options
    echo [noqiflush]     (3x)  - curses input options
    echo [noraw]         (3x)  - curses input options
    echo [notimeout]     (3x)  - curses input options
    echo [qiflush]       (3x)  - curses input options
    echo [raw]           (3x)  - curses input options
    echo [timeout]       (3x)  - curses input options
    echo [typeahead]     (3x)  - curses input options
    echo [wtimeout]      (3x)  - curses input options
    $ man echo
    ECHO(1)                        FSF                        ECHO(1)
    
    NAME
       echo - display a line of text

    SYNOPSIS
       echo [OPTION]... [STRING]...

    DESCRIPTION
       Echo the STRING(s) to standard output.

       -n     do not output the trailing newline

       -e     enable interpretation of the backslash-escaped characters listed below

       -E     disable interpretation of those sequences in STRINGs

       --help display this help and exit (should be alone)

       --version
          output version information and exit (should be alone)

       Without -E, the following sequences are recognized and interpolated:

       \NNN   the character whose ASCII code is NNN (octal)

       \\     backslash

       \a     alert (BEL)

       \b     backspace

       \c     suppress trailing newline

       \f     form feed

       \n     new line

       \r     carriage return

       \t     horizontal tab

       \v     vertical tab

    AUTHOR
       Written by FIXME unknown.

    REPORTING BUGS
       Report bugs to <bug-sh-utils@gnu.org>.

    COPYRIGHT
       Copyright � 2000 Free Software Foundation, Inc.
       This  is  free  software;  see  the  source  for copying conditions.  There is NO warranty; not even for MER�
       CHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    SEE ALSO
       The full documentation for echo is maintained as a Texinfo manual.  If the info and echo programs  are  prop�
       erly installed at your site, the command

          info echo

       should give you access to the complete manual.

    GNU sh-utils 2.0.11         March 2002                    ECHO(1)
    lines 1-69/69 (END)
        
      

Entering Commands
-----------------

General Syntax
~~~~~~~~~~~~~~

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
        
      

Command Sequences
~~~~~~~~~~~~~~~~~

Command History and Editing
---------------------------

**Useful Commands**  

* :ref:`command-history` -- lists the history of entered commands

**Example 2-7. Examing your command history with **history****

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
      

**Table 2-1. Command History Expansion**

==================   ==========================================================
Designator           Description
==================   ==========================================================
*!!*                 Last command
*!n*                 Command numbered *n* in the history
*!-n*                Command *n* previous
*!string*            Last command starting with *string*
*!?string*           Last command containing *string*
*^string1^string2*   Execute the previous command with *string2*
                     substituted for *string1*
==================   ==========================================================

Command Completion and Substitution
-----------------------------------

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

Keyboard shorcuts

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
* :ref:`command-dirs` -- Display the list of currently remembered
                         directories.
* :ref:`command-popd` --  Remove the top entry from the directory
                          stack, and cd to the new top directory.
* :ref:`command-pushd` -- Save the current directory on the top of
                           the directory stack and then cd to dir.
* :ref:`command-pwd` -- print name of current/working directory

**Example 2-13. Moving Around the Filesystem with **cd**, **pushd**, ~,and **pwd****

::

    $ cd ~
    $ pwd
    /home/user1
    
    $ pushd src/doc/
    ~/src/doc ~
    
    $ pwd
    /home/user1/src/doc
    
    $ pushd
    ~ ~/src/doc
    
    $ pwd
    /home/user1
        
      

Manipulation
------------

**Useful Commands**  

* :ref:`command-cat` -- concatenate files and print on the standard output
* :ref:`command-cp`-- copy files and directories
* :ref:`command-diff`-- find differences between two files
* :ref:`command-diff3`-- find differences between three files
* :ref:`command-sdiff`-- find differences between two files and merge interactively
* :ref:`command-comm` -- Compare two sorted files line by line
* :ref:`command-cmp` --  compare two files or byte ranges
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

**Table 2-3. File-Naming Wildcards**

=========================== ==================================================
Wildcard                    Function
=========================== ==================================================
*\\*                        Match zero or more characters.
*?*                         Match exactly one character.
*[characters]*              Match any single character from among *characters*
                            listed between brackets.
*[!characters]*             Match any single character other than *characters*
                            listed between brackets.
*[a-z]*                     Match any single character from among the range of
                            characters listed between brackets.
*[!a-z]*                    Match any single character from among the characters
                            not in the range listed between brackets
*{frag1, frag2, frag3,...}* Brace expansion: create strings frag1, frag2, and
                            frag3, etc.
=========================== ==================================================

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
*' '*                hard quote - no substitution allowed
*" "*                soft quote - allow substitution
*` `*                execute immediately
=================    ====================================
