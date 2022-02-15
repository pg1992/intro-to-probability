"""Probability of number coin throws

Given n throws of a coin, what is the probability that the number of heads
lies between some interval.
"""

import numpy as np
from scipy.special import comb

n = 100
p = .5
k = np.arange(n + 1)
b = comb(n, k) * p**k * (1 - p)**(n - k)

limits = [
    (35, 65),
    (40, 60),
    (45, 55),
]

for lmin, lmax in limits:
    rng = (lmin <= k) & (k <= lmax)
    prob = np.round(np.sum(b[rng]), 3)
    print(f'P({lmin} <= n <= {lmax}) = {prob}')
