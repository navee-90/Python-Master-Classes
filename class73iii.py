import logging
logging.basicConfig(filename="Bank.log",level=logging.INFO,format='%(asctime)s %(message)s')
balance=0
while True:
    amount=int(input("Enter Deposit Amount: "))
    balance=balance+amount
    logging.info(f"{amount} is Deposited")
    print(balance)
    