import logging
logging.basicConfig(filename="Marks.log",level=logging.DEBUG)
logging.info("This is Information message")
balance=0
for i in range(3):
    amount=int(input("Enter Deposit Amount: "))
    balance=balance+amount
    logging.debug(f"{amount} is Deposited")
    print(balance)

