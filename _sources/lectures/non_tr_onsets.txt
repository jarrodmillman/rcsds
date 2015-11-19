######################################
Using onsets that do not start on a TR
######################################

You'll need the file :download:`new_cond.txt` to type along with this
demonstration.

.. testcode::

    import os
    os.chdir('lectures')

.. nbplot::

    >>> from __future__ import division
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> import nibabel as nib

Imagine we are analyzing our :download:`example image <ds114_sub009_t2r1.nii>`.  It has a TR of
2.5, and 173 TRs.

.. nbplot::

    >>> TR = 2.5
    >>> n_trs = 173

The actual condition file for this dataset is
:download:`ds114_sub009_t2r1_cond.txt`. You may remember it has a *block
design* with blocks of length 12 TRs while the subject is doing the task.

What if we had a different *event related* condition file like this:

.. nbplot::

    >>> cond_data = np.loadtxt('new_cond.txt')
    >>> cond_data
    array([[   3.35,    3.  ,    2.  ],
           [  12.76,    3.  ,    2.  ],
           [  43.27,    3.  ,    2.  ],
           [  75.25,    3.  ,    1.  ],
           [  95.48,    3.  ,    2.  ],
           [ 167.84,    3.  ,    2.  ],
           [ 282.36,    3.  ,    2.  ],
           [ 304.76,    3.  ,    2.  ],
           [ 356.32,    3.  ,    2.  ],
           [ 372.22,    3.  ,    3.  ]])

Notice that the onsets of the events can happen in the middle of the volumes
(well after the volumes have started).

.. nbplot::

    >>> onsets_in_scans = cond_data[:, 0] / TR
    >>> onsets_in_scans
    array([   1.34 ,    5.104,   17.308,   30.1  ,   38.192,   67.136,
            112.944,  121.904,  142.528,  148.888])

Notice also that the events have *amplitudes* between 1 and 3.  The events of
amplitude 3 we expect to have an evoked brain response three times higher than
events with amplitude 1.

What to do about the events with onsets that don't exactly align with the
start of the TRs (volumes)?

One option would be to round the event onsets to the nearest TR.  This will
mean that the event model will be different from our expected response by TR
seconds / 2 == 1.25 seconds in this case.

Can we do better than that?

One option is to make a neural and hemodynamic regressor at a finer time
resolution than the TRs, and later sample this regressor at the TR onset
times.

This is what we do next.

.. nbplot::

    >>> tr_divs = 100.0  # finer resolution has 100 steps per TR
    >>> high_res_times = np.arange(0, n_trs, 1 / tr_divs)
    >>> high_res_onsets = onsets_in_scans * tr_divs
    >>> high_res_onsets
    array([   134. ,    510.4,   1730.8,   3010. ,   3819.2,   6713.6,
            11294.4,  12190.4,  14252.8,  14888.8])

.. nbplot::

    >>> high_res_durations = cond_data[:, 1] / TR * tr_divs
    >>> high_res_durations
    array([ 120.,  120.,  120.,  120.,  120.,  120.,  120.,  120.,  120.,  120.])

.. nbplot::

    >>> high_res_neural = np.zeros(high_res_times.shape)
    >>> for hr_onset, hr_duration, amplitude in zip(high_res_onsets, high_res_durations, cond_data[:, 2]):
    ...     hr_onset = int(round(hr_onset))
    ...     hr_duration = int(round(hr_duration))
    ...     high_res_neural[hr_onset:hr_onset + hr_duration] = amplitude

.. nbplot::

    >>> plt.plot(high_res_times, high_res_neural)
    [...]

.. nbplot::

    >>> from scipy.stats import gamma
    >>>
    >>> def hrf(times):
    ...     """ Return values for HRF at given times """
    ...     # Gamma pdf for the peak
    ...     peak_values = gamma.pdf(times, 6)
    ...     # Gamma pdf for the undershoot
    ...     undershoot_values = gamma.pdf(times, 12)
    ...     # Combine them
    ...     values = peak_values - 0.35 * undershoot_values
    ...     # Scale max to 0.6
    ...     return values / np.max(values) * 0.6

.. nbplot::

    >>> hrf_times = np.arange(0, 24, 1 / tr_divs)
    >>> hrf_at_hr = hrf(hrf_times)
    >>> high_res_hemo = np.convolve(high_res_neural, hrf_at_hr)[:len(high_res_neural)]
    >>> plt.plot(high_res_times, high_res_hemo)
    [...]
    >>> len(high_res_times)
    17300

.. nbplot::

    >>> plt.plot(high_res_times[:20 * tr_divs], high_res_hemo[:20 * tr_divs])
    [...]

.. nbplot::

    >>> tr_times = np.arange(n_trs)
    >>> hr_indices = np.round(tr_times * tr_divs).astype(int)
    >>> tr_hemo = high_res_hemo[hr_indices]
    >>> plt.plot(tr_times, tr_hemo)
    [...]
    >>> len(tr_times)
    173

.. nbplot::

    >>> plt.plot(tr_times[:20], tr_hemo[:20])
    [...]

.. testcleanup::

    os.chdir('..')
