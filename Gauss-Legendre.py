import math

def solve(a, b, t, p, n): # newA, newB quiere decir An+1, Bn+1. La variable x ya es Xn+1
    if (n > 0):
        x = (a+b)/2
        newA = x
        newB = math.sqrt(a*b)
        t = t - p*math.pow(a-x, 2)
        pi = math.pow(newA+newB, 2)/(4*t)
        p = 2*p
        print(pi)
        n -= 1
        return solve(newA, newB, t, p, n)
solve(1, 1/math.sqrt(2), 1/4, 1, 4)
