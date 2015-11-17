Y = in_brain_tcs.T
B = npl.pinv(X).dot(Y)
B.shape
# (4, 21353)
