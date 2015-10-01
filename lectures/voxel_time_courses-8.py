# Correlate the neural time course with the voxel time course
np.corrcoef(neural, voxel_time_course)
# array([[ 1.     ,  0.54285],
# [ 0.54285,  1.     ]])
