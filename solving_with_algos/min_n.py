# Write two Python functions to find the minimum number in a list. The first function should
# compare each number to every other number on the list. O(n 2 ). The second function should be
# linear O(n).

import numpy as np

low = 1
high = 1001
size = 1001
numbers = np.random.randint(low, high, size)


def o_n2(numbers):
  lowest = high
  for n in numbers:
    for x in numbers:
      if n < x and n < lowest:
        lowest = n
  return lowest


def o_n(numbers):
  lowest = None
  for n in numbers:
    if lowest is None or n < lowest:
      lowest = n
  return lowest


def o_n_r(numbers, r=None):
  for x in numbers:
    if r is None or x < r:
      r = x
      o_n_r(numbers, r)
  return r