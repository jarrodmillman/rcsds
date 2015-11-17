Y_demeaned = Y - np.mean(Y, axis=1).reshape([-1, 1])
unscaled_cov = Y_demeaned.dot(Y_demeaned.T)
U, S, V = npl.svd(unscaled_cov)
