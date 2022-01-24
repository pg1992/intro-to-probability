import numpy as np


if __name__ == "__main__":
    p = 1/6
    n_dice = 3
    p_success = p**n_dice
    n = 1
    p_fail = 1 - p_success

    while p_fail > .5:
        n += 1
        p_fail *= (1 - p_success)

    print('simulating, we get', n)
    print('n must be greater than', -1/np.log2(1-p**n_dice))
