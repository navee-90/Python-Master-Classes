# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("***HDFC BANK ***")
i=1
balance=0
while i<=10:
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check balance")
    choice=input("Enter choice: ")
    if choice == "1":
        amount=int(input("Enter Amount: "))
        balance=balance+amount
        print("Current balance: ",balance)
    elif choice == "2":
        amount=int(input("Enter amount: "))
        if balance < amount:
            print("Insufficient Funds")
        else:
            balance=balance-amount
            print("Current balance: ",balance)
    elif choice == "3":
        print("Total Balance: ",balance)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
print("Successfully Completed")