"""Problem 1

Show that the proportion of points (area of a bar) that falls in a given
interval divided by the length of the interval, i.e. the height of the bar,
is approximately constant.
"""

import numpy as np
from matplotlib import pyplot as plt


def spinner_distribution(lengths, num_experiments: int = 1000):
    """Generate the bar graph data"""

    assert np.abs(np.sum(lengths) - 1) <= 1e-6

    sizes = lengths.cumsum()
    areas = np.zeros(sizes.shape)
    samples = np.random.sample((num_experiments, 1))

    possibilities = np.repeat(samples, lengths.shape, axis=1)
    sums = np.sum(possibilities > sizes, axis=1)

    for i in range(len(areas)):
        areas[i] = (sums == i).sum() / num_experiments

    x = np.zeros(sizes.size)
    x[1:] = sizes[:-1]
    heights = areas / lengths

    return x, heights, lengths


if __name__ == "__main__":
    p1_params = {
        'lengths': 1 / np.array([2, 3, 6]),
        'num_experiments': 100000,
    }

    x, heights, lengths = spinner_distribution(**p1_params)

    fig, ax = plt.subplots()
    ax.bar(x, height=heights, width=lengths, align='edge', edgecolor='k')
    ax.set_title('Problem 1: area = proportion')

    fig.savefig('01.png')
