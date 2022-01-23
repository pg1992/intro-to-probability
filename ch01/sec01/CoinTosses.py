#! /usr/bin/env python

"""
This module contains the scripts for the simulations of the
questions 1 and 2 from section 1.1 of the book
'Introduction to Probability' by Grinstead and Snell.
"""

import random as rnd
import sys


def printTosses(maxTosses: int = 1000, interval: int = 100):
    """A random experiment showing the behavior of coin tosses.

    This routine shows how the proportion of heads minus 0.5 behaves
    as the number of tosses increases from 1 to 'maxTosses', and also
    how the number of heads minus half the number of tosses
    behaves.

    It prints those results periodically with the specified 'interval'
    between prints.
    """

    rnd.seed()
    num_heads = 0.
    num_tails = 0.
    for i in range(1, maxTosses + 1):
        if rnd.randrange(2) == 0:
            num_heads += 1.
        else:
            num_tails += 1.
        if i % interval == 0:
            prop = num_heads / i - .5
            print(f'{i:06d}: Proportion of heads minus 1/2 = {prop:.3f}.')

            prop *= i
            print(f'{i:06d}: # of heads minus 1/2 the # of tosses: {prop:d}.')
            print('-' * 80)


def printSampleSize(num_exp: int = 100, max_tosses: int = 100,
                    num_trials: int = 100, prop: float = 0.95,
                    dev: float = 0.1):
    """Find the average number of coin tosses required so that the proportion
    of heads lies in the confidence interval.

    Run 'num_exp' experiments with 'num_trials' trials each. In each experiment
    the number of coin tosses increases from 1 to 'max_tosses'.
    The minimum number of tosses necessary so that a proportion 'prop' of
    trials has the proportion of heads lying within 'dev' of 0.5 is stored.
    At the end of the routine the minimum number of tosses is averaged over
    all experiments.
    """

    rnd.seed()
    average_min_num_toss = 0.
    for experiment in range(num_exp):
        for num_tosses in range(1, max_tosses + 1):
            in_range = 0
            for trial in range(num_trials):
                num_heads = 0.
                num_tails = 0.
                for toss in range(num_tosses):
                    if rnd.randrange(2) == 0:
                        num_heads += 1.
                    else:
                        num_tails += 1.
                prop_heads = num_heads / (num_heads + num_tails)
                if abs(prop_heads - 0.5) <= dev:
                    in_range += 1
            if in_range/num_trials >= prop:
                average_min_num_toss += num_tosses
                break
    average_min_num_toss /= num_exp
    print('Number of experiments:', num_exp)
    print('Number of trials per experiment:', num_trials)
    print('Target proportion of successful trials:', prop)
    print('Proportion of heads considered success:', 'within', dev, 'of', 0.5)
    print('Average of the minimum number of tosses per trial over all '
          'experiments that reaches the target proportion of successful '
          'trials:', average_min_num_toss)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Exercise 01:\n')

        numTosses = int(input('Number of tosses: '))
        interval = int(input('Specify the printing interval: '))

        printTosses(numTosses, interval)

        print('\nExercise 02:\n')
        printSampleSize()
    else:
        ex_num = int(sys.argv[1])
        if ex_num == 1:
            numTosses = int(input('Number of tosses: '))
            interval = int(input('Specify the printing interval: '))

            printTosses(numTosses, interval)
        elif ex_num == 2:
            printSampleSize(dev=0.1)
