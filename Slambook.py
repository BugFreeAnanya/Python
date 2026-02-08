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