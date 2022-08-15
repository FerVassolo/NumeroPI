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
