import pandas as pd
df=pd.read_csv("matches.csv")
x =pd.concat([df["umpire1"], df["umpire2"], df["umpire3"]])
print("the umpire who umpired maximum number of times")
print(x.value_counts().head(1))



