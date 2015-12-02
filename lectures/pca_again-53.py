# Finding principal components using SVD on X X^T
unscaled_cov = X.dot(X.T)
U_again, S_again, VT_again = npl.svd(unscaled_cov)
U_again
# array([[-0.87829753, -0.47811447],
# [-0.47811447,  0.87829753]])
