import pandas as pd
score={
    'name':["Adhi","Badra","Asini"],
    'score':[87,67,45],
    'city':["Hyd","MI","PU"]
}
# df=pd.DataFrame(score)
# print(df)
df=pd.DataFrame(score,index=["Rank1","Rank2","Rank3"])
print(df)
d=df.to_csv("score.csv")
print(d)