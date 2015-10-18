scaled_U, scaled_S, scaled_V = npl.svd(np.cov(X))
np.allclose(scaled_V, V)
# True
