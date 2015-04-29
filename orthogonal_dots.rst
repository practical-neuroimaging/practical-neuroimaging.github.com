#########################################
The dot product of two unit vectors in 2D
#########################################

The dot product of two unit vectors $\hat{a}, \hat{b}$ is $\cos \theta$, where
$\theta$ is the angle between the unit vectors.

*****
Proof
*****

We remember the rotation formula from :doc:`rotation_2d`:

.. math::

    x_2 = \cos \beta x_1 - \sin \beta y_1 \\
    y_2 = \sin \beta x_1 + \cos \beta y_1

Now consider the unit vector $\hat{a} = (x_1, y_1)$ rotated by $\theta$ to get
$\hat{b} = (x_2, y_2)$:

.. math::

    \hat{a} \cdot \hat{b} = x_1 x_2 + y_1 y_2 \\
    = x_1 (\cos \theta x_1 - \sin \theta y_1) + y_1 (\sin \theta x_1 + \cos
      \theta y_1) \\
    = \cos \theta x_1^2 - \sin \theta x_1 y_1 + \sin \theta x_1 y_1 + \cos
      \theta y_1^2 \\
    = \cos \theta (x_1^2 + y_1^2)

Because we have assumed $\hat{a}$ is a unit vector, :math:`\| \hat{a} |\ = x_1^2 + y_1^2 = 1` and:

.. math::

    \hat{a} \cdot \hat{b} = \cos \theta

*******************************
Dot product of not-unit vectors
*******************************

Now take two non-unit vectors $\vec{x}, \vec{y}$:

.. math::

    \hat{x} = \frac{1}{\| \vec{x} \|}\vec{x} \\
    \hat{y} = \frac{1}{\| \vec{x} \|}\vec{x}

From the rules of the dot product and the result from the unit vectors above:

.. math::

    \vec{x} \cdot \vec{y} = \| \vec{x} \| \| \vec{y} \| \cos \theta
