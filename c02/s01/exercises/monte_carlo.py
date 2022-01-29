"""Monte Carlo

Estimate areas by running a Monte Carlo simulation inside the unit square
with different criterias.
"""

import numpy as np


def monte_carlo(criteria, num_points) -> float:
    """Area estimation by Monte Carlo

    Generate `num_points` points and see if they satisfy `criteria`.
    Returns the proportion of points that satisfy the criteria.

    All points must lie in the unit square with corners [0, 0], [0, 1], [1, 0],
    and [1, 1].
    """

    samples = np.random.sample((num_points, 2))
    in_area = np.sum(criteria(samples[:, 0], samples[:, 1]))

    return in_area / num_points


if __name__ == "__main__":
    num_points = 1000

    def circle_criteria(x, y):
        """Circle with radius .5 and center [.5, .5]."""

        return (x - .5)**2 + (y - .5)**2 <= .5**2

    proportion = monte_carlo(circle_criteria, num_points)
    pi_estimate = 4 * proportion
    error = np.abs(np.pi - pi_estimate)

    print(f"P3: proportion = {proportion}; pi_estimate = {pi_estimate}; "
          f"error = {error:.2f}.")
