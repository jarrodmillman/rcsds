############################
Correlation per voxel, in 2D
############################

In this exercise, we will take each voxel time course in the brain, and calculate a correlation between the task-on / task-off vector and the voxel time course.  We then make a new 3D volume that contains correlation values for each voxel.

You've done this before in the exercise :doc:`correlation_each_voxel`, but this time we'll do it by reshaping the 4D data to 2D, and looping over the long voxels axis instead of over each of the three spatial axes.

We've given you the stuff you will have done already for the previous exercise - you can copy-paste into IPython.

.. code:: python

    # - import common modules
    import numpy as np  # the Python array package
    import matplotlib.pyplot as plt  # the Python plotting package

.. code:: python

    # import events2neural from stimuli module
    from stimuli import events2neural

.. code:: python

    import nibabel as nib

.. code:: python

    # Load the ds114_sub009_t2r1.nii image
    img = nib.load('ds114_sub009_t2r1.nii')

.. code:: python

    # Get the number of volumes in ds114_sub009_t2r1.nii
    n_trs = img.shape[-1]

The TR (time between scans) is 2.5 seconds.

.. code:: python

    TR = 2.5

Call the ``events2neural`` function to give you a time course that is 1
for the volumes during the task (thinking of verbs) and 0 for the
volumes during rest.

.. code:: python

    time_course = events2neural('ds114_sub009_t2r1_cond.txt', 2.5, n_trs)

.. code:: python

    # Using slicing, drop the first 4 volumes, and the first 4 on-off values
    data = img.get_data()
    data = data[..., 4:]
    time_course = time_course[4:]

.. code:: python

    # Calculate the number of voxels (number of elements in one volume)

Now, reshape the 4D data to a 2D array shape (number of voxels, number
of volumes).

.. code:: python

    # Reshape 4D array to 2D array n_voxels by n_volumes

.. code:: python

    # Make a 1D array of size (n_voxels,) to hold the correlation values

Now loop over all voxels, calculate the correlation coefficient with
``time_course`` at this voxel, and fill in the corresponding entry in your 1D
array.

.. code:: python

    # Loop over voxels filling in correlation at this voxel

Reshape the correlations 1D array back to a 3D array, using the original 3D
shape.

.. code:: python

    # Reshape the correlations array back to 3D

If all went well, you should have generated the same 3D volume of correlations as you did for the original exercise:

.. code:: python

    # Plot the middle slice of the third axis from the correlations array
    plt.imshow(correlations[:, :, 14], cmap='gray')
