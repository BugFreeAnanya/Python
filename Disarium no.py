n = int(input("Enter the number: "))
total_digits = int(input("total no of digits:  "))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** total_digits
    temp = temp // 10
    total_digits = total_digits - 1

if sum == n:
    print("Disarium number.")
else:
    print("Not a Disarium number.")