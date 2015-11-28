# set regions outside mask as missing with np.nan
mean_data[~mask] = np.nan
beta_vols[~mask] = np.nan
