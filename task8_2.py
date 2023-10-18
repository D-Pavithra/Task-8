class circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = 3.141
    def area(self):
        return self.pi*self.radius*self.radius
r = circle(4 , 3.141)
A = r.area()
print(A)