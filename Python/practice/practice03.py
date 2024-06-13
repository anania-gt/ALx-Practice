def add(a, b):
    """
    Returns the sum of a and b.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
"""
we add verbose = True to get feedback
"""
