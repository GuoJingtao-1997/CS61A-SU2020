""" Optional problems for Lab 3 """

def cal_remainder(n, divided_num):
    remainder, divided_num = n % divided_num, int(divided_num - 1)
    if not remainder:
        return False
    elif divided_num <= 1:
        return True
    return cal_remainder(n, divided_num)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    assert n > 1
    "*** YOUR CODE HERE ***"
    divided_num = n ** 0.5
    return cal_remainder(n, divided_num)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    r = a % b
    if not r:
        a = b
        return a
    return gcd(b, r)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    all_but_last， last = n // 10， n % 10

