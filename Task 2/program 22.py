import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("matches.csv")
x=df.groupby(["toss_winner","toss_decision"]).size().unstack()
x.plot(kind="barh")
plt.title("toss decisions")
plt.xlabel("decisions")
plt.ylabel("toss winner")
plt.show()
