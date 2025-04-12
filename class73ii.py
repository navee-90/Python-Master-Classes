import logging
logging.basicConfig(filename="Amount",level=logging.INFO)
logging.debug("This is Debug Message")
balance=0
for i in range(3):
    am=int(input("Eneter Deposit Amount: "))
    balance=balance+am
    logging.info(f"{am} is Deposited")
    print(balance)    