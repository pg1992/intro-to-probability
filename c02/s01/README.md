Descriptions
============

`buffon.py`
-----------

Estimate the value of pi using Buffon's method.

`normal.py`
-----------

This program shows that if we sum a lot of random variables drawn from a uniform
distribution we end up with a normal distribution.

`bertrands_paradox.py`
----------------------

This program shows that the probability of an event happening depends on how
you define the model.

A random chord is chosen at random in a unit circle.  What is the probability
that this chord has length greater than the square root of 3?  It all depends
on how you define random.

If we choose the coordinates of the chord midpoint at random, then it amounts
to choosing the coordinates (x, y) at random.  In this case the probability
becomes 0.25.

If we choose the distance of the midpoint from the center at random, then
the probability becomes 0.5.

If we fix one of the ends of the chord and choose the arc length of the second
end at random, then the probability is 0.333.

This is Bertrand's Paradox!

(E. T. Jeynes showed that the second method is the correct one because it has
some nice properties, like translation invariance.)
