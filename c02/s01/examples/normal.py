"""Construct a normal distribution by summation

If we sum a great number of random variables drawn from a uniform distribution
we end up with a normal distribution.
"""

import numpy as np
from matplotlib import pyplot as plt


if __name__ == "__main__":
    experiments = 100000
    summands = 50
    samples = np.random.sample((experiments, summands))

    n_bins = 50
    sums = samples.sum(axis=1)
    plt.hist(sums, bins=n_bins)
    plt.show()
