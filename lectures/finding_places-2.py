# Simulate an image for the output below
class FakeImage(object): pass
img = FakeImage()
img.shape = (91, 109, 91, 240)
img.affine = np.array([[  -2.,    0.,    0.,   90.],
                       [   0.,    2.,    0., -126.],
                       [   0.,    0.,    2.,  -72.],
                       [   0.,    0.,    0.,    1.]])
