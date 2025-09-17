"looping.py"

""" 
your computer has a component called the random access memory. RAM is responsible for holding all of the info corresponding to process that are running currentrly

when a python program is ran, what the python interpreter will do is allocated partitions of RAM to 2 dif collections

    - Stack: a fixed amount of memory for things like function calls and basic variable assignment
        You have limited memory bugdet for your program
    - Heap: a dynamically changing amount of memory for things like complex data structures
        you have a changing memory budget for your program

"""

"""x = 1
while x <= 10:
    print(x)
    x += 1
    
nums = [1,2,3,4,5,6,7,8,9,10]
x = 0
sum = 0
while x <= len(nums):
    sum += nums[x]
    x += 1
    
    print(f"the sums is {sum}")
    

looping stetments are useful for  repeating a ton of math over and over again. How else are they useful?

from a program design standpoint, they also allow us to repeat an entire program until we quit

there is a boolean datatype, we can set variables equal to True or False

"""

check = False
while check == False:
    print("option 1")
    print("option 2")
    print("option 3")
    option = input("Select your option type or quit to exit: ")
    if option == "1":
        print(1)
    elif option == "2":
        print(2)
    elif option == "3":
        print(3)
    elif option == "quit":
        check = True
