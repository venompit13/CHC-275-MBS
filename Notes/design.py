""" 
progrrameer implemented functions, problem of file is no longer obvious to us

readable files
exposed all of the under implemented functions as the interpreter starts executing code

REQUIREMENTS:
    all fun ctions to be exposed to us
    dont want code being executed inline with function definitions
    
    code should be function definitions at top
    executed atr bottom
    

"""

def foo():
    print("bar")
    
def fizz(x):
    if x % 2 == 1:
        print("buzz")
        
def main():
    check = True
    while check == True:
        print("welcome to test program")
        print("1. foo")
        print("2. fizz")
        print("type exit to quit")
        option = input("enter your option: ")
        if option == "1":
            foo()
        if option == "2":
            number = input
        