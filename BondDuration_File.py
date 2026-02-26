import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1)
    df = 1 / ((1 + r) ** t)

    cf = np.full(n, c, dtype=float)
    cf[-1] = cf[-1] + face

    pv = cf * df
    price = np.sum(pv)

    weighted = np.sum(t * pv)
    duration_periods = weighted / price
    x = duration_periods / ppy

    return(x)
