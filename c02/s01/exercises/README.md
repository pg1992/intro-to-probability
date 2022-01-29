Description
===========

Problems 1 and 2
----------------

The program [`01_02.py`](01_02.py) simulates the spinner.

Problem 3
---------

The program [`monte_carlo.py`](monte_carlo.py) finds the proportion of points
that lie in a region and we can estimate the area.  By counting only the numbers
that lie in the circle with radius .5 (i.e., (x-.5)^2 + (y-.5)^2 <= .5^2), we
can estimate pi (approx. 4 * proportion).  Running the simulation with 1,000
points we get values with .05 error.
