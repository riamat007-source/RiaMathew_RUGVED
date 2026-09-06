import pandas as pd
df=pd.read_csv("matches.csv")
x=df.groupby("result").size()
print("normal matches:",x["normal"])
print("tied matches:",x["tie"])

