from scipy.ndimage import gaussian_filter
# Smooth by 2 voxel SD in all three spatial dimensions
smooth_data = gaussian_filter(data, [2, 2, 2, 0])
