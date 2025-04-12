# class12
import pandas as pd
details={
    "Maths":{'Alekya':35,"John":76,"Suma":87},
    "Science":{"Alekya":67,"John":79,"Suma":68},
    "Social":{"Alekya":77,"John":49,"Suma":48},
}
df=pd.DataFrame(details)
# print(df)
data=df.to_csv("details.csv")
# print(data)
show=pd.read_csv("details.csv")
# show=pd.read_csv("details.csv",header=None)
print(show)
print(show.head())
print(show.tail())
print(show.info())
print(show.describe())
print(show.shape)
print(show.size)
print(show.columns)
print(show.dtypes)
print(show.isnull())