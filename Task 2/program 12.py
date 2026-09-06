import pandas as pd
df=pd.read_csv("matches.csv")
df1=pd.read_csv("deliveries.csv")
tr=match_runs = df1.groupby("match_id")["total_runs"].sum()
x=pd.merge(df[["id","venue"]],tr,left_on="id",right_on="match_id")
print(x.groupby("venue")["total_runs"].mean())
