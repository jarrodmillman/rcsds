.. _command-popd:

popd
====

Name
----

popd --  Remove the top entry from the directory stack, and cd to
the new top directory.

Synopsis
--------

**popd** [option...]

Description
-----------

Remove the top entry from the directory stack, and cd to the new
top directory. When no arguments are given, popd removes the top
directory from the stack and performs a cd to the new top
directory.

Frequently used options
-----------------------

- +N 
    Removes the Nth directory (counting from the left of the list
    printed by dirs), starting with zero.

- -N 
    Removes the Nth directory (counting from the right of the list
    printed by dirs), starting with zero.



