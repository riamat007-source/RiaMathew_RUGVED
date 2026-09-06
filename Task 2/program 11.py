import pandas as pd
df=pd.read_csv("deliveries.csv")
print(df[df["batsman_runs"]==6])
