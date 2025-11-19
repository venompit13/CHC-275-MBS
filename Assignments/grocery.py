print("Welcome to Sage Grocery!")
file = open("Assignments/food.txt", "r")
stock = file.readlines()
items = []
prices = []
file.close()
for line in stock:
    line = line.strip()
    line = line.split(",")
    items.append(line[0])
    prices.append(line[1])

check = False
while check == False:
    for i in range(len(items)):
        print(f" Item: {items[i]}; Price: {prices[i]}")
    cart = []
    total = []
    print("1. Add to Cart")
    print("2. Remove from Cart")
    print("3. Go to Checkout")
    print("4. Quit")
    option = input("Select option or quit: ")
    if option == "1":
            print(items)
            print(prices)
            carts = input("What would you like to add: ")
            cart.append(carts)
            num = input(f"How many {carts} would you like: ")
            num = int(num)
            total.append(num)
    elif option == "2":
            print(cart)
            remove = input("What would you like to remove: ")
            index = items.index(remove)
            items.pop(index)
    if option == "quit":
        check = True