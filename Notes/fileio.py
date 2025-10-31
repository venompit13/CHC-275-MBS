""" 
exception handliong leads to file input/ouput

most fioles on comps are text files with specifics contextxs

.docx are .txts with microosoft overhead
"""

msg = "hello \nworld"
print(msg)

""" 
escape sequences decided when one line starts and another ends

fileitself may not exist in system
"""

file = open("names.txt", "r")
names = file.readlines()
print(names)
for i in range(len(names)):
    names[i] = names[i].strip()
print(names)
file.close()