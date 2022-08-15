import math
from unicodedata import decimal


class SpigotAlgorithm:
    def calculate(n):
        sum = SpigotAlgorithm._iteration(0)
        i = 1
        while i < n:
            sum += SpigotAlgorithm._iteration(i)
            i += 1
        return sum

    def _iteration(i) -> decimal:
        return ((math.factorial(i) ** 2) * 2 ** (i + 1)) / (math.factorial(2 * i + 1))
    
    def calculate_for_n_decimals(n):
        k = 2
        a = 4
        b = 1
        a1 = 12
        b1 = 4
        while n > 0:
            p, q, k = SpigotAlgorithm.calculate_pqk(k)
            a, b, a1, b1 = SpigotAlgorithm.calculate_ab(a, b, a1, b1, p, q)
            d, d1 = SpigotAlgorithm.calculate_d(a, b, a1, b1)
            while d == d1 and n > 0:
                yield int(d)
                a = 10 * (a % b)
                a1 = 10 * (a1 % b1)
                d, d1 = SpigotAlgorithm.calculate_d(a, b, a1, b1)
                n -= 1

    def calculate_pqk(k):
        return (k * k, 2 * k + 1, k + 1)

    def calculate_ab(a, b, a1, b1, p, q):
        return (a1, b1, p * a + q * a1, p * b + q * b1)

    def calculate_d(a, b, a1, b1):
        return (a / b, a1 / b1)
