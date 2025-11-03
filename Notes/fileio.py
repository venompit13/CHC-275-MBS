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

file = open("Notes/names.txt", "r")
names = file.readlines()
print(names)
for i in range(len(names)):
    names[i] = names[i].strip()
print(names)
file.close()

""" 
opening the file
reading into list called buffer
preproccessiong data such thatt we can use it in our porgram

writting into a file?

third mode opening file called append mode
"""