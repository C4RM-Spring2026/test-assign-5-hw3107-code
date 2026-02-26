import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1)
    df = 1 / ((1 + r) ** t)

    cf = np.full(n, c)
    cf[-1] = c + face

    price = np.sum(cf * df)
    return(price)
