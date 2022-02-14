"""Hypothesis testing

What is the value which will make us reject the null hypothesis?
"""

import numpy as np
from scipy.special import comb
from matplotlib import pyplot as plt


def alpha(n, p, m):
    """Probability of successes greater than 'm'."""

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
    error_threshold = .01
    n = 200

    p_null = .6
    k_null, b_null = binomial(n, p_null)

    p_alternate = .8
    k_alternate, b_alternate = binomial(n, p_alternate)

    fig, axd = plt.subplot_mosaic([['ul', 'r'],
                                   ['dl', 'r']])

    axd['ul'].stem(
        k_null,
        b_null,
        linefmt='b',
        markerfmt='ob',
        basefmt=' ',
        label=f'Null hypothesis (n = {n}; p = {p_null})',
    )

    axd['ul'].stem(
        k_alternate,
        b_alternate,
        linefmt='k',
        markerfmt='ok',
        basefmt=' ',
        label=f'Alternate hypothesis (n = {n}; p = {p_alternate})',
    )

    axd['ul'].legend()
    axd['ul'].axis([0, n, 0, .2])
    axd['ul'].set_title(f'Distributions (n = {n})')
    axd['ul'].set_xticks(n * np.array([0, p_null, p_alternate, 1]))
    axd['ul'].set_yticks([0, np.max(b_null), np.max(b_alternate)])
    axd['ul'].set_xlabel('Number of successes')
    axd['ul'].set_ylabel('Probability')
    axd['ul'].grid()

    alpha_null = np.array([alpha(n, p_null, m) for m in k_null])

    axd['dl'].stem(
        k_null,
        alpha_null,
        linefmt='b',
        markerfmt='ob',
        basefmt=' ',
        label=r'Type 1 error probability: $\alpha(p_{null})$',
    )

    alpha_alternate = np.array([alpha(n, p_alternate, m) for m in k_alternate])

    axd['dl'].stem(
        k_alternate,
        1 - alpha_alternate,
        linefmt='k',
        markerfmt='ok',
        basefmt=' ',
        label=r'Type 2 error probability: $1 - \alpha(p_{alternate})$',
    )

    axd['dl'].plot(
        [0, n],
        error_threshold * np.ones(2),
        'r--',
        label='5% threshold'
    )

    axd['dl'].set_title('Error probability')
    axd['ul'].set_xticks(n * np.array([0, p_null, p_alternate, 1]))
    axd['dl'].set_yticks([error_threshold, 1 - error_threshold])
    axd['dl'].set_xlabel('Critical value (m)')
    axd['dl'].set_ylabel(r'$\alpha(p) = \sum_{m \leq k \leq n} b(n, p, k)$')
    axd['dl'].legend()
    axd['dl'].grid()

    type_1 = alpha_null < error_threshold
    type_2 = (1 - alpha_alternate) < error_threshold

    valid = type_1 & type_2
    k_null_valid = k_null[valid]
    alpha_null_valid = alpha_null[valid]
    k_alternate_valid = k_alternate[valid]
    alpha_alternate_valid = alpha_alternate[valid]

    axd['r'].stem(
        k_null_valid,
        alpha_null_valid,
        linefmt='b',
        markerfmt='ob',
        basefmt=' ',
        label=r'Type 1 error probability: $\alpha(p_{null})$',
    )

    axd['r'].stem(
        k_alternate_valid,
        1 - alpha_alternate_valid,
        linefmt='k',
        markerfmt='ok',
        basefmt=' ',
        label=r'Type 2 error probability: $1 - \alpha(p_{alternate})$',
    )

    axd['r'].plot(
        [0, n],
        error_threshold * np.ones(2),
        'r--',
        label='5% threshold'
    )

    axd['r'].axis([np.min(k_null_valid) - 1, np.max(k_null_valid) + 1, 0, .1])
    axd['r'].set_title('Type 1 and 2 errors (valid critical values)\n'
                       f'error threshold = {error_threshold}')
    axd['r'].set_xticks(k_null_valid)
    axd['r'].set_yticks([0, error_threshold])
    axd['r'].set_xlabel('Critical value (m)')
    axd['r'].set_ylabel(r'$\alpha(p)$')

    plt.show()
