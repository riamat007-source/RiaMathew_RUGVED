import pandas as pd
df=pd.read_csv("matches.csv")
df1=pd.read_csv("deliveries.csv")
x=df1[["match_id","total_runs"]]
x=x.groupby("match_id")["total_runs"].sum()
y=pd.merge(df[["id","season"]],x,left_on="id",right_on="match_id")
t=y.groupby("season")["total_runs"].sum()
print(t)
