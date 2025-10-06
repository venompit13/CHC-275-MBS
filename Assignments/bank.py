print("Welcome to FFCU Bank!") #the followig is how to make a coding system for a fake virtual bank with the option to remove and add accounts as well as depositing, withdrawling, and tranfering money between accounts
names = ["Mitch Schauer", "Gabby Crespo", "Colin Lawton", "Paul Gage", "Asher Collins"] #list of accounts matching up woth balances
balances = [10000, 15000, 20000, 30000, 1000] #list of balances mat hing up with accounts

check = False
while check == False:
    for i in range(len(names)):
        print(f"Name: {names[i]}; Balance: {balances[i]}")
    print("1. Add Account?")
    print("2. Remove Account?")
    print("3. Deposit?")
    print("4. Withdrawl?")
    print("5. Transfer Funds?")
    print("6. Coming Soon...")
    option = input("Select option or quit to exit: ")
    if option == "1":
        name = input("Enter account name you want to add to the list: ")
        names.append(name)
        bal = input("Enter account balance for account:") #bal is a varibale for the balance of the added account
        bal = int(bal)
        balances.append(bal) #append adds to the list this is adding to balances list
    elif option == "2":
        name = input("Enter account name you want to remove:")
        index = names.index(name)
        names.pop(index) #pop removes from list, this removing from names list
        balances.pop
    elif option == "3":
        name = input("Which account is depositing: ")
        index = names.index(name)
        money = input("How much is being deposited: ")
        money = int(money)
        balances[index] = balances[index] + money #equation needed for adding amount to balance
    elif option == "4":
        name = input("Which account is withdrawling: ")
        index = names.index(name)
        money = input("How much is being withdrawn: ")
        money = int(money)
        balances[index] = balances[index] - money #equation needed for subtracting from balance
    elif option == "5":
        name = input("Which account is transferring: ")
        index = names.index(name)
        name2 = input("To which account: ")
        index2 = names.index(name2)
        transfer = input("How much is being transfered: ")
        transfer = int(transfer)
        balances[index] = balances[index] - transfer #both equations cover adding and subtracting from DIFFERENT accounts
        balances[index2] = balances[index2] + transfer
    if option == "quit":
        check = True 