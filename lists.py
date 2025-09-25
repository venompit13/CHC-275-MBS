""" 
recap:
    - create variables and manipouplate them basic ways
        - doing arithmatic
    - branching
    - repetition
    - keyboard input
    - typecast variables

benefit of using computer at all is amoutn of data computer can process

so if i wanted bunch of related data points, the only way i can do that currently ius by creating a bunch of individual variables
creating individual variuables is unwidely way of goingg about this
we need one alias(name)

lists = linear ordered collections of objects under one varibale name (one memory address)
    = lists are also variables
<name of the list> = [<member attributes>]
"""

mylist = [5,10,15,20]
print(mylist)

""" 
how do we acces one singular element from the list square brackets indicate list
use square bracket operator on variabnel name and place the index of object we want to reference inside the sbs

index = the numerical position of the object within the list
"""

print(mylist[0])

""" 
counting in comp sci starts at 0
dereferencing elements from a list b  ehaves exactlky like a variballe would
"""
print(mylist[0] * mylist[3])
sum = mylist[1] + mylist[2]
print (sum)

""" 
NOTE: iun other languages list has to share same datatype
not in python
"""

mylist2 = [1,3.14,True,"hello"]
print(mylist2[2])

""" 
cannot acces placers in memory that are not allocated yet
negatives go backwards
"""

print(mylist2[-1])

mylist = [5,10,15,20]

""" 
in porgramming there is adesign pattern called traversing a list
    - repetition control center where 1 by 1 acces each element of the list
    
iterator - number that corresponds with index you are trying access
use i to denote the interator

we wiull use a while loop and iterator to traverse our list
"""
i = 0
while i <= 3:
    print(mylist[i])
    i = i + 1
    
""" 
most of the time index errors occur from not having suitable exit condition
cumbersome to use

another weay to do this almost equivalent to this
use for-loops to do almost same thing
"""

mylist = [5,10,15,20,25,30]
print("for-loop")
for huh in mylist:
        print(huh)
        
""" 
for-loops:
    create temporary vartiable tassigned toi the name you give
    it assigns that tempv to location you created
    does the procedure in code block
    goes to nect item in the list
huh =/= mylist[i]
    2 seperate things with same value
"""

for huh in mylist:
    huh = huh + 5
print(mylist)

i = 0
while i <= len(mylist) - 1:
    mylist[i] = mylist[i] * 5
    i = i + 1
print(mylist)

""" 
for-loop did not update list
    crate copies
while loop updated list
    directly acces the list
    
this while loop makes a huige assumption about the list, the lists last object is at mylist[3]
the list could be length 0 or length 100

there is a way to intrinsically get the last value of the list
length function
"""

print(len(mylist))