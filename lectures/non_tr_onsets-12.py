tr_times = np.arange(n_trs)
hr_indices = np.round(tr_times * tr_divs).astype(int)
tr_hemo = high_res_hemo[hr_indices]
plt.plot(tr_times, tr_hemo)
# [...]
len(tr_times)
# 173
