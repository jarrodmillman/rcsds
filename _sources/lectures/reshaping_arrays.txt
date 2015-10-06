################
Reshaping arrays
################

The obvious example - making an array flat (1D):

.. testsetup::

    import os
    os.chdir('lectures')
    import numpy as np

Here is a 2D array, shape (2, 6):

>>> arr = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
>>> arr
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])

We can reshape to a 1D array (as we've seen already):

>>> arr_1d = np.reshape(arr, 12)
>>> arr_1d
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

Notice what happened. Numpy first makes an output array shape ``(12,)``. It
then proceeds along the *last* axis, element by element, taking the element
and putting it into the output array. When it has finished each line on the
last axis, it continues to the next line (on the second-to-last axis).

We can reverse the process, like this:

>>> np.reshape(arr_1d, (2, 6))
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])

In the example above, numpy can work out how large the second dimension
should be, because it knows it is starting with 12 elements. You can use
the value ``-1`` to say "a dimension length of the right size to use the
rest of the input array". For example:

>>> np.reshape(arr_1d, (2, -1))
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])


>>> np.reshape(arr_1d, (-1, 6))
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])

When doing the reshape, numpy first creates the output array of the given
shape (2, 6), then fills the last dimension first, just like the case of
reshaping to 1D.

Making an N-D array into a 1D array is very common, so numpy has a short-cut
for that:

>>> arr.ravel()
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

For a 3D array, there are three axes. In this case numpy first proceeds along
the lines over the third axis. When it reaches the end of the line it moves to
the next line on the *second* axis, and when it gets to the end of the second
axis it goes to the first axis.

>>> arr_3d = np.array([ # now define first of 2 2D arrays (arr_3d[0, :, :])
...                     [[0,  1,  2,  3],
...                      [4,  5,  6,  7],
...                      [8,  9, 10, 11]],
...                     # define second of 2 2D arrays (arr_3d[1, :, :])
...                     [[12, 13, 14, 15],
...                      [16, 17, 18, 19],
...                      [20, 21, 22, 23]]
...                   ])
>>> arr_3d
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],
<BLANKLINE>
       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])

>>> n_elements = 2 * 3 * 4
>>> np.reshape(arr_3d, n_elements)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23])

You can reshape to any shape. For example, you might want to reshape only the
first two dimensions, leaving the last the same. This will take you from an
array of shape (2, 3, 4), to an array of shape (6, 4). The procedure is the
same in numpy. It makes an output array shape (6, 4), then takes each element
over the last dimension in the input, and fills the last dimension of the
output, moves one across on the second dimension of the input, then fills
a line in the first dimension of the output, and so on.

>>> arr_2d = np.reshape(arr_3d, (6, 4))
>>> arr_2d.shape
(6, 4)

>>> arr_2d
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23]])

Of course we can do this with image data arrays:

>>> import nibabel as nib
>>> img = nib.load('ds114_sub009_t2r1.nii')
>>> data = img.get_data()
>>> data.shape
(64, 64, 30, 173)

>>> vol_shape = data.shape[:-1]
>>> vol_shape
(64, 64, 30)

Here I am using the ``np.prod`` function, which is like ``np.sum``, but
instead of adding the elements, it multiplies them:

>>> n_voxels = np.prod(vol_shape)
>>> n_voxels
122880

>>> voxel_by_time = np.reshape(data, (n_voxels, data.shape[-1]))
>>> voxel_by_time.shape
(122880, 173)

I can also use the -1 trick for this:

>>> voxel_by_time = np.reshape(data, (n_voxels, -1))
>>> voxel_by_time.shape
(122880, 173)

.. testcleanup::

    os.chdir('..')
