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
    if not b:
        return a
    r = a % b
    return gcd(b, r)

def count_appearance(n, digit, lenN, position=0):
    if position == lenN:
        return digit
    digit[n[position]], position = digit[n[position]] + 1, position + 1
    return count_appearance(n, digit,,position)

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
    digit = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    count_appearance(str(n), digit, len(str(n)))
    ten_pairs = 0
    if digit['1'] and digit['9']:
        ten_pairs += digit['1'] * digit['9']
    if digit['2'] and digit['8']:
        ten_pairs += digit['2'] * digit['8']
    if digit['3'] and digit['7']:
        ten_pairs += digit['3'] * digit['7']
    if digit['7'] and digit['6']:
        ten_pairs += digit['4'] * digit['6']
    # if digit['5'] > 1:


    return ten_pairs

print(ten_pairs(73824601))

