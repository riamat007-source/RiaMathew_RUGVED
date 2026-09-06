import pandas as pd
df=pd.read_csv("matches.csv")
x=df.groupby("city").size()
print(x)
