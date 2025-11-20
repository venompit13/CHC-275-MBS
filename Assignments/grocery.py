print("Welcome to Sage Grocery!")
file = open("Assignments/food.txt", "r")
stock = file.readlines()
items = []
prices = []
file.close()
for line in stock:
    line = line.strip()
    line = line.split(",")
    line[1] = float(line[1])
    items.append(line[0])
    prices.append(line[1])
cart = []
cost = []
check = False
while check == False:
    for i in range(len(items)):
        print(f" Item: {items[i]}; Price: {prices[i]}")
    print("1. Add to Cart")
    print("2. Remove from Cart")
    print("3. Go to Checkout")
    print("4. Quit")
    option = input("Select option or quit: ")
    if option == "1":
        try:
            print(items)
            print(prices)
            carts = input(f"What would you like to add: ")
            carts = int(carts)
            cart.append(items[carts])
            num = input(f"How many {items[carts]} would you like: ")
            num = int(num)
            total = num * prices[carts]
            cost.append(total)
        except Exception as e:
            print(e)
    elif option == "2":
        try:
            print(cart)
            remove = input(f"What would you like to remove: ")
            remove = int(remove)
            cart.pop(remove)
            cost.pop(remove)
        except Exception as e:
            print(e)
    elif option == "3":
        subtotal = sum(cost)
        tax = subtotal * .06
        grandtotal = subtotal + tax
        print(cart)
        print(f"your total is {grandtotal}")
        check = True
    if option == "4":
        check = True