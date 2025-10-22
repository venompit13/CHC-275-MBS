small_mush = []
med_mush = []
large_mush = []
check = False
while check == False:
    size = input("Enter mushroom size: ").strip().lower()
    if size == "stop":
        check = True
    elif size.isnumeric():
        size = int(size)
        if size < 100:
            small_mush.append(size)
        elif size >= 100 and size < 200:
            med_mush.append(size)
        elif size >= 200:
            large_mush.append(size)
print(small_mush)
print(med_mush)
print(large_mush)