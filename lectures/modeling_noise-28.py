b_pca_vols = np.zeros(vol_shape + (5,))
b_pca_vols[in_brain_mask, :] = B_pca.T
