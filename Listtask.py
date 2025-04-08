Accounts=[]
for i in range(3):
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    city=input("Enter City: ")
    account={"name":name,"age":age,"city":city}
    Accounts.append(account)
print(Accounts)

for i in Accounts:
    print(f"{i['name']}-{i['age']}-{i['city']}")