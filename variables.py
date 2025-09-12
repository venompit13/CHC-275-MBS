"""
file name: variables.py    
    
Live coding: write in one python file and have notes in multiline

python is a programming language
   - set of syntax and protocols that you write instructions in for your computer top follow 
   - command line program
    - when you download python off the internet, you're downloading what is actually called the python interpreter
        - interpreter's role on your computer is to look at .py files line by line and convert valid python syntax into machine code
        
    - python is an interpreted language
        - just point interpreter at a python file and it'll run the code
        
    - compiled languages
        - c, c++, javaa, etc.
        - call the complier on your code file, and it'll get compiled into an execitible file that you run
        
    - first thing important to us are variables
        -carry three properties
            - name of the variable
            - date type
            - attribute (actual data itself)
        - variable is just a named place on your computer's RAM
"""
x=5
#^ This is your variable
#<name of your variable> = <attribute>

print(x)

"""
Date types:
 
 - nuamebers
 - strings of text
 
2 data types for numbers
    - integer: whole number, including 0 and neagatives
    - float: floating point number, pi
"""
x=5
#this is a variable named x, of typoe integer, of value 5

"""
we can add, subtract, divide, and square numbers
"""

y = 10
#adddition
print(x+y)
#subtraction
print(x-y)
#multiplication
print(x*y)
#division
print(x/y)
#squaring a number
print(x**2)

"""
sometimes when we're manipulating numbers, we want to work with the results again later on

all we did was print the results of our arithmetic

the python interpreter is really not smart, it doesn't remeber what is prints. so in order for python to remember what it did, you need to save it back into another
variable
"""
sum = x + y
print(sum)

"""
so let's keep sum in mind and alsio add another variable to it

equals sign is really just an assingment operator and not an equality operator
"""
sum = sum + 20 #this is perfectly valid
print(sum)
"""
sum is a named place memory

on the left hand side of the quals sign, we're declaring a variable
on the right hand side, we substitue the value of sum into where called it


strings of text:
    - in other programming languages, you have a data type speciffically for single characters of text
    - in python, strings of text are all the same data type (string)
"""

name = "venompit"
#<name of the variable> = <attribute>
print(name)

"""
in python we can do this in 2 ways

    - fstrings: format strings and it lets specify placeholder values in strongs so you can drop in varaibles
"""
print(f"My name is {name}")
print(f"the sum of x and y is {sum}")

"""
we made variables
we added variables
we printed variables using f-strings
"""