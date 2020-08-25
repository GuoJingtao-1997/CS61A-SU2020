import tree as t1

tree = t1.tree
branches = t1.branches
is_leaf = t1.is_leaf
label = t1.label
print_tree = t1.print_tree

def height(tree, depthest=0):
    """Return the height of a tree.

    >>> t = tree(1,[tree(3,[tree(4),tree(5),tree(6)]),tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(tree):
        return depthest
    depth = 0
    for branch in branches(tree):
        depth = max(depth, height(branch, depthest + 1))
    return depth

def square_tree(t):
    """Return a tree with the square of every element in t

    >>> print_tree = t1.print_tree
    >>> numbers = tree(1,
    ...             [tree(2,
    ...                     [tree(3),
    ...                     tree(4)]),
    ...             tree(5,
    ...                     [tree(6,
    ...                         [tree(7)]),
    ...                     tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    return tree(label(t) ** 2, [(lambda branch: tree(label(branch) ** 2) if is_leaf(branch) else square_tree(branch))(branch) for branch in branches(t)])

def find_path(tree, x):
    """Return a list containing the nodes along the path required to 
    get from the root of the tree to a node containing x.


    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 13) # returns None
    """
    if label(tree) == x or is_leaf(tree):
        return tree
    for branch in branches(tree):
        path = find_path(branch, x)
        if path != None and x in path :
            return [label(tree)] + path

def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(2, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    while x:
        lst.append(el)
        x -= 1

def group_by(s, fn):
    """a function that takes in a sequence s and a function fn 
    and returns a dictionary

    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    group = {}
    for n in s:
        i = fn(n)
        if i not in group:
            group[i] = [n]
        else:
            group[i] += [n]
    return dict(sorted(group.items(), key=lambda d: d[0]))

# def partition_options(total, biggest):
#     """outputs all the ways to partition a number
#     total using numbers no larger than biggest.

#     >>> partition_options(2, 2)
#     [[2], [1, 1]]
#     >>> partition_options(3, 3)
#     [[3], [2, 1], [1, 1, 1]]
#     >>> partition_options(4, 3)
#     [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
#     """
#     if not total or total == 1:
#         return biggest
#     elif total < 0 or not biggest:
#         return []
#     else:
#         with_biggest = partition_options(total - biggest, biggest)
#         without_biggest = partition_options(total, biggest - 1)
#         with_biggest = [[with_biggest] + without_biggest]
#     return with_biggest + without_biggest
    

def min_elements(T, lst, num=0):
    """Return the minimum number of elements from the list that 
    need to be summed in order to add up to T.

    >>> min_elements(10, [2, 4, 1]) # 4 + 4 + 2
    3
    >>> min_elements(12, [9, 4, 6, 1]) # 6 + 6
    2
    >>> min_elements(0, [1, 2, 3])
    0
    """
    if not T:
        return 0
    lst = sorted(lst, reverse=True)
    def min_num(T, lst, num):
        if not T:
            return num
        elif T in lst:
            return num + 1
        elif T < 0:
            return min_num(T + lst[0] * num, lst[1:], 0)
        return min_num(T - lst[0], lst, num + 1)
    return min_num(T - lst[0], lst, num + 1)
