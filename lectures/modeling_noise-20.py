projection_vols = np.zeros(data.shape)
projection_vols[in_brain_mask, :] = projections.T
