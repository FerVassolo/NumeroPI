import math
import decimal

def solve(a, b, t, p, n): # newA, newB quiere decir An+1, Bn+1. La variable x ya es Xn+1
    if (n > 0):
        x = (a+b)/2
        newA = x
        newB = math.sqrt(a*b)
        t = t - p*math.pow(a-x, 2)
        pi = math.pow(newA+newB, 2)/(4*t)
        p = 2*p
        n -= 1
        if n != 0:
            return solve(newA, newB, t, p, n)
        else:
            return pi
solve(1, 1/math.sqrt(2), 1/4, 1, 4)


def conDecimal(a, b, t, p, n):
    D = decimal.Decimal
    a = a
    b = b
    t = t
    p = p
    if (n > 0):
        x = (a+b)/2
        newA = x
        newB = (a*b).sqrt()
        t = t - p*(a-x)*(a-x)
        pi = ((newA+newB)*(newA+newB))/(4*t)
        p = 2*p
        n -= 1
        if n != 0:
            return conDecimal(newA, newB, t, p, n)
        else:
            return pi

D = decimal.Decimal
conDecimal(1, 1/D(2).sqrt(), 1/D(4), 1, 5)


