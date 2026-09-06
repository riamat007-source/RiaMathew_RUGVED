import pandas as pd
df=pd.read_csv("matches.csv")
x=df[df["win_by_runs"]>0]
max1=x["win_by_runs"].max()
min1=x["win_by_runs"].min()
print("the venue where the team won by highest number of runs",x[x["win_by_runs"]==max1]["venue"].iloc[0])
print("the venue where the team won by lowest number of runs",x[x["win_by_runs"]==min1]["venue"].iloc[0])
