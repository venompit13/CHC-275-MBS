""" 
Next pert about strings and about the act of parsing strings

effectively analyzing the input and making sure its in ther correct format

reading input -> transforming into something we care about/can manipulate -> pythoin code on that

a = input("enter num 1:")

typecasting is a form of parsing our input

lasting we talked about were lists and for-loops and other forms of iteration
now we will talk about strings

strings of text also behave as lists <= supposed to be indblowing
cnsider this a list of chracters
"""
"""print("for each loop")
mystr = "hello"
for char in mystr:
    print(char)
print("for i loop")
for i in range(len(mystr)):
    print(mystr[i])"""

""" 
same ideas/behaviors from lists work for strings

both inherit from smae parent called iterable <= python trivia

strings have their own functions that are interesting to us
"""

"""print("1. A")
print("2. B")
print("3. C")
print("4. D")
option = input("Enter your selection: ")
if option == "A":
    print("Execuiting A!")
elif option == "B":
    print("Execuiting B!")
elif option == "C":
    print("Execuiting C!")
elif option == "D":
    print("Execuiting D!")"""
    
""" 
our design pattern only works with very strict parsing. we couldnt have estra added spaces, our input had to be exactly as descrribed

python has a lot of built in functions to help us parse strings better

.strip() <= removes whitespace from the start and end of a string
"""
"""mystr2 = "                 A          "
mystr2 = mystr2.strip()
print(mystr2)"""


print("1. A")
print("2. B")
print("3. C")
print("4. D")
option = input("Enter your selection: ")
if option.strip() == "A":
    print("Execuiting A!")
elif option.strip() == "B":
    print("Execuiting B!")
elif option.strip() == "C":
    print("Execuiting C!")
elif option.strip() == "D":
    print("Execuiting D!")

""" 
string matching was case sensitive
2 functions that force string to be all uppercase or all lowercase
.upper() and .lower()

we have .lower() and .upper() to help with case sensitivity and .strip() to help with whitespace issues

addition only works if both values are of the same data type
if wrong crashes the whole program
if we dont input a number into option it causes valuer error

only typecasting we want is if they type in a number
how dow we parse option? if else statement
onyl typecast if user types in a number

we have a function called isnumeric() that returns true if the string is a number

"""
option = input("Enter your number: ")
if option.strip().isnumeric():
    option = int(option)
    ex = option + 5
    print(f"{option} + 5 = {ex}")
else:
    print(f"{option} is not a number!")

""" 
parsing a string in order not to get an error is called error/exception handling
standards of code is a lot higher now because we can type check and error handle

/n stands for new line
/t stands for tab
i want to parse my poem string and seperate each line into its own element  of a list called lines
.splitlines() <= splits a string into a list of strings at each new line
"""
poem = "roses are red\nviolets are blue\nsugar is sweet\nand so are you"
lines = poem.splitlines()
print(lines)
