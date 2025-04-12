import pandas as pd
data1={
        "Names":["Abhi","varsha","Ram"],
        "score":[25,65,78],
        "city":["Hyd","MI","DI"]
}
df=pd.DataFrame(data1)
# print(df)
d=pd.DataFrame(data1,index=["Rank1","Rank2","Rank3"])
# print(d)
e=d.to_csv("data1.csv")
print(e)