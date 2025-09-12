"""
we want keyboard input

hardcoding into programs i8s not excatly how we use computers
we want some sort of input and output from the ccomputer based on what user does

for example, if we wanted to have a calc, we would want the user to be able to choose tthe number to be added before runtime

there is an entire func in py dedicated to keyboard input

inputy() <= this function does three things
    1. prints prompt into the terminal
    2. scans the keyboard for input
    3. saves the input into a variable
    
input(what is the 1st number)
our obj is take 2 numbers and add them together
"""



"""
the user is going to type in :
numsix = 10
lorkeez = 5
sum = numsix + lorkeez
we expect 15 to be printed
we got 105, that is not the right answer
when input scans the keyboard it assigns the variable to the string data type
variabl;es have 3 pieces of info:
    1. name
    2. data type
    3. attribute
    
numsix
    1. the name numsix
    2. string
    3. "10"
you can't do math with strings. typecasting

typecasting = reassigning datatype of the variable as loing as its valid target

numsix = "Jack Basmaci" <-  i want to typecast this into a number
numsix = "10" <- i can typecast

to change a str -> int
"""

numsix = input("Enter your number ")
numsix = int(numsix)
    #int(variable name) <= will typecast your variable into integer
lorkeez = input("Enter your second number ")
lorkeez = int(lorkeez)
    #now numsix and lorkeez are both datatype integer
sum = numsix + lorkeez
print(f"The sum is {sum}")

"""
input always gives a strong -> you need to typecast this into the correct datatype that you're expecting
"""
