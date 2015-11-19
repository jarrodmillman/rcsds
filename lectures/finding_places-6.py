mm_to_vox = npl.inv(img.affine)
nib.affines.apply_affine(mm_to_vox, [0, 0, 10])
# array([ 45.,  63.,  41.])
