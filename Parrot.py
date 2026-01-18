class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        print(f"{self.name} sings {song}")

    def dance(self):
        print(f"{self.name} is now dancing")

blue = Parrot("Blue", 13)
woo = Parrot("Woo", 16)

print(f"blue is a {blue.species}")
print(f"woo is a {woo.species}")

print(f"{blue.name} is {blue.age} years old.")
print(f"{woo.name} is {woo.age} years old.")

blue.sing(" 'Happy' ")
woo.dance()