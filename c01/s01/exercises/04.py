import numpy as np


def game(win_prob_serve: float, win_prob: float, points: int = 21) -> bool:
    """Simulates a game of raquetball

    The player starts serving and wins with probability 'win_prob_serve' when
    serving, and with probability 'win_prob' when not serving.  The player
    only scores a point if it is serving and wins the volley.  The player
    who scores 'points' first wins the game.

    Returns True if the player won and False otherwise.
    """

    my_serve = True
    my_points = 0
    opponents_points = 0

    while my_points < points and opponents_points < points:
        if my_serve:
            if np.random.sample() < win_prob_serve:
                my_points += 1
                my_serve = True
            else:
                my_serve = False
        else:
            if np.random.sample() < win_prob:
                my_serve = True
            else:
                my_serve = False
                opponents_points += 1

    if my_points == points:
        return True

    return False


if __name__ == "__main__":
    win_prob_serve = .6
    win_prob = .5
    num_games = 10000
    games_won = 0

    for _ in range(num_games):
        if game(win_prob_serve, win_prob):
            games_won += 1

    print(games_won / num_games)
