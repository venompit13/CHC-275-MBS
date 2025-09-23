x = input("Enter your number: ")
x = int(x)
check = False

while check == False:
    if x % 2 == 1:
        x = x * 3 + 1
        print(x)
    elif x % 2 == 0:
        x = x/2
        print(x)
    elif x == 1:
        check = True