#####################
Testing with ``nose``
#####################

Today we will start using a utility called ``nose`` to test our code::

    pip install --user nose

When we write code, most of the time, we make mistakes. These mistakes can be
hard to see.

Most untrained programmers write code, try it a few times at the interactive
prompt, get the answers they expect, and then assume the code is OK.

Long experience shows that this is rarely true. "Code that is not tested, must
be assumed to be broken".

* The code may give the right answer for some inputs and the wrong answer for
  others that you didn't test;
* The code may not work on another system or configuration.

The main way to reduce these problems is to write tests.

For example, let's say I had a module called ``mymodule``, like this::

    # file mymodule.py
    def do_div(arg1, arg2):
        return arg1 / arg2

Interactively, I might try a few numbers:

.. code:: python

    from mymodule import do_div
    do_div(1, 1)

.. code:: python

    do_div(0, 1)

That looks right so far. But I forgot that Python 2.7 does integer division by
default:

.. code:: python

    do_div(1, 2)

This gives the answer 0.

Oops, that wasn't what I wanted. And I might even have tested this on
Python 3 and not realized I would have a problem on Python 2 (why?).

What I should have done, was write a test for this function. A test written for
``nose`` looks like this::

    # file test_mymodule.py
    from nose.tools import assert_equal

    from mymodule import do_div

    def test_do_div():  # any name starting with 'test is a test
        assert_equal(do_div(1, 1), 1)
        assert_equal(do_div(0, 1), 0)
        assert_equal(do_div(1, 2), 0.5)  # The one that I got wrong

We usually write these out as a separate file module, named after the module it
is testing. In this case the file is ``test_mymodule.py``.

I run the tests using the ``nosetests`` command line utility::

    nosetests test_mymodule.py

Luckily I thought to test this case. Now I have tested it, I can fix it
(how?), and then I can keep testing it every time I edit the code, to
make sure I haven't broken anything. This turns out to be very
important.
