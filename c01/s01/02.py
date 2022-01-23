import numpy as np


if __name__ == "__main__":
    sample_size = 0
    num_experiments = 100
    possibilities = ['H', 'T']
    proportion = 0

    while proportion < .95:
        sample_size += 1
        within_range = 0
        for _ in range(num_experiments):
            samples = np.random.choice(possibilities, sample_size)
            heads = samples == 'H'
            if np.abs(heads.sum() / sample_size - .5) <= .1:
                within_range += 1
        proportion = within_range / num_experiments

    print(sample_size)
