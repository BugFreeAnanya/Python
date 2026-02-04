print("Star Pattern")
for i in range(1,7):
    for j in range(i):
        print("*", end = "")
    print("\n")

print("Inverted Star Pattern")
for i in range(7,1,-1):
    for j in range(i):
        print("*", end = "")
    print("\n")