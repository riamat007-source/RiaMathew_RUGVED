import pandas as pd
df1=pd.read_csv("deliveries.csv")
t=df1.groupby("batsman")["batsman_runs"].sum()
t=t.sort_values(ascending=False)
print(t.head(10))
