lst= ["Apple", "Banana", "Kiwi", "Mango", "Orange"]

print("The length of list is:", len(lst))
print("The first element is:", lst[0])
print("The last element is:", lst[-1])

lst.append("Grapes")
print("Updated list:", lst)
lst.remove("Kiwi")
print("Updated list:", lst)
lst.sort()
print("Updated list:", lst)
lst.reverse()
print("Updated list:", lst)
lst.pop(3)
print("Updated list:", lst)
print("Multiplication of list:", lst*2)
lst= lst[:4]
print("Sliced list:", lst)
lst.clear()
print("Cleared list:", lst)