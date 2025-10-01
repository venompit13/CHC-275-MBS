print("Welcome to FFCU Bank!")
names = ["Mitch Scahuer", "Gabby Crespo", "Colin Lawton", "Paul Gage", "Asher Collins"]
balances = [10000, 15000, 20000, 30000, 1000]

check = False
while check == False:
    for i in range(len(names)):
        print(f"Name: {names[i]}; Balance: {balances[i]}")
    print("1. Add Account?")
    print("2. Remove Account?")
    print("3. Deposit?")
    print("4. Withdrawl?")
    print("5. Transfer Funds?")
    option = input("Select option or quit to exit: ")
    if option == "1":
        name = input("Enter account name you want to add to the list: ")
        names.append(name)
        bal = input("Enter account balance for account:")
        bal = int(bal)
        balances.append(bal)
    elif option == "2":
        name = input("Enter account name you want to remove:")
        index = names.index(name)
        names.pop(index)
        balances.pop
    elif option == "3":
        name = input("Which account is depositing: ")
        index = names.index(name)
        money = input("How much: ")
        money = int(money)
        balances[index] = balances[index] + money
    if option == "quit":
        check = True