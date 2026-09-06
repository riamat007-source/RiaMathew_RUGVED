import pandas as pd
df=pd.read_csv("matches.csv")
x=df.groupby("season").size()
print(x)
