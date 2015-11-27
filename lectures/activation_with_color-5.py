Y = data[mask].T
P = 3  # number of parameters == columns in model
X = np.ones((n_trs, P))
X[:, 0] = np.loadtxt('ds114_sub009_t2r1_conv.txt')[4:]
X[:, 1] = np.linspace(-1, 1, n_trs)
