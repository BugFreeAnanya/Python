class Fruit:
    category = "Food"
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def details(self):
        print(f"{self.name} is {self.color} and belongs to {self.category} category.")
        
Fruit1 = Fruit("Apple", "Red")
Fruit2 = Fruit("Banana", "Yellow")

Fruit1.details()
Fruit2.details()