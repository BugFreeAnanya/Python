import sys
def initialize_slambook():
    rows, cols = int(input("Please enter initial number of entries: ")), 6
    slambook = []
    print(slambook)
    for i in range(rows):
        print(f"Enter entry {i+1} details in the following order only")
        print("Note * indicates mandatory fields")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name*: ")))
                if temp[j] == "" or temp[j] == " ":
                    sys.exit("Name is a mandatory field. Exiting the program.")
            if j == 1:
                temp.append(int(input("Enter age*: ")))
            if j == 2:
                temp.append(str(input("Enter favourite color: ")))
                if temp[j] == "" or temp[j] == " ":
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter hobby: ")))
                if temp[j] == "" or temp[j] == " ":
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Enter dream job: ")))
                if temp[j] == "" or temp[j] == " ":
                    temp[j] = None
            if j == 5:
                temp.append(str(input("Enter nickname: ")))
                if temp[j] == "" or temp[j] == " ":
                    temp[j] = None
        slambook.append(temp)
    print(slambook)
    return slambook

initialize_slambook() 

print("\t\tSMARTPHONE DIRECTORY", flush=False)

print("\tYou can now perform the following operation on this\nslambook\n")
print("1. Add a new contact")
print("6. Exit slambook")

def add_contact(pb):
    
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter age: ")))
        if i == 2:
            dip.append(str(input("Enter favourite color: ")))
        if i == 3:
            dip.append(str(input("Enter hobby: ")))
        if i == 4:
            dip.append(str(input("Enter dream job: ")))
        if i == 5:
            dip.append(str(input("Enter nickname: ")))
    pb.append(dip)
    
    return pb
def thanks():
   
    print("******************************************************")
    print("Thank you for using our Slam Book.")
    print("Please visit again!")
    print("******************************************************")
    sys.exit("Goodbye, have a nice day ahead!")


print("........................................................")
print("Hello dear Friends, welcome to our Slam Book")
print("You may now proceed to explore this Slam Book and fill your details about your friends")

pb = initial_slambook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 4:
        pb = add_contact(pb)
    else:
        thanks()
