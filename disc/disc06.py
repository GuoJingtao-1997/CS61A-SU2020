import tree as t

tree = t.tree
branches = t.branches
is_leaf = t.is_leaf
label = t.label

def memory_f(n):
    """return a one-argument function which takes in a
    function that is used to update n.

    >>> f = memory_f(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f_maker(f):
        nonlocal n
        n = f(n)
        return n
    return f_maker

def nonlocalist():
    """return two function prepend and get, which represent the 
    "add to front of list" and "get the ith item" operations, respectively.
    Do not use any python built-in data structures like lists or dictionaries.

    Just too difficult fo me
    >>> prepend, get = nonlocalist()
    >>> prepend(2)
    >>> prepend(3)
    >>> prepend(4)
    >>> get(0)
    4
    >>> get(1)
    3
    >>> get(2)
    2
    >>> prepend(8)
    >>> get(2)
    3
    """
    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = get
        def get(i):
            if not i:
                return value
            return f(i - 1)
    return prepend, lambda i: get(i)

# f = lambda n: [print(i) for i in range(1, n + 1)]
# f = f(10)
# print(f)

square = lambda x: x * x
double = lambda x: 2 * x
def memory(x, f):
    """return a higher-order function that prints its memories
    You may only use names and call expressions in your solution. 
    You may not write numbers or use features of Python not yet covered in
    the course.

    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    def g(h):
        nonlocal f
        print(f(x))
        f = h
        return g
    return g

def announce_losses(who, last_score=0):
    """return a commentary function that announces whenever 
    that player loses points

    >>> f = announce_losses(0)
    >>> f1 = f(10, 0)
    >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
    Oh no! Player 0 just lost 9 point(s).
    >>> f3 = f2(7, 10)
    >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
    >>> f5 = f4(11, 12)
    """
    assert who == 0 or who == 1, 'the who argument should indicate a Player'
    def say(score0, score1):
        if who == 0:
            score = score0
        elif who == 1:
            score = score1
        if score < last_score:
            print("Oh no! Player {0} just lost {1} point(s).".format(who, last_score - score))
        return announce_losses(who, score)
    return say

def fox_says(start, middle, end, num):
    """return a string 
    You cannot use any for or while statements and string operations
    other than '+' operator

    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(n):
        if n == 1:
            return middle
        return middle + '-' + repeat(n - 1)
    return start + '-' + repeat(num) + '-' + end

def primary_stress(t):
    """let’s write a function that, given one of
    these tree structures, identifies the stressed part of a word or phrase.

    >>> word = tree("", [tree("s", [tree("w", [tree("min")]), tree("w", [tree("ne")])]),tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
    >>> primary_stress(word)
    'so'
    >>> phrase = tree("", [tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]),tree("w", [tree("requirement")])])
    >>> primary_stress(phrase)
    'law'
    """
    def helper(t, num_s):
        if is_leaf(t):
            return [label(t), num_s]
        if label(t) == "s":
            num_s += 1
        return max([helper(branch, num_s) for branch in branches(t)], key = lambda lst: lst[1])
    return helper(t, 0)

def subset_sum(seq, k):
    """
    >>> subset_sum([2, 4, 7, 3], 5) # 2 + 3 = 5
    True
    >>> subset_sum([1, 9, 5, 7, 3], 2)
    False
    >>> subset_sum([1, 1, 5, -1], 3)
    False
    >>> 3 in [1, 2, 3]
    True
    >>> 4 in [1, 2, 3]
    False
    """
    subset = {}
    for num in seq:
        subnum = k - num
        if subnum in subset:
            return True
        subset[num] = 1
    return False
