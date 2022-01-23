import random
from matplotlib import pyplot as plt


if __name__ == "__main__":
    n = 10000000
    interval = 1000
    heads = 0
    tails = 0
    proportion = []
    total = []
    quantity = []
    q = 0

    while n > 0:
        num = min(interval, n)
        q += num
        quantity.append(q)
        tosses = random.choices(population='HT', k=num)
        heads += len(list(filter(lambda x: x == 'H', tosses)))
        tails += len(list(filter(lambda x: x == 'T', tosses)))
        n -= interval
        proportion.append(heads / (heads + tails) - .5)
        total.append(heads - (heads + tails) / 2)

    plt.subplot(121)
    plt.plot(quantity, proportion)
    plt.subplot(122)
    plt.plot(quantity, total)
    plt.show()
