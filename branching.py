"""
when we run a calc program, we expect to be able to choose which opperaiton we want to do from a list of options

having some sort of main menu protocol is contigent on our control structure

control structures=individual steps in our program
    -sequential (lines running one after another)
    -branching (what we're doing today)
    - repetition (reopeating code blocks)

branching = we wanbt code blocks to run based ojn certain conditions being mewt within our program

boolean=t/f

conditional =  some logical statement that can evaluated to a boolean value
            = some english statement that is either true or false
if <conditional>
    <must be tabbed over code block>
    
modulus: %

what modulus does is divide a by b and returns the remainder
a % b = a mod b = the remainder after a/b
we can use modulus for divisibbility rules. for a numbnber to be divisible by 2

a % 2 = 0

"""



"""
ONE EQUALS (=) is for variable assignment TWO EUALS (==) is for equallity checking

    Garunteed ways to screq up if statements:
    1. make sure you have colon after if statement
    2. make sure the codeblock underneatrh the if statement is tabbed over
    3. make sure EVERY line of code under if statement has the same amount of white space
    
    VS CODE TOP TIP:
        if you highlight all of whitespace, you'll see how many spaces are there
        1 tab = 4 spaces
        
"""

x = 15
if x % 2 ==0:
    print(f"{x} is divisible by 2")
    print("example")
    if x % 4 == 0:
        print (f"{x} is divisible by 4")
    elif x % 3 == 0:
        print("whatever")
elif x % 3 == 0:
    print(f"{x}  is divisible by 3")
    print("example")
else:
    print("fail condition")

"""
Last class we covered if statements: IF-ELIF-ELSE
branchingg paths within our programs
Booleans: true or false values
Conditional statements: statements thzt can be evaluated to true or false

if <conditional>:
    <code block>
elif <conditional>:
    <code block>
else:
    <code block>
    
equality: ==
variable assignment: =

there are time times where you want to evaluate more than  one codiitional
<coditional> AND <other conditional>

for ex, for something to be a triangle
angle 1 == 90 AND angle 2 + angle 3 == 90
condition 1: angle 1 == 90
condition 2: angle 2 + angle 3 == 90
"""