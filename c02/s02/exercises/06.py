import numpy as np
from scipy.special import comb


p_guess = .5
p_knows = .75

trials = 10
m = 7

k = np.arange(trials + 1)
b_guess = comb(trials, k) * p_guess**k * (1 - p_guess)**(trials - k)
b_knows = comb(trials, k) * p_knows**k * (1 - p_knows)**(trials - k)

p_wins_knows = np.round(np.sum(b_knows[k >= m]), 3)
p_loses_guess = np.round(1 - np.sum(b_guess[k >= m]), 3)

print(f'Probability that Charles wins if he has the ability that he claims: {p_wins_knows}.')
print(f'Probability that Ruth wins if Charles is guessing: {p_loses_guess}.')
