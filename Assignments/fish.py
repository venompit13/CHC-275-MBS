print("Welcome to the Docks! Go catch some fish.")
print("Carnivorous")
print("SaltWater")
print("Community")
option = input("What did you catch: ")

if (option == "carnivorous"):
    print("Do you already have this?")
    option = input(" ")
    if (option == "yes"):
        print("Too Bad!")
    elif (option == "no"): 
        print("Enjoy!")
elif (option == "saltwater"):
    print("You're a fancy fish parent!")
elif (option == "community"):
    print("You should get more than one!")
else:
    print("I don't think that's a fish!")