"triangles.py"
""" 
3 angle valuesas inout and determine or not it is a triangle
"""

angle1 = input("Enter angle 1: ")
angle1 = int(angle1)
angle2 = input("Enter angle 2: ")
angle2 = int(angle2)
angle3 = input("Enter angle 3: ")
angle3 = int(angle3)

if (angle1 == 90 and angle2 + angle3 == 90) or (angle2 == 90 and angle1 + angle3 == 90) or (angle3 == 90 and angle1 + angle2 == 90):
    print("This is a triangle")
    
""" 
our test values worked for 90, 30, 60. we need to find a way to make sure we can have very valid combination of angle 1, 2, 3 create  a valid triangle

if you wrap two or more conditionals into one conditioanl using () you  can reframe the 2 conditionals into 1 conditional

truth table
A   B   A and B
T   F      F
F   T       F
F   F       F
T   T       T

A   B   A or B
T   F   T
F   T   T
T   T   T
F   F   F


this was our lession on compound conditional
"""