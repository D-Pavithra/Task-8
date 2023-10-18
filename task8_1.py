class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        areas = [3.14*r**2 for r in self.radius]
        return areas
radius = [10, 501, 22, 37, 100, 999, 87, 351]
C = circle(radius)
A = C.area()
print(A)