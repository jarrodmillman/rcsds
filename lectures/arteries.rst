####################
Finding the arteries
####################

The major arteries in some anatomical MRI images often have high
signal (white when displaying in grayscale).

Our task is to see if we can pick out the courses of the `vertebral,
basilar
<http://en.wikipedia.org/wiki/Vertebral_artery#mediaviewer/File:Vertebral_artery_3D_AP.jpg>`__
and `carotid
<http://en.wikipedia.org/wiki/Internal_carotid_artery#mediaviewer/File:Magnetic_resonance_angiogram_of_segments_of_the_internal_carotid_artery.jpg>`__
arteries on this image.

This time we are going to load an image using the nibabel_ library.
The image is :download:`ds107_sub001_highres.nii`.
If you didn't download this during class, download this
file to your working directory.

Start off by importing ``nibabel``:

.. code:: python

    import nibabel as nib

Try loading the image using nibabel, to make an image object. Use tab
completion on ``nib.`` to work out how to do this.

.. code:: python

    # img = ?

Now get the image array data from the nibabel image object. Don't
forget to use tab completion on the image object if you can remember
or don't know the methods of the object.

.. code:: python

    # data = ?

Try plotting a few slices over the third dimension to see whether you
can see the arteries. For example, to plot the first slice over the
third dimension, you might use:

.. code:: python

    plt.imshow(data[:, :, 0], cmap='gray')

where ``data`` is your image array data.

.. code:: python

    # Plotting some slices over the third dimension

Now try looking for a good threshold so that you pick up only the very
high signal in the brain. A good place to start is to use ``plt.hist``
to get an idea of the spread of values within the volume and within
the slice.

.. code:: python

    # Here you might try plt.hist or something else to find
    # a threshold

Try making a binarized image with your threshold and displaying slices
with that. What structures are you picking up?

.. code:: python

    # Maybe display some slices from the data binarized with a
    # threshold

Now try taking a 3D subvolume out of the middle of the image (the
approximate middle in all three axes) to pick out a good subvolume of
the image that still contains the big arteries.

.. code:: python

    # Create a smaller 3D subvolume from the image data that still
    # contains the arteries

Try binarizing that with some thresholds to see whether you can pick
out the arteries without much other stuff. Hint - you might consider
using ``np.percentile`` or ``plt.hist`` to find a good threshold.

.. code:: python

    # Try a few plots of binarized slices and other stuff to find a good threshold

If you have a good threshold and a good binarized subset, see if you
can see the arterial structure using the fancy function to plot the
binarized image with a 3D rendering.

For this last part, you will need the scikit-image_ Python package.

Install as you did for `nibabel`_ in class.  First try (in IPython) ``import
skimage``.  If that fails, exit IPython, and try ``pip install scikit-image``.
If that works, try ``import skimage`` in IPython again.

.. code:: python

    # This function uses matplotlib 3D plotting and sckit-image for
    # rendering
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    from skimage import measure

    def binarized_surface(binary_array):
        """ Do a 3D plot of the surfaces in a binarized image

        This uses scikit-image and some fancy commands that we don't
        need to worry about at the moment, to do the plot.
        """
        verts, faces = measure.marching_cubes(binary_array, 0)
        fig = plt.figure(figsize=(10, 12))
        ax = fig.add_subplot(111, projection='3d')

        # Fancy indexing: `verts[faces]` to generate a collection of triangles
        mesh = Poly3DCollection(verts[faces], linewidths=0, alpha=0.5)
        ax.add_collection3d(mesh)
        ax.set_xlim(0, binary_array.shape[0])
        ax.set_ylim(0, binary_array.shape[1])
        ax.set_zlim(0, binary_array.shape[2])

For example, let's say you have a binarized subvolume of the original
data called ``binarized_subvolume``. You could do a 3D rendering of
this binary image with::

.. code:: python

    binarized_surface(binarized_subvolume)

.. include:: ../links_names.inc
