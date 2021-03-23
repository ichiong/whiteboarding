#!/usr/bin/python

def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7":

    >>> check("D6", "H6")
    True
    >>> check("E6", "E4")
    True
    >>> check("B7", "D5")
    True
    >>> check("A1", "H8")
    True
    >>> check("A8", "H1")
    True
    >>> check("D6", "H7")
    False
    >>> check("E6", "F4")
    False

    """

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GREAT JOB!")
    print()
