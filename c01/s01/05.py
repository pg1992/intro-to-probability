import numpy as np


def proportion(trials, throws, dice=3) -> float:
    sim = np.random.choice(6, (trials, throws, dice)) + 1

    return (sim == 6).all(axis=2).any(axis=1).sum() / trials


if __name__ == "__main__":
    # Increase the number of throws until the probability of failure passe 0.5
    p = 1/6
    n_dice = 3
    p_success = p**n_dice
    n = 1
    p_fail = 1 - p_success

    while p_fail > .5:
        n += 1
        p_fail *= (1 - p_success)

    print('The probability of failure becomes < .5 after', n, 'throws.')

    # Explicit calculation
    print('Explicit calculation: n >', -1 / np.log2(1 - p**n_dice))

    # Simulate (a.k.a. Monte Carlo)
    throws = 1
    trials = 10000
    while proportion(trials, throws, n_dice) < .5:
        throws += 1
    print(f"At least {n_dice} sixes appeared more than half of {trials} "
          f"games if we throw {n_dice} dice {throws} times at each game.")
