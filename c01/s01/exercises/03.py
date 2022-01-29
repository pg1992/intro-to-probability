import numpy as np


if __name__ == "__main__":
    n = 100_000_000
    dice_num = 3

    rolls = np.random.choice(6, (n, dice_num)) + 1
    rolls_sum = rolls.sum(axis=1)

    sum_9 = (rolls_sum == 9).sum()
    sum_10 = (rolls_sum == 10).sum()

    print('proportion of 9s', sum_9 / n)
    print('proportion of 10s', sum_10 / n)

    if sum_10 > sum_9:
        print('The gamblers were correct (10 comes up more often than 9)')
