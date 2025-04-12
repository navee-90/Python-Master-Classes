# pandas
# in python pandas is a data analysis and manipulation library.
# pip install pandas
import pandas as pd
score=[27,38,56]
series=pd.Series(score)
# print(series)
series1=pd.Series(score,index=["Abhi","Varsha","Divya"])
print(series1)
print(series1["Divya"])