def summation(n,term):
    """Sum the first N terms of a sequence.

    >>> summation(5,cube)
    225
    """
    total,i=0,1
    while i<=n:
        total,i=total+term(i),i+1
    return total

def identity(n):
    return n

def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    return summation(n,identity)

def cube(n):
    return pow(n,3)

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    return summation(n,cube)

def term3(n):
    return 8/((4*n-3)*(4*n-1))

def sum_term3(n):
    """Sum the first N terms of a sequence.

    >>> sum_term3(5)
    3.041839618929402
    """
    return summation(n,term3)