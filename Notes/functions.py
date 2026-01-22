#functions.py
"""
Drills starting this semester
    - small program
    - reading code and evaluating what the output is or whether there is an error

be able to  write code once and use it twice or more
f(x) = x^2
^takes x as input and outputs x squared

routines u can repeat that outputs something

pros:
    - we can reuse code rather than having to rewrite it all the time
    - much more readable
    
cons:
    - kinda difficult to undewrstand what is happening in the program
    - we introduce a large level of abstraction that we ar enot used to so far
        - this includes "control flow being more complicated, in the sense that code execution has owners and services

"""

#basic function example
def foo(): #function header
           #1 def keyword
           #2 function name
           #3 parameter list
    #startiung from line 31, this is the function body. func needs to be indented
    #when func ends, you must unindent
    print("bar")

foo() #remember using a func end name with ()

""" 
functions act like verbs in plain  english
u can think of () as being period at end of sentence
"""

def add(x,y):
    print(x + y)
    
add(6,7)
add("foo","bar")
