from PiMethods import mathLibraryPi, spigotAlgorithm, GaussLegendre
from Circle.circle import Circle
import math


gausslegendreValue = GaussLegendre.solve(1, 1/math.sqrt(2), 1/4, 1, 3)
spigotValue = spigotAlgorithm.SpigotAlgorithm.calculate(6)

def comparisson():
    print("Distintos valores de pi:")
    print(f"\tMath Library: \n\t\t{mathLibraryPi.getPi()}\n\tSpigot: \n\t\t{spigotValue}\n\tGauss-Legendre: \n\t\t{gausslegendreValue}")

comparisson()

circle1 = Circle(4)
print("---------------------------")
print("Areas para los distintos valores de pi:")
print(f"\tMath Library Area: {circle1.calculateArea(mathLibraryPi.getPi())}")
print(f"\tSpigot Area: {circle1.calculateArea(spigotValue)}")
print(f"\tGauss-Legendre Area: {circle1.calculateArea(gausslegendreValue)}")
