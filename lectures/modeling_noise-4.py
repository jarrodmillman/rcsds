img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
data = data[..., 4:]
vol_shape = data.shape[:-1]
n_trs = data.shape[-1]
vol_shape, n_trs
# ((64, 64, 30), 169)
