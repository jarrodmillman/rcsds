high_res_neural = np.zeros(high_res_times.shape)
for hr_onset, hr_duration, amplitude in zip(high_res_onsets, high_res_durations, cond_data[:, 2]):
    hr_onset = int(round(hr_onset))
    hr_duration = int(round(hr_duration))
    high_res_neural[hr_onset:hr_onset + hr_duration] = amplitude
