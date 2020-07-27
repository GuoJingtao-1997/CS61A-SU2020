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

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    num = n
    while n != 2:
        n -= 1
        if not (num % n):
            is_prime = False
            print(n)
            break
        else:
            print(n)
            is_prime = True
    return is_prime
print(is_prime(7)) 
