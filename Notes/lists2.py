""" 
for-loops make copy of elements instead of directly accessing them

"""

mylist = [10,20,30,40,50]
            #0,1,2,3,4

""" 
would you say the indices also count as an ordered sequence of elements? YES

rather than travesing list of elements in a for-loop
could traverse over inciedces instead

there are two new functions involved:

    range(<name of list>) <= creates a list of numbers corresponding to the iondices of a list
    range(len(mylist)) = [0,1,2,3,4] <= we can do a for-loop over this instead
    
    len(<name of list>)  = this returns the length of the list
"""

"""for i in range(len(mylist)):
    print(mylist[i])
    
for num in mylist:
    print(num)
    
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1"""
    
""" 
1) for-i loop
2) for-each loop
3) while loop
"""

"""print("example 2")
for i in range(len(mylist)):
    mylist[i] = mylist[i] + 5
print (mylist)"""

""" 
lists in python are dynamically sized  we can add and remove elemnts from the list

to add something to the list:
    -<nameoflist>.append(<value we want to add to list)
"""
"""print("example 3")
names = ["john","james","paul"]
print (names)
names.append("zach")
print(names)"""

""" 
two ways top remove from list:
    either by index
    by the value
"""

"""snames.remove("john")
print(names)

names.pop(0)
print(names)

print("example 4")
names = []
check = False
while check == False:
    name = input("Enter the name you want to add to the list ")
    if name == "quit":
        check = True
    else:
        names.append(name)
        
print(names)"""

print("example 5")

students = ["john","zach","paul"]
GPAs = [88,71,85]

""" 
tied by the index
"""

for i in range(len(students)):
    print(f"Student: {students[i]} GPA: {GPAs[i]}")
    
""" 
we assuming that the user has perfect knowledge and can access the contents and indces of the list
bad assumption because lists are dynamically sized (same indices line up, bad to assume this)

need a way to search our list
how get indices out of listy without having to look at code before hand

.index()

<nameoflist>.index(<value>)
"""
print("example 6")
index = students.index("zach")
print(index)
