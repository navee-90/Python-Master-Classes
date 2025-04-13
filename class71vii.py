# import pandas as pd
# df=pd.read_csv("Score.csv")
# print(df)
import pandas as pd
data={
    'Maths':{"Ajay":35,"karna":67,"Manoj":87},
    "Science":{"Ajay":65,"karna":56,"Manoj":97},
    "History":{"Ajay":68,"karna":86,"Manoj":57}
}
arr=pd.DataFrame(data)
# print(arr)
arr=pd.DataFrame(data,index=["Ajay","karna","Manoj"]) #same names give in index
print(arr)
df=arr.to_csv("Data.csv")
print(df)
# df=pd.read_csv("Data.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())