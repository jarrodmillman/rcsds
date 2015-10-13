# Compile the design matrix
# First column is convolved regressor
# Second column all ones
design = np.ones((len(convolved), 2))
design[:, 0] = convolved
plt.imshow(design, aspect=0.1, interpolation='nearest', cmap='gray')
# <...>
