import pandas as pd
df=pd.read_csv("matches.csv")
x=df[df["win_by_runs"]>0]
max1=x.groupby("winner")["win_by_runs"].max()
min1=x.groupby("winner")["win_by_runs"].min()
print("the team who won by the highest number of runs",max1.idxmax(),"by",max1.max())
print("the team who won by the lowest number of runs",min1.idxmin(),"by",min1.min())
