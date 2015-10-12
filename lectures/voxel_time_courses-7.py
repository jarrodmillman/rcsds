# Plot the neural prediction against the data
neural = neural[1:]
# Notice the + to specify the "line marker"
plt.plot(neural, voxel_time_course, 'o')
# [...]
