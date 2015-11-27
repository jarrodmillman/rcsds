# set regions outside mask as missing with np.nan
mean_data[~mask] = np.nan
beta_conv[~mask] = np.nan
