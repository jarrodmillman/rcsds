#####################
Basic linear modeling
#####################

In this exercise we will run a simple regression on all voxels in a 4D
FMRI image.

.. plot::
    :context:
    :nofigs:

    >>> # import some standard librares
    >>> import numpy as np
    >>> import numpy.linalg as npl
    >>> import matplotlib.pyplot as plt
    >>> import nibabel as nib

.. plot::
    :context:
    :nofigs:

    >>> # Load the image as an image object

.. plot::
    :context:
    :nofigs:

    >>> # Load the image data as an array
    >>> # Drop the first 4 3D volumes from the array
    >>> # (We already saw that these were abnormal)

.. plot::
    :context:
    :nofigs:

    >>> # Load the pre-written convolved time course
    >>> # Knock off the first four elements

.. plot::
    :context:
    :nofigs:

    >>> # Compile the design matrix
    >>> # First column is convolved regressor
    >>> # Second column all ones

.. plot::
    :context:
    :nofigs:

    >>> # Reshape the 4D data to voxel by time 2D
    >>> # Transpose to give time by voxel 2D
    >>> # Calculate the pseudoinverse of the design
    >>> # Apply to time by voxel array to get betas

.. plot::
    :context:
    :nofigs:

    >>> # Tranpose betas to give voxels by 2 array
    >>> # Reshape into 4D array, with same 3D shape as original data,
    >>> # last dimension length 2

.. plot::
    :context:
    :nofigs:

    >>> # Show the middle slice from the first beta volume

.. plot::
    :context:
    :nofigs:

    >>> # Show the middle slice from the second beta volume

.. include:: ../links_names.inc
