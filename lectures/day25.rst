******
Day 25
******

Announcements
-------------

Preprocessed data for each project now up at https://nipy.bic.berkeley.edu/rcsds

There are ``.tar`` archives, and unpacked archives so you can fetch images for
any give subject or run.

These kindly provided by Russ Poldrack and the folks at the OpenFMRI project.

The processing applied to the scans is:

* motion correction (coregistration in time to partially correct for movement
  during the run and between runs);
* high-pass filtering in time (to remove low frequency drifts / noise);
* registration to a standard anatomical template (the MNI template).

Using these images, you can estimate the location of a given voxel coordinate
in a standard brain millimeter space, using the image ``affine``:
:doc:`finding_places`.

Notes
-----

* :doc:`non_tr_onsets`
