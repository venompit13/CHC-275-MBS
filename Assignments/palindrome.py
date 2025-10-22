#strings behave like lists can use for-loops (pulls out individual character one by one)
#when adding 2 strings if str1 is hello and str2 world add them str1 + str2 = hello world
#2 pointers method on google\
check = True
palindrome = input("Type in your palindrome: ").strip().lower()
palindrome = palindrome.split()
palindrome = "".join(palindrome)
left = 0
right = len(palindrome) - 1
while left < right and check == True:
    if palindrome[left] == palindrome[right]:
        left = left + 1
        right = right - 1
    else:
        check = False
if check == True:
    print("PALINDROME!")