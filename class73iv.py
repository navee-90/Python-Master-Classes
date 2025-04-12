# ATM Machine
import logging
logging.basicConfig(filename="ATM.log",level=logging.INFO,format='%(asctime)s %(message)s')
balance=0
while True:
    print("1.Deposit")
    print("2.Credit")
    print("3.Check balance")
    print("4.Exit")
    choice=int(input("Enter Your choice: "))
    if choice==1:
        amount=int(input("Enter Deposit Amount: "))
        balance=balance+amount
        logging.info(f"{balance} is Deposited")
        print(f"Total Balance is : {balance}")
    elif choice==2:
        amount=int(input("Enter Credit Amount: "))
        if amount>balance:
            print("Insufficient Fund")
        else:
            balance=balance-amount
            logging.info(f"{balance} is Credited")
            print(f"Total Balance is : {balance}")
    elif choice==3:
        print(f"Total Balance is : {balance}")
    elif choice==4:
        break
print("Program Successfully completed!")