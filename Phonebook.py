import sys
def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")), 5
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print(f"Enter contact {i+1} details in the following order only")
        print("Note * indicates mandatory fields")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name*: ")))
                if temp[j] == "" or temp[j]== " ":
                    sys.exit("Name is a mandatory field. Exiting the program.")
            if j == 1:
                temp.append(int(input("Enter phone number*: ")))
            if j == 2:
                temp.append(str(input("Enter email: ")))
                if temp[j] == "" or temp[j] == " ":
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j] == "" or temp[j] == " ":
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Enter category(family/friends/works/others): ")))
                if temp[j] == "" or temp[j] == " ":
                    temp[j] = None
        phone_book.append(temp)
    print(phone_book)
    return phone_book

initial_phonebook()