b_vols = np.zeros(vol_shape + (4,))
b_vols[in_brain_mask, :] = B.T
