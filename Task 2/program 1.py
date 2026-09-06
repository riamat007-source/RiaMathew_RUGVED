import pandas as pd
df=pd.read_csv("matches.csv")
x=df[df["season"]==2008]
print("the number of matches in 2008 is",len(x))
