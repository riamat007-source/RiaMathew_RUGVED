import pandas as pd
df=pd.read_csv("deliveries.csv")
x=df.groupby("batsman")["batsman_runs"].sum()
y=df[df["player_dismissed"].notna()].groupby("player_dismissed").size()
print((x/y).sort_values(ascending=False).head(10))
