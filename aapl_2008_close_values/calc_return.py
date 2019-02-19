"""
Calc return
===========

For a given stock, the return is connected to its close price p by

         p(t) - p(t-1)
ret(t) = -------------
             p(t-1)

The close price for Apple stock for all business days in 2008 is loaded for you
from the data file `aapl_2008_close_values.csv`.

1. Use these values to compute the corresponding daily return for every
business day of that year (except the first one).

2. Plot these returns, converted to percentages, over the course of the year.
On the same plot, draw a red line at 0.

Note: a for loop is neither necessary nor recommended for this calculation

Bonus
~~~~~
3. There is some blank space in the plot made in question 2 because by default,
matplotlib displays plots with a range along the x axis that is larger than the
highest x coordinate. Use IPython to learn about matplotlib's `plt.xlim` function
and make the limits of your plot tighter.
"""
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt


def first_exercise(prices):
    return [(prices[index] - prices[index-1])/prices[index-1] for index in np.arange(1, prices.size)]


def second_exercise(returns, ax):
    ax.set(xlabel='Relevation time', ylabel='Return %',
           title='Apple to eat, I am hungry')
    percentages = [value * 100 for value in returns]
    ax.plot(np.arange(0, len(percentages)), percentages, label='Returns')
    return None


def third_exercise(returns, padding=1):
    plt.xlim(-padding, len(returns) + padding)
    return None


if __name__ == '__main__':
    prices = np.loadtxt("aapl_2008_close_values.csv",
                        usecols=[1], delimiter=",")
    print("Prices for AAPL stock in 2008:")
    print(prices)
    print('First exercise:')
    returns = first_exercise(prices)
    print(returns)

    fig, ax = plt.subplots()

    print('Second exercise:')
    print(second_exercise(returns, ax))
    print('Third exercise')
    print(third_exercise(returns))

    plt.legend()
    plt.show()
