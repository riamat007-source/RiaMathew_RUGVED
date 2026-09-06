import pandas as pd
df=pd.read_csv("deliveries.csv")
x=df[df["dismissal_kind"].isin(["bowled", "caught", "caught and bowled",
     "lbw", "stumped", "hit wicket"])]
y=x.groupby("bowler").size()
print(y)

