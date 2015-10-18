import numpy.linalg as npl
# Finding principal components using SVD
unscaled_cov = X.dot(X.T)
U, S, V = npl.svd(unscaled_cov)
