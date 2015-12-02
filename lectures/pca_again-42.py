# Show v1 as sum of projections onto components 1 and 2
x, y = v1
# Projections onto first and second component
p1_x, p1_y = projected_1[:, 0]
p2_x, p2_y = projected_2[:, 0]
# Make subplots for vectors and text
fig, (vec_ax, txt_ax) = plt.subplots(1, 2, figsize=(14, 4))
# Show 0, 0
vec_ax.plot(0, 0, 'ro')
# Show vectors with arrows
vec_ax.arrow(0, 0, p1_x, p1_y, color='r', length_includes_head=True, width=0.01)
vec_ax.arrow(0, 0, x, y, color='k', length_includes_head=True, width=0.01)
vec_ax.arrow(p1_x, p1_y, p2_x, p2_y, color='b', length_includes_head=True, width=0.01)
# Label origin
vec_ax.annotate('$(0, 0)$', (-0.5, -0.5), fontsize=16)
# Label vectors
vec_ax.annotate(r'$\vec{{v_1}} = ({x:.2f}, {y:.2f})$'.format(x=x, y=y),
                (x / 2 - 2.2, y / 2 + 0.4), fontsize=16)
vec_ax.annotate(r'$proj_1\vec{{v_1}} = ({x:.2f}, {y:.2f})$'.format(x=p1_x, y=p1_y),
                (p1_x / 2 + 0.5, p1_y / 2), fontsize=16)
vec_ax.annotate(r'$proj_2\vec{{v_1}} = ({x:.2f}, {y:.2f})$'.format(x=p2_x, y=p2_y),
                (x + 0.3, y - 0.1), fontsize=16)
# Make sure axes are right lengths
vec_ax.axis((-1, 7.5, -1, 3))
vec_ax.set_aspect('equal', adjustable='box')
vec_ax.set_title(r'first and and second principal components of $\vec{v_1}$')
# Text about length
txt_ax.axis('off')
txt_ax.annotate(
    r'$\|\vec{v_1}\|^2 = \|proj_1\vec{v_1}\|^2 + \|proj_2\vec{v_1}\|^2$ =' +
    '\n' +
    '${p1_x:.2f}^2 + {p1_y:.2f}^2 + {p2_x:.2f}^2 + {p2_y:.2f}^2$'.format(
    p1_x=p1_x, p1_y=p1_y, p2_x=p2_x, p2_y=p2_y),
    (0, 0.5), fontsize=16)
# ...