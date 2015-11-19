vox_to_mm = img.affine
nib.affines.apply_affine(vox_to_mm, [2, 3, 4])
# array([  86., -120.,  -64.])
