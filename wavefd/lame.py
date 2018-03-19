"""
Calculate Lamé's first and second parameter.
"""


def lame_lambda(pvel, svel, density):
    r"""
    Calculate Lamé's first parameter :math:`\lambda`.

    Defined in terms of the P and S wave velocities
    (:math:`v_P` and :math:`v_S`) and the density (:math:`\rho`).

    .. math::

        \lambda = v_P^2 \rho - 2v_S^2 \rho

    Units must be consistent. For example, if *pvel* and *svel* are in m/s, the
    density must be kg/m³ (or g/m³, etc).

    Parameters:

    * pvel : float or array
        The P wave velocity
    * svel : float or array
        The S wave velocity
    * density : float or array
        The density

    Returns:

    * lambda : float or array
        The Lamé parameter

    Examples::

        >>> print(lame_lambda(pvel=2350, svel=1125, density=2500))
        7478125000
        >>> import numpy as np
        >>> pvel = np.array([2000., 3000.])
        >>> svel = np.array([1000., 1700.])
        >>> density = np.array([2700., 3100.])
        >>> lamb = lame_lambda(pvel, svel, density)
        >>> print(' '.join(['{:.0f}'.format(i) for i in lamb]))
        5400000000 9982000000

    """
    return density*pvel**2 - 2*density*svel**2


def lame_mu(svel, density):
    r"""
    Calculate Lamé's second parameter :math:`\mu` (the shear modulus).

    Defined in terms of the S wave velocity (:math:`v_S`) and the density
    (:math:`\rho`).

    .. math::

        \mu = v_S^2 \rho

    Units must be consistent. For example, if *svel* is in m/s, the density
    must be kg/m³ (or g/m³, etc).

    Parameters:

    * svel : float or array
        The S wave velocity
    * density : float or array
        The density

    Returns:

    * mu : float or array
        The Lamé parameter

    Examples::

        >>> print(lame_mu(svel=1125, density=2500))
        3164062500
        >>> import numpy as np
        >>> svel = np.array([1000., 1700.])
        >>> density = np.array([2700., 3100.])
        >>> mu = lame_mu(svel, density)
        >>> print(' '.join(['{:.0f}'.format(i) for i in mu]))
        2700000000 8959000000

    """
    return density*svel**2
