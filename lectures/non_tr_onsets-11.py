hrf_times = np.arange(0, 24, 1 / tr_divs)
hrf_at_hr = hrf(hrf_times)
high_res_hemo = np.convolve(high_res_neural, hrf_at_hr)[:len(high_res_neural)]
plt.plot(high_res_times, high_res_hemo)
# [...]
len(high_res_times)
# 17300
