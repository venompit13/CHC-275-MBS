"""
Make a four function calculator that takes in 2 numbers per opperation

1. take in 2 numbers
2. add them
3. print the sum

1. take 2 numbers (use input to save numbers in variables)
2. subtract them
3. print the difference
"""

""" 
write a 4 func calc where:
    input strionog parsed
    program does not close after one  operation
    math operation is inside try-except block
"""    
print("Welcome to Calculator 2.0!")
check = False
while check == False:
    option = input("Choose Operation or Quit: ").strip().lower()
    if option == "add":
        try:
            num1 = input("Enter numone: ")
            num1 = int(num1)
            num2 = input("Enter numtwo: ")
            num2 = int(num2)
            sum = num1 + num2
            print (f"The sum of {num1} and {num2} is {sum}")
        except ValueError:
            print("no")
    if option == "subtract":
        try:
            num3 = input("Enter num3: ")
            num3 = int(num3)
            num4 = input("Enter num4: ")
            num4 = int(num4)
            difference = num3 - num4
            print(f"The difference of {num3} and {num4} is {difference}")
        except ValueError:
            print("no")
    if option == "multiply":
        try:
            num5 = input("Enter num5: ")
            num5 = int(num5)
            num6 = input("Enter num6: ")
            num6 = int(num6)
            product = num5 * num6
            print(f"The product of {num5} and {num6} is {product}")
        except ValueError:
            print("no")
    if option == "divide":
        try:
            num7 = input("Enter num7: ")
            num7 = int(num7)
            num8 = input("Enter num8: ")
            num8 = int(num8)
            quotient = num7 / num8
            print(f"The quotient of {num7} and {num8} is {quotient}")
        except ValueError and ZeroDivisionError:
            print("no")
    if option == "quit":
        check = True