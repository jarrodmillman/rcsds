.. _more-shell:

*****************
More on the Shell
*****************

.. contents::

Streams, Pipes, and Redirects
=============================

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

**Table 3-2. Common Redirection Operators**

===========================   ===============================================
Redirection Syntax            Function
===========================   ===============================================
*$ cmd > file*                 Send *stdout* to *file*            
*$ cmd 1> file*                Same as above
*$ cmd 2> file*                Send *stderr* to *file*
*$ cmd > file 2>&1*            Send both *stdout* and *stderr* to *file*
*$ cmd < file*                 Receive *stdin* from *file*
*$ cmd >> file*                Append *stdout* to *file*:
*$ cmd 1>> file*               Same as above
*$ cmd 2>> file*               Append *stderr* to *file*
*$ cmd >> file 2>&1*           Append both *stdout* and *stderr* to *file*
*$ cmd1 \| cmd2*               Pipe *stdout* from *cmd1* to *cmd2*
*$ cmd1 2>&1 \| cmd2*          Pipe *stdout* and *stderr* from *cmd1* to *cmd2*
*$ cmd1 tee file1 \| cmd2*     Pipe *stdout* and *cmd1* to *cmd2* while
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

bg,fg,jobs,Ctrl-C,Ctrl-Z

