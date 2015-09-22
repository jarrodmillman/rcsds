#############
Simple arrays
#############

5 minutes.

Create this array::

   2  7 12  0
   3  9  3  4
   4  0  1  3

What is the array ``shape``?

What is the array ``ndim``?

How about the ``len`` of the array?

Can you get the ``ndim`` and ``len`` from the shape?

###############################
Creating arrays using functions
###############################

10 minutes.

1. Create a 1D array from 2 through 5 inclusive.

2. Make an array with 10 elements between 2 and 5 inclusive.

3. Make an all-ones array shape (4, 4).

4. Make an identity array shape (6, 6).

5. Make this array with a single Python / numpy command::

    1  0  0
    0  2  0
    0  0  3

Look at the docstring for ``np.random.randn``.  Make a shape (3, 5) array with random numbers from a mean=0, variance = 1 normal distribution.

#####################
Simple visualizations
#####################

7 minutes.

1. Make an array ``x`` with 100 evenly spaced values between 0 and 2 * pi;

2. Make an array ``y`` which contains the cosine of the corresponding value in
   ``x`` - so ``y[i] = cos(x[i])`` (hint: ``np.lookfor('cosine')``).

3. Plot ``x`` against ``y``;

4. Make a 10 by 20 array of mean 0 variance 1 normal random numbers;

5. Display this array as an image;

6. Investigate ``plt.cm``.  See if you can work out how to make the displayed
   image be grayscale instead of color.

####################################
Indexing and slicing, array creation
####################################

10 minutes.

1. Create the following array, call this ``a`` (you did this before)::

    2  7 12  0
    3  9  3  4
    4  0  1  3

2. Get the 2nd row of ``a`` (``[ 3 9 3 4]``);

3. Get the 3rd column of ``a`` (``[12 3 1]``);

Then continue with lecture exercises on "array creation". If you have time, go
onto the "tiling" section.

###################################
Fancy indexing using boolean arrays
###################################

5 minutes.

1. Create the following array ``a`` (same as before)::

    2  7 12  0
    3  9  3  4
    4  0  1  3

2. Use ``>`` to make a mask that is true where the elements are greater than
   5, like this::

    False True  True  False
    False True  False False
    False False False False

3. Return all the elements in ``a`` that are greater than 5.

4. Set all the elements greater than 5 to be equal to 5, to get this::

    2  5  5  0
    3  5  3  4
    4  0  1  3

######################
Elementwise operations
######################

10 minutes.

Remember our array ``a``::

   2  7 12  0
   3  9  3  4
   4  0  1  3

1. Use array slicing to get a new array composed of the even columns (0, 2) of
   ``a``. Now get array that contains the odd columns (1, 3) of ``a``.  Add
   these two arrays.

2. Generate this array::

    [2**0, 2**1, 2**2, 2**3, 2**4]

3. Generate an array length 10 such that this is true of the elements (where
   ``x[i]`` is the element of ``x`` at index ``i``)::

    x[i] = 2 ** (3 * i) - i

#################
Summary functions
#################

Remember our array ``a``::

   2  7 12  0
   3  9  3  4
   4  0  1  3

What are the:

* sum of all the values?
* mean?
* min?
* max?
