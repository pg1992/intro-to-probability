import numpy as np
from scipy.special import comb
from matplotlib import pyplot as plt


def alpha(n, p, m):
    k = np.arange(m, n + 1)
    d = comb(n, k) * p**k * (1 - p)**(n - k)

    return np.sum(d)


def binomial(n, p):
    """Binomial probability distribution

    Returns a tuple with the number of seccesses and the probability
    of each Bernoulli trial, with n trials and probability of success p.
    """

    k = np.arange(n + 1)

    return k, comb(n, k) * p**k * (1 - p)**(n - k)


if __name__ == "__main__":
    n = 100

    p_null = .6
    k, b_null = binomial(n, p_null)

    p_alternate = .8
    k, b_alternate = binomial(n, p_alternate)

    plt.stem(k, b_null, linefmt='b', markerfmt='ob', label=f'Null hypothesis (n = {n}; p = {p_null})')
    plt.stem(k, b_alternate, linefmt='k', markerfmt='ok', label=f'Alternate hypothesis (n = {n}; p = {p_alternate})')

    plt.legend()
    plt.show()
