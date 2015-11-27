from matplotlib import colors
nice_cmap_values = np.loadtxt('actc.txt')
nice_cmap = colors.ListedColormap(nice_cmap_values, 'actc')
