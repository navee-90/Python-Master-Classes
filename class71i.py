import pandas as pd
score={'Abhi':56,'Varsha':25,'Divya':67}
series=pd.Series(score)
# print(series)
df=pd.Series(score,["Abhi","Divya"])
print(df)