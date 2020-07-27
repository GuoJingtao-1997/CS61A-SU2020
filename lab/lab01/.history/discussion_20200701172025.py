
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
print(wears_jacket(40,False))
    
