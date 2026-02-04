def fib_series(n):
    n1, n2 = 0,1
    count = 0
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

n = int(input("Enter thenumber of terms: "))
if n <= 0:
    print("Please enter a positve integer")
else:
    print("Fibonacci Series: ")
    fib_series(n)