Scientific computing with Python
================================

.. contents::


Introduce Python’s core numerical, scientific, and plotting packages.

-  Fernando Pérez, Brian E. Granger, and John D. Hunter. “Python: an
   ecosystem for scientific computing.” *Computing in Science &
   Engineering* 13, no. 2 (2011): 13-21.

-  Stéfan van der Walt, S. Chris Colbert, and Gael Varoquaux. “The NumPy
   array: a structure for efficient numerical computation.” *Computing
   in Science & Engineering* 13, no. 2 (2011): 22-30.

-  John D. Hunter. “Matplotlib: A 2D graphics environment.” *Computing
   in Science & Engineering* 9, no. 3 (2007): 0090-95.

Introduction
------------

-  http://docs.scipy.org/doc/

-  http://matplotlib.org/gallery.html

-  https://scipy-lectures.github.io/

-  https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks

NumPy and matplotlib
--------------------

Exercise: lock ’n load
~~~~~~~~~~~~~~~~~~~~~~

For this exercise please work through Stéfan van der Walt’s NumPy lock
’n load.

-  https://github.com/stefanv/teaching/tree/master/2008_numpy_load_n_load

-  http://mentat.za.net/numpy/intro/intro.html

ndarray
~~~~~~~

-  http://scipy-lectures.github.io/intro/numpy/array_object.html

-  http://scipy-lectures.github.io/intro/numpy/operations.html

2D plotting
~~~~~~~~~~~

-  http://scipy-lectures.github.io/intro/matplotlib/matplotlib.html

Example: random walk redux
--------------------------

Recall the random walk simulation from 243.

Here is a version implemented as a class.

Exercise: Sierpinski triangle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Write a Python script to construct Sierpinski triangle using the
following algorithm:

#. Choose 3 points in the plane (forming a triangle).

#. Choose another “starting” pointing (current position).

#. Randomly choose one of the corners of the triangle.

#. Move halfway from your current position to the selected corner.

#. Plot the new current position.

#. Repeat from step 3 (for 100 times).

SciPy
-----

-  http://scipy-lectures.github.io/intro/scipy.html

Exercise: State of the Union addresses
--------------------------------------

For this exercise, you will revisit the State of the Union Addresses.
Load the data, use whatever tools and analysis you want, and use
matplotlib to make plots.
