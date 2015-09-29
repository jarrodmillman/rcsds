******
Day 10
******

Lesson plan
-----------

We will go over the :doc:`OpenFMRI notes <openfmri_notes>`.

We will then download and extract a dataset in class, and explain the
directory structure and how to read the data.

Next we will do a couple of exercises with some introduction before each.

See :doc:`images_in_4d`:

* BOLD images;
* Revision of nibabel load, ``get_data``;
* Images with three and four dimensions;
* Summary functions work on all dimensions unless you tell them otherwise; use
  ``axis=`` to tell them otherwise;
* Negating booleans with ``~bool_arr``

Then we will do the :doc:`in_4d` exercise.

* Brain cartoons, and the frontal lobe;
* Gray matter, white matter, CSF;
* Block designs and event-related designs;
* Repetition time (TR) is the time between the beginning of acquisition of one
  volume and the beginning of the next;
* ``np.loadtxt`` loads text files into numpy arrays;

See :doc:`reading_text_files`

Now we do the :doc:`first_activation` exercise.

Solutions
---------

* `in 4D solutions
  <https://github.com/jarrodmillman/rcsds/blob/master/lectures/in_4d_solutions.ipynb>`_
* `first activation solutions
  <https://github.com/jarrodmillman/rcsds/blob/master/lectures/first_activation_solutions.ipynb>`_

.. include:: ../links_names.inc
