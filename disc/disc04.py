def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    return multiply(m, n - 1) + m


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    if n == 1:
        return False
    def prime_helper(k=2):
        if k > n ** 0.5:
            return True
        elif not (n % k):
            return False
        return prime_helper(k + 1)
    return prime_helper()


def count_stair_ways(n):
    """Return ways to count stairs
    >>> count_stair_ways(4)
    5
    """
    if n == 1 or n == 0:
        return 1
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0 or k == 1:
        return 1
    elif n < 0:
        return 0
    steps, total = 1, 0
    while steps <= k:
        total += count_k(n - steps, k)
        steps += 1
    return total

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if not (i % 2)]

def max_product(s):
    """Return the maximum product that can be formed using non-consecutive 
    elements of s.

    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not s:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))

def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    """ String way
    def helper(s):
        if len(s) == 1:
            return True
        return s[1] < s[0] and s[1] < s[2] and helper(s[2:])
    return helper(str(n))
    """
    "number way"
    if n < 10:
        return True
    return (n % 10) > (n // 10 % 10) and (n // 10 % 10) < (n // 100 % 10) and check_hole_number(n // 100)


def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    """ list way
    def helper(s, is_increasing):
        if len(s) == 1:
            return True
        if is_increasing and s[0] < s[1]:
            return s[0] < s[1] and helper(s[1:], True)
        return s[0] > s[1] and helper(s[1:], False)
    return helper(str(n), True)
    """
    "number way"
    def helper(n, is_increasing):
        if n < 10:
            return True
        if is_increasing and (n % 10) < (n // 10 % 10):
            return (n % 10) < (n // 10 % 10) and helper(n // 10, True)
        return (n % 10) > (n // 10 % 10) and helper(n // 10, False)
    return helper(n, True)
