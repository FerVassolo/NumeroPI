from PiMethods import mathLibraryPi, spigotAlgorithm, GaussLegendre
from Circle.circle import Circle
import math
import decimal


gausslegendreValue = GaussLegendre.solve(1, 1/math.sqrt(2), 1/4, 1, 4)
D = decimal.Decimal
gausslegendreDecimals = GaussLegendre.conDecimal(1, 1/D(2).sqrt(), 1/D(4), 1, 5)
spigotValue = spigotAlgorithm.SpigotAlgorithm.calculate(45)

print("Distintos valores de pi:")
print(f"\tMath Library: \n\t\t{mathLibraryPi.getPi()}\n\tSpigot: \n\t\t{spigotValue}\n\tGauss-Legendre: \n\t\t{gausslegendreValue}\n\tGauss-Legendre con decimals: \n\t\t{gausslegendreDecimals}")


circle1 = Circle(4)
print("---------------------------")
print("Areas para los distintos valores de pi:")
print(f"\tMath Library Area: {circle1.calculateArea(mathLibraryPi.getPi())}")
print(f"\tSpigot Area: {circle1.calculateArea(spigotValue)}")
print(f"\tGauss-Legendre Area: {circle1.calculateArea(gausslegendreValue)}")
print(f"\tGauss-Legendre con decimals Area: {circle1.calculateArea(gausslegendreDecimals)}")
