Description
===========

Problems 1 and 2
----------------

The program [`01_02.py`](01_02.py) simulates the spinner.

Problems 3 and 4
----------------

The program [`monte_carlo.py`](monte_carlo.py) finds the proportion of points
that lie in a region and we can estimate the area.  By counting only the numbers
that lie in the circle with radius .5 (i.e., (x-.5)^2 + (y-.5)^2 <= .5^2), we
can estimate pi (approx. 4 * proportion).  Running the simulation with 1,000
points we get values with .05 error.

In problem 4 the exact probability would be the area under half of a sine wave
with 0.5 Hz frequency, which is 2 divided by pi.  We could estimate pi
by finding the proportion _p_, i.e. 2 / _p_.  The error we get is about 0.01,
which is a bit more accurate.