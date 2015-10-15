#####################################
Correlation per voxel, the faster way
#####################################

You are going to use your new super-fast correlation routine to recalculate
the voxel correlation volumne

We've given you the stuff you will have done already for the previous exercise
- you can copy-paste into IPython.

If you don't have them already you will need these files in your working
directory:

* :download:`ds114_sub009_t2r1.nii <../_downloads/ds114_sub009_t2r1.nii>`
* :download:`ds114_sub009_t2r1_cond.txt <../_downloads/ds114_sub009_t2r1_cond.txt>`

First, import ``sys`` and append the directory containing your ``pearson.py``
module to ``sys.path``:

.. code:: python

    # Import sys, and append directory to sys.path

Check you can import ``pearson`` and ``stimuli``.  Call over someone to help
if you can't.

.. code:: python

    import pearson
    import stimuli

Now load up the data, and get the on-off time course (neural prediction):

.. code:: python

    # - import common modules
    import numpy as np  # the Python array package
    import matplotlib.pyplot as plt  # the Python plotting package

    # import events2neural from stimuli module
    from stimuli import events2neural

    # Load the ds114_sub009_t2r1.nii image
    import nibabel as nib
    img = nib.load('ds114_sub009_t2r1.nii')

    # Get the number of volumes in ds114_sub009_t2r1.nii
    n_trs = img.shape[-1]

    # Time between 3D volumes in seconds
    TR = 2.5

    # Get on-off timecourse
    time_course = events2neural('ds114_sub009_t2r1_cond.txt', 2.5, n_trs)

    # Drop the first 4 volumes, and the first 4 on-off values
    data = img.get_data()
    data = data[..., 4:]
    time_course = time_course[4:]

Now the real work.

.. code:: python

    # Calculate the number of voxels (number of elements in one volume)

Reshape the 4D data to a 2D array shape (number of voxels, number of volumes).

.. code:: python

    # Reshape 4D array to 2D array n_voxels by n_volumes

Transpose the array to make a (number of volumes, number of voxels) array.

.. code:: python

    # Transpose 2D array to give n_volumes, n_voxels array

Use the `pearson_2d` function to return the correlation coefficients with
``time_series`` at each voxel:

.. code:: python

    # Calculate 1D vector length n_voxels of correlation coefficients

You might have noticed this is much faster than doing the correlation by
looping over each voxel.

Reshape the correlations 1D array back to a 3D array, using the original 3D
shape.

.. code:: python

    # Reshape the correlations array back to 3D

If all went well, you should have generated the same 3D volume of correlations
as you did for the original exercise:

.. code:: python

    # Plot the middle slice of the third axis from the correlations array
    plt.imshow(correlations[:, :, 14], cmap='gray')
