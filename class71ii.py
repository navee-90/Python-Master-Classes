import pandas as pd
data1={'Swathi':[69],'RAJI':[87],"ADHI":[76]}
df=pd.DataFrame(data1)
# print(df)
df=pd.DataFrame(data1,index=['Swathi'])
print(df)