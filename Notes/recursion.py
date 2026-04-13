""" 
functions from math remembner that
    f(x) = x^2
    procedures

functions end after either the function body ends or when a value is returned
recursions allow us to have repetition in our program wihtout having any for-loops/while-loops
recursive function is a fuinction that cxalls itself wwithin body opf function
"""

def bar():
    print("hello")
    bar()

""" 
running the func prints hello forever

every single recursive func can be broken down into 2 pieces
    base case (this ends the function call)
    recursive case (repeats until you hit base case)
 recursive case has to be able to hit base case
"""

def countdown(n):
    if n == 0:
        return
    
    print(n)
    countdown(n-1)

countdown(10)

""" 
why do we care at all about implementing procedure recursively
a lot of the time procedures are hard to implement with for-loops are much easier to implement with recursion
"""

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

print(factorial(5))

""" 
F(n) = F(n-1) + F(n-2)
"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print()
for i in range (11):
    print(fibonacci(i), ends = " ")