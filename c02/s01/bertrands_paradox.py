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


if __name__ == "__main__":
    print(f"Method 1 - {midpoint_rectangular()}.")
