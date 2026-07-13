balance = 1000
while True:
    print("\n1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")

    choice = int(input("enter your choice:"))
    if choice == 1:
        print("balance:",balance)
    elif choice == 2:
        amount = int(input("enter the deposit amount:"))
        balance += amount
        print("amount deposited successfully")
    elif choice == 3:
        amount = int(input("enter the withdraw amount"))
        if amount <= balance:
            balance -= amount
            print("amount withdrawn successfully!")
        else:
            print("insufficient balance")
    elif choice == 4:
        print("thank u!")
    else:
        print("invalid")
