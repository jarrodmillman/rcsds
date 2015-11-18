X_pca = np.ones((n_trs, 5))
X_pca[:, 0] = convolved
X_pca[:, 1:3] = U[:, :2]
X_pca[:, 3] = linear_drift
plt.imshow(X_pca, aspect=0.1)
# ...
