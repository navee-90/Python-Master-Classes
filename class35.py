students=[]
for i in range(3):
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    city=input("Enter City: ")
    student={"name":name,"age":age,"city":city}
    students.append(student)
print(students)

# for i in students:
#     print(i)
 
# for i in students:
#     print(i["name"]+"-"+i["age"]+"-"+i["city"])

for i in students:
    print(f'{i["name"]}-{i["age"]}-{i["city"]}')