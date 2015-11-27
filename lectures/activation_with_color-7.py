from scipy.ndimage import gaussian_filter
beta_conv = beta_vols[..., 0]
beta_conv = gaussian_filter(beta_conv, 2)  # smooth by 2 voxel SD
