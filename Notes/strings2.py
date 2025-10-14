""" 
.split() method in Python
Splits a string into a list where each word is a list item. The default separator is any whitespace.
.join() method in Python
Joins the elements of an iterable (like a list or tuple) into a single string, with a specified separator.
.lower() and .upper() methods in Python
Converts all characters in a string to lowercase or uppercase, respectively.
"""


mystr = "101010101010Hello101010World101010How101010Are101010You101010"
msg = mystr.split("101010")
print(msg)

space = " "
newmsg = space.join(msg)
print(newmsg)

""" 
what .join() does is it takes each element of the list and puts the string we called .join() on in between each element

you can call strong methods on strings that arent saved to variables
"""

newmsg = " ".join(msg)
print(newmsg)

newmsg = " ".join(msg).strip()
print(newmsg)

""" 
python behaves in a weird way when it comes to strings and booleans
an empty string is considered false

entire unit on stroing parsing
.strip()
.lower()
.upper()
.split()
.join()
.splitlines()
.itsnumeric()

recall this that we can add numbers using +

"""
sum = 5 + 4
print(sum)

str1 = "Hello"
str2 = "World"
join = str1 + " " + str2
print(join)