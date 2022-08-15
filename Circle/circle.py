class Circle:
    def __init__(self, r):
        self.r = r

    def calculateArea(self, piValue):
        area = piValue * self.r**2
        return area
