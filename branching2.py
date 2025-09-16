"branching2.py"

"""
let's discuss forom a software development standpoint how if-elifs can be used in a software design question

when you launch a game you open to a main menu in our command liune programs

whats an easy way to make a main menu?

1. PRINT OUT ALL OF THE OPTIONS
2. TAKE IN KEYBOARD INPUT
3. USE IFs and ELIFs in order to select the option the user typed in

freshman $5
sophmores $7
juniors $9
seniors $11

"""
print("Welcome to the lunch loan program")
print("Enter your grade level")
print("1. Freshman")
print("2. Sophmore")
print("3. Junior")
print("4. Senior")
option = input("Enter your grade level: ")

if option == "freshman":
    print("You get $5")
if option == "sophmore":
    print("You get $7")
if option == "junior":
    print("You get $9")
if option == "senior":
    print("You get $11")

""" 
your goal is to match the output to the option using ifs and elifs
"""

