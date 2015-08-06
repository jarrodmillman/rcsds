.. _data-manipulation:

*****************
Data Manipulation
*****************

.. contents::

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
*^*          Match the beginning of a line.
*$*          Match the end of a line.
=========  ====================================================================

**Character sets**

=============    ====================================================================
Operators        Description
=============    ====================================================================
*[abc]*          Match any single character from from the listed characters
*[a-z]*          Match any single character from the range of characters
*[^abc]*         Match any single character not among listed characters
*[^a-z]*         Match any single character not among listed range of characters
*\\< word\\>*    Match *words* bounded by whitespace.
*.*              Match any single character expcept a *newline*
*\\*             Turn off (escape) the special meaning of a metacharacter
=============    ====================================================================

**Modifiers**

=============    ====================================================================
Operators        Description
=============    ====================================================================
*\**             Match zero or more of the character that precedes it.
*?*              Match zero or one instace of the preceding *regex*.
*+*              Match one or more instances of the preceding *regex*.
*\\{n,m\\}*      Match a range of occurrences of the single character or *regex*
                 that precedes this construct.
*\|*             Match the character or expression to the left or right of the
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
      

