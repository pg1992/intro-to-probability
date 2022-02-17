import numpy as np
from scipy.special import comb


p = .5
pt = .7

for n in [10, 30, 50]:
    n70 = pt * n
    k = np.arange(n + 1)
    b = comb(n, k) * p**k * (1 - p)**(n - k)
    p70 = np.round(np.sum(b[k >= n70]), 3)
    print(f'Probability of getting {int(pt*100):d}% or more in '
          f'a test with {n} questions just by guessing: {p70}.')
