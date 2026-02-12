"""
Docstring for Notes.stacalc
"""

def main():
    num = []
    go = True
    def makeList():
        nonlocal go
        nums = input("Enter number... ")
        if nums.lower().strip() == "quit":
            go = False
            print(nums)
        else:
            try:
                nums = int(nums)
                num.append(nums)
                return num
            except ValueError:
                pass
            
    while go:
        makeList()
        
    while not go:
        print("Choose Calculator Function:")
        print("Get 'Min'")
        print("Get 'Max'")
        print("Get 'Median'")
        print("Get 'Mean'")
        print("Get 'stdDev'")
        print("Quit")
        choice = input("Enter choice... ")
        if choice.lower().strip() == "min":
            print(min(num))
        elif choice.lower().strip() == "max":
            print(max(num))
        elif choice.lower().strip() == "median":
            num.sort()
            if len(num) % 2 == 0:
                median = (num[len(num) // 2 - 1] + num[len(num) // 2]) / 2
            else:
                median = num[len(num) // 2]
            print(median)
        elif choice.lower().strip() == "mean":
            mean = sum(num) / len(num)
            print(mean)
        elif choice.lower().strip() == "stddev":
            sdmean = sum(num) / len(num)
            for i in range(len(num)):
                num[i] = (num[i] - sdmean) ** 2
            stddev = (sum(num) / len(num)) ** 0.5
            print(stddev)
        elif choice.lower().strip() == "quit":
            go = True
        else:
            print("nope")
            
if __name__ == "__main__":
    main()
    