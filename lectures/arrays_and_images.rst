#################
Arrays and images
#################

The main point of this class is to show that you can consider arrays
as images, and images as arrays.

Let's make an array of numbers between 0 through 99:

.. code:: python

    an_array = np.array([[ 0,  0,  0,  0,  0,  0,  0,  0],
                         [ 0,  0,  0,  9, 99, 99, 94,  0],
                         [ 0,  0,  0, 25, 99, 99, 79,  0],
                         [ 0,  0,  0,  0,  0,  0,  0,  0],
                         [ 0,  0,  0, 56, 99, 99, 49,  0],
                         [ 0,  0,  0, 73, 99, 99, 31,  0],
                         [ 0,  0,  0, 91, 99, 99, 13,  0],
                         [ 0,  0,  9, 99, 99, 94,  0,  0],
                         [ 0,  0, 27, 99, 99, 77,  0,  0],
                         [ 0,  0, 45, 99, 99, 59,  0,  0],
                         [ 0,  0, 63, 99, 99, 42,  0,  0],
                         [ 0,  0, 80, 99, 99, 24,  0,  0],
                         [ 0,  1, 96, 99, 99,  6,  0,  0],
                         [ 0, 16, 99, 99, 88,  0,  0,  0],
                         [ 0,  0,  0,  0,  0,  0,  0,  0]])
    an_array.shape

In fact this array represents a monochrome picture of a letter.

As we've seen, we can show arrays as images using the ``plt.imshow`` command.

.. code:: python

    plt.imshow(an_array)

The image looks rather blurry. This is because matplotlib is drawing
an image with many more pixels than the array has values. For the
pixels in-between array values, matplotlib is using *interpolation* to
estimate a good value.  I suggest you always turn off interpolation
like this:

.. code:: python

    plt.imshow(an_array, interpolation='nearest')

The image is weirdly colorful. That is because matplotlib is using the
default *colormap*. A colormap is a mapping from values in the array
to colors. In this case the default colormap is called ``jet`` and
maps low numbers in the image (0 in our case) to blue, and high
numbers (99 in our case) to red.

We can see what the colormap is doing by asking for a color bar:

.. code:: python

    plt.imshow(an_array, interpolation='nearest')
    plt.colorbar()

In our case, our image would make more sense as grayscale, so we use
the ``gray`` colormap, like this:

.. code:: python

    plt.imshow(an_array, interpolation='nearest', cmap=plt.cm.gray)
    plt.colorbar()

We can specify the colormap with a string, if we know it.  This gives the same output as the command above:

.. code:: python

    plt.imshow(an_array, interpolation='nearest', cmap='gray')
    plt.colorbar()

A grayscale image is an array containing numbers giving the pixel
intensity values - in our case between 0 and 99.

We can also plot lines from the array. For example, we might want to
plot row 8 out of this array (the 9th row):

.. code:: python

    plt.plot(an_array[8])

The x axis is the position in the array (0 through 7) and the y axis
is the value of the array row at that position.

The plot shows us the 0 values at the edges of the bar of the "i", an
the ramp up to the peak at the middle of the bar of the "i", in
columns number 3 and 4.

A transpose in numpy uses the ``.T`` method on the array. This has the
effect of flipping the rows and columns (in 2D):

.. code:: python

    an_array.T

.. code:: python

    plt.imshow(an_array.T, interpolation='nearest', cmap='gray')

We can also reshape the original array to a 1D array, by stacking all
the rows end to end:

.. code:: python

    n_pixels = an_array.shape[0] * an_array.shape[1]
    a_1d_array = np.reshape(an_array, (n_pixels,))
    a_1d_array

.. code:: python

    a_1d_array.shape

Reshaping the array to one dimension is a common operation, so there
is a separate numpy command for that, ``np.ravel``:

.. code:: python

    np.ravel(an_array)

One use of the 1D version of the array, is for getting a histogram of
the distribution of values in the array:

.. code:: python

    plt.hist(a_1d_array)

By default, the ``plt.hist`` function uses 50 bins, but you can
specify how many bins you want with the ``bins`` keyword:

.. code:: python

    plt.hist(a_1d_array, bins=75)

As you can imagine, it's easy to go back to the 2D shape, by splitting
the 1D array back into 15 rows of 8 values each (and therefore
8 columns):

.. code:: python

    array_back = np.reshape(a_1d_array, (15, 8))
    array_back

.. code:: python

    plt.imshow(array_back, interpolation='nearest', cmap='gray')

In numpy, basic operations like multiplication, addition, comparison,
are always elementwise. For example, this multiplies every array value
by 10:

.. code:: python

    an_array * 10

Comparison is also elementwise. For example, this gives True for every
value > 50, and False for every value <= 50:

.. code:: python

    an_array > 50

Matplotlib will treat False as 0 and True as 1, so this is one way of
binarizing the image at a threshold (of 50 in this case):

.. code:: python

    plt.imshow(an_array > 50, interpolation='nearest', cmap='gray')

We can slice arrays as we slice strings or lists. The difference for
arrays is that we can slice in any or all dimensions at the same time.
For example, to get the dot of the "i" it looks (from the numbers at
the sides of the plot) that we want to the top 4 rows, and the last
5 columns:

.. code:: python

    an_array[0:4, 3:]

.. code:: python

    plt.imshow(an_array[0:4, 3:], interpolation='nearest', cmap='gray')

**********************************
Some final notes for the exercises
**********************************

Converting strings to floating point values:

.. code:: python

    float('1.34')

This is integer division:

.. code:: python

    1 // 2
