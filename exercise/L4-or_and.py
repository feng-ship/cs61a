from math import sqrt
def has_big_sqrt(n):
    return n>0 and sqrt(n)>10

def reasonable(n):
    return n==0 or 1/n!=0