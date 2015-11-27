data = img.get_data()[..., 4:]
vol_shape, n_trs = data.shape[:-1], data.shape[-1]
