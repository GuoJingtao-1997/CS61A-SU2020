def is_even(x):
    return x % 2 == 0

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    
    >>> def is even(x):
    ...     # Even numbers have remainder 0 when divided by 2
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n + 1):
        if cond(i):
            print(i)

def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out 
    all integers 1..i..n where calling cond(i) returns True.

    >>> def is even(x):
    ...     # Even numbers have remainder 0 when divided by 2
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def condition(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)
    return lambda cond: condition(cond)

def square(x):
    return x * x

def and_add(f, n):
    """Return a new function. This new function takes an 
    argument x and returns f(x) + n

    >>> def square(x):
    ...     return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """
    return lambda x: f(x) + n

