##################################
On correlation and the dot product
##################################

We are going to implement `Pearson product-moment
correlation <https://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient>`__.

We have two vectors, :math:`\mathbf{x}` and :math:`\mathbf{y}`, each
with :math:`N` values, :math:`\mathbf{x} = x_0, x_1, ..., x_{N-1}`,
:math:`\mathbf{y} = y_0, y_1, ..., y_{N-1}`.

The sample mean is:

.. math::

   \bar{x}=\frac{1}{N}\sum_{i=0}^{N-1} x_i

In ``numpy`` this would just be ``np.mean(x)``.

The Pearson product-moment correlation coefficient between two vectors
:math:`\mathbf{x}, \mathbf{y}` is defined as:

.. math::

   r_{xy} =\frac{\sum ^{N-1} _{i=0}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum ^{N-1} _{i=0}(x_i - \bar{x})^2} \sqrt{\sum ^{N-1} _{i=0}(y_i - \bar{y})^2}}

:math:`(x_i - \bar{x})` is the vector :math:`\mathbf{x}` after it has
been *mean-centered* (it has a sample mean of zero).
