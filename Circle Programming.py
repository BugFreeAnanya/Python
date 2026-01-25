class Circle:
     # Finding area and perimeter of Circle

    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
circle1 = Circle(10)
print(f"Radius of the Circle is: {circle1.radius}")
print("Area of the Circle is:", circle1.area())
print("Perimeter of the Circle is:", circle1.perimeter())