def wears_jacket(temp, raining):
    return temp < 60 or raining

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket(90,False)
    False
    >>> wears_jacket(40,False)
    True
    >>> wears_jacket(100,True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False

def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

print(so_slow(5)) 
# square(so_slow(5))
    
