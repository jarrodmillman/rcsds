remaining_ss = []
for u in u_vectors.T: # iterate over columns
    remaining = line_remaining(u, X)
    remaining_ss.append((remaining ** 2).sum())
