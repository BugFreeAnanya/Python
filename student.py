class Student:
    stream = "CSE"
    def __init__(self, roll):
        self.roll = roll
    def set_address(self, address):
        self.address= address
    def get_address(self):
        return self.address
    
add = Student(111)
add.set_address("123 Main St, Cityville")
print(add.get_address())

a = Student(111)
b = Student(112)
print(a.stream)
print(b.stream)
print(Student.stream)