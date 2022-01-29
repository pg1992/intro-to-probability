"""Bertrand's Paradox

What is the probability that a chord chosen at random inside a unit circle is
greater than sqrt(3)?  Well... It depends.
"""

import numpy as np
from numpy import linalg as LA


def midpoint_rectangular(num_points: int = 10000) -> float:
    """Choose the rectangular coordinates at random"""

    samples = 2 * np.random.sample((num_points, 2)) - 1
    distances = LA.norm(x=samples, axis=1)

    inside_unit_circle = (distances < 1).sum()
    inside_center_circle = (distances < .5).sum()

    return inside_center_circle / inside_unit_circle


def midpoint_polar(num_points: int = 10000) -> float:
    """Choose midpoint distance from center at random"""

    distances = 2 * np.random.sample(num_points) - 1

    less_than_half = (np.abs(distances) < .5).sum()

    return less_than_half / num_points


def endpoint_angle(num_points: int = 10000) -> float:
    """Choose chord endpoint angle at random"""

    low = 2 * np.pi / 3
    high = 4 * np.pi / 3

    angles = 2 * np.pi * np.random.sample(num_points)

    inside_arc = np.sum((angles > low) & (angles < high))

    return inside_arc / num_points


if __name__ == "__main__":
    print(f"Method 1 - {midpoint_rectangular()}.")
    print(f"Method 2 - {midpoint_polar()}.")
    print(f"Method 3 - {endpoint_angle()}.")
