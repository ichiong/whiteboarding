#!/usr/bin/python

def best(stock_prices):
  """"Given a list of prices, return the maximum profit.

  If no profit is possible, return 0.

    >>> best([15, 10, 20, 22, 1, 9])
    12
    >>> best([1, 2, 3, 4, 5])
    4
    >>> best([2, 3, 10, 6, 4, 8, 1])
    8
    >>> best([7, 9, 5, 6, 3, 2])
    2
    >>> best([0, 100])
    100
    >>> best([5,4 ,3, 2, 1])
    0
    >>> best([100])
    0
    >>> best([100, 0])
    0
    >>> best([])
    0

  """

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GREAT JOB!")
    print()
