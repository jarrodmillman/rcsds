#####################
Dot products in numpy
#####################

.. testsetup::

    import numpy as np

If I have two vectors :math:`\mathbf{a}` with elements :math:`a_0, a_1, ...
a_{n-1}`, and :math:`\mathbf{b}` with elements :math:`b_0, b_1, ... b_{n-1}`
then the `dot product <https://en.wikipedia.org/wiki/Dot_product>`__ is
defined as:

.. math::

   \mathbf{a}\cdot \mathbf{b} = \sum_{i=0}^{n-1} a_ib_i = a_0b_0 + a_1b_1 + \cdots + a_{n-1}b_{n-1}

In code:

>>> a = np.arange(5)
>>> b = np.arange(10, 15)
>>> np.dot(a, b)
130

We could do exactly the same calculation using elementwise multiplication followed by a ``sum``:

>>> np.sum(a * b)  # Elementwise multiplication
130

Matrix multiplication operates by taking dot products of the rows of the
first array (matrix) with the columns of the second.

Let's say I have a matrix :math:`\mathbf{X}`, and :math:`X_{i,:}` is row
:math:`i` in :math:`\mathbf{X}`. I have a matrix :math:`\mathbf{Y}`, and
:math:`Y_{:,j}` is column :math:`j` in :math:`\mathbf{Y}`. The output matrix
:math:`\mathbf{Z} = \mathbf{X} \mathbf{Y}` has entry :math:`Z_{i,j} = X_{i,:}
\cdot Y_{:, j}`.

>>> X = np.array([[0, 1, 2], [3, 4, 5]])
>>> X
array([[0, 1, 2],
       [3, 4, 5]])

>>> Y = np.array([[7, 8], [9, 10], [11, 12]])
>>> Y
array([[ 7,  8],
       [ 9, 10],
       [11, 12]])

The numpy array ``dot`` method does this operation:

>>> X.dot(Y)
array([[ 31,  34],
       [112, 124]])


>>> X[0, :].dot(Y[:, 0])
31

>>> X[1, :].dot(Y[:, 0])
112
