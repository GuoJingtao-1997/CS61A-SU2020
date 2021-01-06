from operator import mul


def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    nums = 0
    while lnk is not Link.empty:
        nums += lnk.first
        lnk = lnk.rest
    return nums

def multiply_lnks(lis_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    mul = 1
    for i in range(len(lis_of_lnks)):
        if lis_of_lnks[i] is Link.empty:
            return Link.empty
        mul *= lis_of_lnks[i].first
        lis_of_lnks[i] = lis_of_lnks[i].rest
    return Link(mul, multiply_lnks(lis_of_lnks))

def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link != Link.empty:
        try:
            if f(link.first):
                yield link.first
            link = link.rest
        except StopIteration:
            print("StopIteration")
        

def filter_no_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """ 
    if link is Link.empty:
        return 
    elif f(link.first):
        return [link.first] + filter_no_iter(link.rest,f)
    filter_no_iter(link.rest, f)
    
def make_even(t):
    """
    >>> t = Tree(1, [Tree(5, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    >>> t.branches[0].label
    6
    """
    # if t.is_leaf():
    #     return
    # elif t.label % 2 != 0:
    #     t.label += 1
    # for b in t.branches:
    #     if b.label % 2 != 0:
    #         b.label += 1
    #     make_even(b)
    if t.label % 2 != 0:
        t.label += 1
    for b in t.branches:
        make_even(b)

def square_tree(t):
    """
    Mutates a Tree t by squaring all its elements.

    >>> t = Tree(2, [Tree(5, [Tree(3)]), Tree(4), Tree(5)])
    >>> square_tree(t)
    >>> t.label
    4
    >>> t.branches[0].branches[0].label
    9
    >>> t.branches[0].label
    25
    """
    t.label **= 2
    for b in t.branches:
        square_tree(b)

def find_path(t, entry):
    """
    Return False if entry is not present in t, 
    else return a path from the root of t to entry

    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(5)])
    >>> find_path(tree_ex, 5)
    [[2, 7, 6, 5], [2, 5]]
    >>> find_path(tree_ex, 12)
    False
    """
    def helper(t, entry):
        paths = []
        if t.label == entry:
            paths.append([entry])
        for b in t.branches:
            for path in helper(b, entry):
                paths.append([t.label] + path)
        return paths
    paths = helper(t, entry)
    return paths if paths else False
    # if t.label == entry:
    #     return [entry]
    # for b in t.branches:
    #     path = find_path(b, entry)
    #     if path:
    #         return [t.label] + path
    # return False

def average(t):
    """
    Return the average value of all the nodes in t.

    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    def sum_helper(t):
        total, count = t.label, 1
        for b in t.branches:
            total_b, count_b  = sum_helper(b)
            total, count = total + total_b, count + count_b
        return total, count
    total, count = sum_helper(t)
    return total / count

def combine_tree(t1, t2, combiner):
    """
    Combines the values of two trees t1 and t2 together with the combiner function
    This function should return a new tree.
    
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    # t = Tree(combiner(t1.label, t2.label))
    # for b in zip(t1.branches, t2.branches):
    #     t = Tree(combiner(t1.label, t2.label), [combine_tree(b[0], b[1], combiner)])
    # return t

    """Another solution using list comprehension"""
    branch = [combine_tree(b[0], b[1], combiner) for b in zip(t1.branches, t2.branches)]
    return Tree(combiner(t1.label, t2.label), branch)

def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    # def map_helper(t, depth=0):
    #     if depth % 2 == 0:
    #         t.label = map_fn(t.label)
    #     for b in t.branches:
    #         map_helper(b, depth + 1)
    #     return t
    # return map_helper(t)

    """Another solution without using helper function"""
    label, branch = map_fn(t.label), []
    for b in t.branches:
        b0 = [alt_tree_map(bb, map_fn) for bb in b.branches]
        branch.append(Tree(b.label, b0))
    return Tree(label, branch)


class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            tree_str = ", " + repr(self.branches)
        else:
            tree_str = ""
        return  "Tree({0}{1})".format(self.label, tree_str)

    
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = "," + repr(self.rest)
        else:
            rest_str = " "
        return 'Link{0}{1}'.format(repr(self.first), rest_str)

    def __str__(self):
        string = '<'
        while self.rest != Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


