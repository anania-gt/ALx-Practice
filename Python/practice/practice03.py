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
"""
or we can do
if __name__ == "__main__":
    print("Running tests...")
    print(f"add(2, 3) = {add(2, 3)}")  # Expected output: 5
    print(f"subtract(5, 3) = {subtract(5, 3)}")  # Expected output: 2
"""