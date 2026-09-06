import pandas as pd
df=pd.read_csv("matches.csv")
x=df.groupby("city").size()
print("the city with minimum matches is",x.idxmin())
print("the city with maximum matches is",x.idxmax())
