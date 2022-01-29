import numpy as np


def roulette(bets: int = 1000) -> int:
    reds = 18
    blacks = 18
    greens = 2

    odds = reds / (reds + blacks + greens)

    wins = 0

    for _ in range(bets):
        if np.random.sample() < odds:
            wins += 1
        else:
            wins -= 1

    return wins


if __name__ == "__main__":
    bets = 1000
    print(f'Winnings after {bets} bets = {roulette(bets)}.')
