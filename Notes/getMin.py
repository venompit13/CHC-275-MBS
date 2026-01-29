"""
For this assignment you will be writing a function called getMin() that has these properties:
    parameters: userList (this is a list of integer values)
    performs a while loop over the entire list that searches for the minimum values
    once the minimum is found, returns that value
"""

def getMin(userList):
    if not userList:
        return None
    
    index = 0
    min_val = userList[0]

    while index < len(userList):
        if userList[index] < min_val:
            min_val = userList[index]
        index += 1
    return min_val

print(getMin([1, 2, 3, 4]))
print(getMin([4, 3, 1, 3]))