########################################
Making sure you have floating point data
########################################

*******
Summary
*******

Always convert your image data to floating point number format, before doing
numerical operations.

***********
Explanation
***********

When you load use nibabel_ to load the image data, you need to be careful
about the array data type.

Remember that numpy_ arrays have a ``dtype``.  This is the type of the element
in the array.  See the `scipy lecture notes on dtypes
<http://www.scipy-lectures.org/intro/numpy/array_object.html#basic-data-types>`_
for more detail.

When you load the image data from disk, the array has a ``dtype``, that
depends on the way the data was stored on disk.  For example, nibabel returns
our example image data as an array of signed 16-bit integers:

.. testsetup::

    import os
    os.chdir('lectures')

>>> import nibabel as nib
>>> img = nib.load('ds114_sub009_t2r1.nii')
>>> data = img.get_data()
>>> data.dtype
dtype('<i2')
>>> data.dtype.type
<type 'numpy.int16'>

A 16-bit integer is an integer that can store the numbers from $-2^{15}$ to
$2^{15}-1$.   Unfortunately, you have to be very careful when using arrays
like this, because if you do operations that generate a number outside this
range, strange things will happen.  This is due to `integer overflow
<https://en.wikipedia.org/wiki/Integer_overflow>`_

For example, let's make an array with the maximum and minimum numbers that the
np.int16 datatype can store:

>>> import numpy as np
>>> int_arr = np.array([-2**15, 2**15-1], dtype=np.int16)
>>> int_arr
array([-32768,  32767], dtype=int16)

Now if we add 1, the max value is outside the range that can be stored in this
datatype, and we get integer overflow.  The max number wraps round to give the
most negative number the type can store:

>>> int_arr + np.array(1, dtype=np.int16)
array([-32767, -32768], dtype=int16)

The same kind of thing happens when we subtract 1:

>>> int_arr - np.array(1, dtype=np.int16)
array([32767, 32766], dtype=int16)

One operation where this can cause severe problems is the dot product of one
integer matrix with another.  The result will all be integers, but because we
are doing many multiplications and sums, the dot product result very often
overflows the values the datatype can contain, and therefore gives nonsense
answers:

>>> int_arr2 = np.zeros((2, 3), dtype=np.int16) + np.int16(3201)
>>> int_arr2
array([[3201, 3201, 3201],
       [3201, 3201, 3201]], dtype=int16)
>>> int_arr2.T.dot(int_arr2)
array([[-19966, -19966, -19966],
       [-19966, -19966, -19966],
       [-19966, -19966, -19966]], dtype=int16)

The best way to avoid this, is to default to casting the integer numbers into
floating point numbers.  These can store much wider range of numbers to a
reasonable precision, and the calculations are usually very quick because
modern computers are highly optimized for floating point values:

>>> float_arr2 = int_arr2.astype(float)
>>> float_arr2
array([[ 3201.,  3201.,  3201.],
       [ 3201.,  3201.,  3201.]])
>>> float_arr2.T.dot(float_arr2)
array([[ 20492802.,  20492802.,  20492802.],
       [ 20492802.,  20492802.,  20492802.],
       [ 20492802.,  20492802.,  20492802.]])
>>> 3201**2 * 2
20492802

These problems only occur when the output array is also the integer type.  For
example, if I did a dot product of an integer array with a floating point
array, numpy is intelligent enough to know it will need a floating point array
as output, and you do not get overflow:

>>> int_arr2.T.dot(float_arr2)
array([[ 20492802.,  20492802.,  20492802.],
       [ 20492802.,  20492802.,  20492802.],
       [ 20492802.,  20492802.,  20492802.]])

.. testcleanup::

    os.chdir('..')

.. include:: ../links_names.inc
