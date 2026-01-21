class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def area(self):
        return self.length * self.width
    
Rectangle1 = Rectangle(12 , 5)
print(f"Length: {Rectangle1.length} , Width: {Rectangle1.width}")
print("Area of Rectangle:", Rectangle1.area())