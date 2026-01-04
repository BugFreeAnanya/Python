x = int(input("Enter the base number: "))
n = int(input("Enter the number of terms: "))

print("The power series is: ")
for i in range(n):
    result = x**i
    print(f"{x}^{i} = {result}")