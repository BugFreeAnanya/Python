my_dict = {}
my_dict = {'apple': 1, 'mango': 2, 'orange': 3 , 'cherry': 4}

key = input("Enter the fruit name to find it's value: ")
print("The value is :", my_dict.get(key, "Key not found"))