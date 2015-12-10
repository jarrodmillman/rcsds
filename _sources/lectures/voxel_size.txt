###################################
What is the voxel size of my image?
###################################

A voxel is an element in the 3D image array.

We can think of the voxel as representing a volume that is a 3D rectangle (rectangular box).

The lengths of the sides of the box in millimeters are the *voxel sizes*. The
voxel sizes will be a length 3 vector.

This page describes how to work out the voxel sizes from the image affine.

To understand this page, you should first read `coordinate systems and affines <http://nipy.org/nibabel/coordinate_systems.html>`_.

The voxel size of an array axis $d$ is the distance in millimeters moved when
moving from the center of one voxel to the next voxel on axis $d$.

For example, I could start at the voxel of coordinate (array index) $(0, 0,
0)$.  The voxel size for the first axis ($v_1$) is the distance in millimeters
moved when moving from $(0, 0, 0)$ to $(1, 0, 0)$.

Remember that the *affine* gives the millimeter coordinate corresponding to any
given voxel (array) coordinate.

The image affine $A$ can be written as:

.. math::

    A =
    \begin{bmatrix}
    m_{11} & m_{12} & m_{13} & a \\
    m_{21} & m_{22} & m_{23} & b \\
    m_{31} & m_{32} & m_{33} & c \\
    0 & 0 & 0 & 1 \\
    \end{bmatrix}

If I apply the image affine to the voxel coordinate $(0, 0, 0)$ I get:

.. math::

    \begin{bmatrix}
    x\\
    y\\
    z\\
    1\\
    \end{bmatrix} =
    \begin{bmatrix}
    m_{11} & m_{12} & m_{13} & a \\
    m_{21} & m_{22} & m_{23} & b \\
    m_{31} & m_{32} & m_{33} & c \\
    0 & 0 & 0 & 1 \\
    \end{bmatrix}
    \begin{bmatrix}
    0\\
    0\\
    0\\
    1\\
    \end{bmatrix}

Thus:

.. math::

    x = a \\
    y = b \\
    z = c

Applying the image affine to voxel coordinate $(1, 0, 0)$ I get:


.. math::

    \begin{bmatrix}
    x'\\
    y'\\
    z'\\
    1\\
    \end{bmatrix} =
    \begin{bmatrix}
    m_{11} & m_{12} & m_{13} & a \\
    m_{21} & m_{22} & m_{23} & b \\
    m_{31} & m_{32} & m_{33} & c \\
    0 & 0 & 0 & 1 \\
    \end{bmatrix}
    \begin{bmatrix}
    1\\
    0\\
    0\\
    1\\
    \end{bmatrix}

So:

.. math::

    x' = m_{11} + a \\
    y' = m_{21} + b \\
    z' = m_{31} + c

The difference vector moving from $(0, 0, 0)$ to $(1, 0, 0)$ is therefore:

.. math::

    \begin{bmatrix}
    d_x\\
    d_y\\
    d_z\\
    \end{bmatrix} =
    \begin{bmatrix}
    x'\\
    y'\\
    z'\\
    \end{bmatrix} -
    \begin{bmatrix}
    x\\
    y\\
    z\\
    \end{bmatrix} =
    \begin{bmatrix}
    m_{11}\\
    m_{21}\\
    m_{31}
    \end{bmatrix}

The Euclidean length of this difference vector is the voxel size for the first
image axis:

.. math::

    v_1 = \sqrt{m_{11}^2 + m_{21}^2 + m_{31}^2}

By following the same logic, moving from $(0, 0, 0)$ to $(0, 1, 0)$ or $(0, 0,
1)$, you can show that the voxel sizes for the second and third axes are the
Euclidean lengths of the second and third columns of the image affine:

.. math::

    v_2 = \sqrt{m_{12}^2 + m_{22}^2 + m_{32}^2} \\
    v_3 = \sqrt{m_{13}^2 + m_{23}^2 + m_{33}^2}
