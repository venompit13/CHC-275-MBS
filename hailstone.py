check = False
while check == False:
    x = input("Enter your number: ")
    x = int(x)
    
    if x % 2 == 1:
        print(x * 3 + 1)
    elif x % 2 == 0:
        print(x/2)
    elif x == 1:
        check == True