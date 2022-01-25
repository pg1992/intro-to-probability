import numpy as np
from numpy import linalg as LA
from matplotlib import pyplot as plt


def random_walk() -> int:
    directions = np.array([
        [+1,  0],
        [-1,  0],
        [0, +1],
        [0, -1],
    ])

    position = np.array([0, 0])
    position += directions[np.random.choice(4)]
    n = 1

    while LA.norm(position) > 1e-3:
        position += directions[np.random.choice(4)]
        n += 1
        if n > 1e4:
            return np.Inf

    return n


if __name__ == "__main__":
    plt.stem([random_walk() for _ in range(100)])
    plt.show()
