"""
Dow Selection
-------------

Topics: Boolean array operators, sum function, where function, plotting.

The array 'dow' is a 2-D array with each row holding the
daily performance of the Dow Jones Industrial Average from the
beginning of 2008 (dates have been removed for exercise simplicity).
The array has the following structure::

       OPEN      HIGH      LOW       CLOSE     VOLUME      ADJ_CLOSE
       13261.82  13338.23  12969.42  13043.96  3452650000  13043.96
       13044.12  13197.43  12968.44  13056.72  3429500000  13056.72
       13046.56  13049.65  12740.51  12800.18  4166000000  12800.18
       12801.15  12984.95  12640.44  12827.49  4221260000  12827.49
       12820.9   12998.11  12511.03  12589.07  4705390000  12589.07
       12590.21  12814.97  12431.53  12735.31  5351030000  12735.31

0. The data has been loaded from a .csv file for you.
1. Create a "mask" array that indicates which rows have a volume
   greater than 5.5 billion.
2. How many are there?  (hint: use sum).
3. Find the index of every row (or day) where the volume is greater
   than 5.5 billion. hint: look at the where() command.

Bonus
~~~~~

1. Plot the adjusted close for *every* day in 2008.
2. Now over-plot this plot with a 'red dot' marker for every
   day where the volume was greater than 5.5 billion.

See :ref:`dow-selection-solution`.
"""

from numpy import loadtxt, sum, where, array, reshape, arange
import matplotlib.pyplot as plt

# Constants that indicate what data is held in each column of
# the 'dow' array.
OPEN = 0
HIGH = 1
LOW = 2
CLOSE = 3
VOLUME = 4
ADJ_CLOSE = 5


def first_exercise(dow, minimum_volume=5_500_000_000):
    return dow[:, VOLUME] >= minimum_volume


def second_exercise(high_volume_mask):
    return sum(high_volume_mask)


def third_exercise(dow, high_volume_mask):
    return [index for index in arange(0, len(dow)) if high_volume_mask[index]]


def fourth_exercise(dow, ax):
    ax.set(xlabel='Relevation time', ylabel='Adjusted close',
           title='MONEY, MY PRECIOUS MONEY!')
    ax.plot(arange(0, len(dow)), dow[:, ADJ_CLOSE], label='Adjusted close')
    return None


def fifth_exercise(dow, high_volume_rows, ax):
    ax.scatter(high_volume_rows, dow[high_volume_rows, ADJ_CLOSE],
               marker='o', color='red', label='Adj close with high volume')
    return None


if __name__ == '__main__':
    dow = loadtxt('dow.csv', delimiter=',')
    print('First exercise:')
    high_volume_mask = first_exercise(dow)
    print(high_volume_mask)
    print('Second exercise:')
    print(second_exercise(high_volume_mask))
    print('Third exercise')
    high_volume_rows = third_exercise(dow, high_volume_mask)
    print(high_volume_rows)

    fig, ax = plt.subplots()

    print('Fourth exercise')
    print(fourth_exercise(dow, ax))
    print('Fifth exercise')
    print(fifth_exercise(dow, high_volume_rows, ax))
    plt.legend()
    plt.show()

# 0. The data has been loaded from a .csv file for you.

# 'dow' is our NumPy array that we will manipulate.

# 1. Create a "mask" array that indicates which rows have a volume
#    greater than 5.5 billion.


# 2. How many are there?  (hint: use sum).

# 3. Find the index of every row (or day) where the volume is greater
#    than 5.5 billion. hint: look at the where() command.

# BONUS:
# a. Plot the adjusted close for EVERY day in 2008.
# b. Now over-plot this plot with a 'red dot' marker for every
#    day where the volume was greater than 5.5 billion.
