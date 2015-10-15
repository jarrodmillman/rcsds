y = voxel_time_course
y_hat = X.dot(beta_hat)
residuals = y - y_hat
# Residual sum of squares
RSS = np.sum(residuals ** 2)
# Degrees of freedom
df = X.shape[0] - npl.matrix_rank(X)
# Mean residual sum of squares
MRSS = RSS / df
# This is our s^2
s2 = MRSS
print(s2)
# 247.937561534
print(np.sqrt(s2))
# 15.7460332
