######################################
Reading numerical data from text files
######################################

Reading text files
------------------

We've been reading values from text files in the exercises.

Here is some revision on how to do that, going from the crude to the
elegant way.

I first write a little text file out to disk:

.. code:: python

    numbers = [1.2, 2.3, 3.4, 4.5]
    fobj = open('some_numbers.txt', 'wt')
    for number in numbers:
        # String version of number, plus end-of-line character
        fobj.write(str(number) + '\n')
    fobj.close()

Now I read it back again. First, I will just read the strings:

.. code:: python

    fobj = open('some_numbers.txt', 'rt')
    lines = fobj.readlines()

Next I will read the file, but converting each number to a float:

.. code:: python

    fobj = open('some_numbers.txt', 'rt')
    numbers_again = []
    for line in fobj.readlines():
        numbers_again.append(float(line))
    numbers_again

This gives:

.. parsed-literal::

    [1.2, 2.3, 3.4, 4.5]

In fact we can do this even more simply by using ``np.loadtxt``:

.. code:: python

    import numpy as np
    np.loadtxt('some_numbers.txt')

.. parsed-literal::

    array([ 1.2,  2.3,  3.4,  4.5])

