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

.. nbplot::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> import nibabel as nib


.. nbplot::

    >>> img = nib.load('ds114_sub009_t2r1.nii')
    >>> n_trs = img.shape[-1]
    >>> TR = 2.5

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

.. nbplot::

    >>> onsets_in_scans = cond_data[:, 0] / TR
    >>> onsets_in_scans
    array([   1.34 ,    5.104,   17.308,   30.1  ,   38.192,   67.136,
            112.944,  121.904,  142.528,  148.888])

.. nbplot::

    >>> tr_divs = 100.0
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

    >>> plt.plot(high_res_times[:2000], high_res_hemo[:2000])
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
