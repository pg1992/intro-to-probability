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


def problem_3():
    num_points = 1000

    def circle_criteria(x, y):
        """Circle with radius .5 and center [.5, .5]."""

        return (x - .5)**2 + (y - .5)**2 <= .5**2

    proportion = monte_carlo(circle_criteria, num_points)
    pi_estimate = 4 * proportion
    error = np.abs(np.pi - pi_estimate)

    print(f"P3: proportion = {proportion}; pi_estimate = {pi_estimate}; "
          f"error = {error:.2f}.")


def problem_4():
    num_points = 10000

    def sine_criteria(x, y):
        """Half of a sine wave."""

        return y <= np.sin(np.pi * x)

    proportion = monte_carlo(sine_criteria, num_points)
    pi_estimate = 2 / proportion
    error = np.abs(np.pi - pi_estimate)

    print(f"P4: proportion = {proportion}; pi_estimate = {pi_estimate}; "
          f"error = {error:.2f}.")


def problem_5():
    num_points = 10000

    def reciprocal_criteria(x, y):
        """Reciprocal function."""

        return y <= 1 / (x + 1)

    proportion = monte_carlo(reciprocal_criteria, num_points)
    error = np.abs(np.log(2) - proportion)

    print(f"P5: proportion = {proportion}; error = {error:.2f}.")


if __name__ == "__main__":
    problem_3()
    problem_4()
    problem_5()
