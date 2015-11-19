convolved = np.loadtxt('ds114_sub009_t2r1_conv.txt')[4:]
X = np.ones((n_trs, 4))
X[:, 0] = convolved
linear_drift = np.linspace(-1, 1, n_trs)
X[:, 1] = linear_drift
quadratic_drift = linear_drift ** 2
quadratic_drift -= np.mean(quadratic_drift)
X[:, 2] = quadratic_drift
plt.imshow(X, aspect=0.1)
# <...>
