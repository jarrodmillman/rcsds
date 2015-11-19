tr_divs = 100.0
high_res_times = np.arange(0, n_trs, 1 / tr_divs)
high_res_onsets = onsets_in_scans * tr_divs
high_res_onsets
# array([   134. ,    510.4,   1730.8,   3010. ,   3819.2,   6713.6,
# 11294.4,  12190.4,  14252.8,  14888.8])
