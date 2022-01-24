from matplotlib import pyplot as plt
import numpy as np


if __name__ == "__main__":
    reds = 18
    blacks = 18
    greens = 2
    total = reds + blacks + greens

    prob_red = reds / total
    bets = 500
    samples = np.random.sample(bets)
    winnings_red = (samples <= prob_red) * 1 - (samples > prob_red)

    plt.subplot(121)
    plt.plot(np.cumsum(winnings_red))

    prob_17 = 1 / total
    bets = 500
    samples = np.random.sample(bets)
    winnings_17 = (samples <= prob_17) * 35 - (samples > prob_17)

    plt.subplot(122)
    plt.plot(np.cumsum(winnings_17))

    plt.show()
