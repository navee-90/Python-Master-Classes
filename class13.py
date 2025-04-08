# HDFC bank task
print("*** HDFC BANK ***")
balance=0
while True:
    print("1.Deposit")
    print("2.withdraw")
    print("3.Check Balance")
    print("4.Exit")
    choice=input ("Enter your choice: ")
    if choice == "1":
        amount=int(input("Enter amount: "))
        balance=balance+amount
        print("Tota payment is: ",balance)
    elif choice == "2":
        amount=int(input("Enter Amount: "))
        if balance < amount:
            print("Insufficient Funds")
        else:
            balance=balance-amount
            print("Current Balance: ",balance)
    elif choice == "3":
        print("Total Balance: ",balance)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
     