try:
    x = int(input("Enter num 1: "))
    y = int(input("Enter num 2: "))
    quo = x/y
    print(quo)
except ValueError:
    print("Both inputs need to be numeric")
except ZeroDivisionError:
    print("Cannot divide by zero!")