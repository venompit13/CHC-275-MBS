small_mush = []
med_mush = []
large_mush = []
check = False
while check == False:
    size = input("Enter mushroom size: ").strip().lower()
    if size == "stop":
        check = True
    elif size.isnumeric:
        if size < 100:
            small_mush = small_mush.append(size)
        elif size >= 100 and size < 200:
            med_mush = med_mush.append(size)
        elif size <= 200:
            large_mush = large_mush.append(size)
print(small_mush)
print(med_mush)
print(large_mush)
    