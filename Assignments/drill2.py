"""
write a function called makeList() that
    takes in numbers via input() and typecasts them to integers, then appends them to a list called
    nums UNTIL the user types "stop"
    returns that list

    try making 2 lists using makeList() and print those lists out
"""

def makeList():
    nums = []
    pass
    while True:
        user = input("enter a number or 'stop': ")
        if user.lower() == "stop":
            break
        try:
            number = int(user)
            nums.append(number)
        except ValueError:
            print("ENTER VALID INTEGER")
    return nums

list1 = makeList()
print(list1)
list2 = makeList()
print(list2)