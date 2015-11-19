##########################################
Finding the location of a voxel coordinate
##########################################

.. nbplot::

    >>> import numpy as np
    >>> import numpy.linalg as npl
    >>> import nibabel as nib

We can load some data matched to a standard brain template::

    >>> img = nib.load('filtered_func_data_mni.nii.gz')

.. nbplot::
    :include-source: false

    >>> # Simulate an image for the output below
    >>> class FakeImage(object): pass
    >>> img = FakeImage()
    >>> img.shape = (91, 109, 91, 240)
    >>> img.affine = np.array([[  -2.,    0.,    0.,   90.],
    ...                        [   0.,    2.,    0., -126.],
    ...                        [   0.,    0.,    2.,  -72.],
    ...                        [   0.,    0.,    0.,    1.]])

.. nbplot::

    >>> img.shape
    (91, 109, 91, 240)

The ``affine`` attribute of the image contains the mapping from voxel
coordinates to millimeters in the space of the image.   In this case the image
is matched a particular standard template called the MNI template:

.. nbplot::

    >>> img.affine
    array([[  -2.,    0.,    0.,   90.],
           [   0.,    2.,    0., -126.],
           [   0.,    0.,    2.,  -72.],
           [   0.,    0.,    0.,    1.]])

We can get the mm coordinate for a particular voxel coordinate by applying
this affine to a particular voxel coordinate.  See `Coordinate transformations
<http://nipy.org/nibabel/coordinate_systems.html>`_ for a full explanation.

.. nbplot::

    >>> vox_to_mm = img.affine
    >>> nib.affines.apply_affine(vox_to_mm, [2, 3, 4])
    array([  86., -120.,  -64.])

The mapping from millmeter coordinate to voxel coordinates is just the inverse
of ``img.affine``:

.. nbplot::

    >>> mm_to_vox = npl.inv(img.affine)
    >>> nib.affines.apply_affine(mm_to_vox, [0, 0, 10])
    array([ 45.,  63.,  41.])
