betas = npl.pinv(X).dot(Y)
beta_vols = np.zeros(vol_shape + (P,))
beta_vols[mask] = betas.T
