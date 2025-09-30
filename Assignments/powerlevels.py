""" 
Problem 3: powerlevels.py

if the 1st number is bigger than the 2nd one, print num1 wins
if the 2nd number is bigger, print num2 wins
if theyre equal print that its a tie
"""

num1 = input("Enter power level: ")
num1 = int(num1)
num2 = input("Enter power level: ")
num2 = int(num2)
if num1 > num2: 
    print(f"{num1} Wins!")
elif num1 < num2:
    print(f"{num2} Wins!")
elif num1 == num2: 
    print("Tie!")
 