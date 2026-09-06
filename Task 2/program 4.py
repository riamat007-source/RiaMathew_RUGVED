import pandas as pd
df=pd.read_csv("matches.csv")
x=df.groupby(["toss_winner","toss_decision"]).size()
print(x)

