"""Buffon's needle

The probability that a needle with unit length crosses one of the lines of a
set of parallel lines equally spaced by one unit is 2 / pi.  Based on that we
can estimate the value o pi by finding the proportion of needles that crosses
a line:

pi ~= 2 / ("number of needles touching a line" / "total of needles")
"""

import numpy as np


if __name__ == "__main__":
    cross = 0
    trials = 100000

    for _ in range(trials):
        # we only need to account for the y coordinate of the extremeties of
        # the needle if we assume that all lines are horizontal
        angle = np.pi * np.random.sample()
        y1 = 10 * np.random.sample()
        y2 = y1 + np.sin(angle)

        # middle of the needle
        mid = (y1 + y2) / 2
        closest_line = np.round(mid)

        # count the crossings
        cross += 1 if (y1 <= closest_line <= y2) else 0

    p = cross / trials
    pi_estimate = 2 / p
    print(f'pi is approx {pi_estimate}.')
