import numpy as np
from .source import Source


def empty_sky():
    """
    Returns an empty source so that instrumental fluxes can be simulated

    Returns
    -------
    sky : Source

    """
    sky = Source(lam=np.array([0.3, 3.0]), spectra=np.array([0, 0]),
                 x=[0], y=[0], ref=[0], weight=[0])
    return sky