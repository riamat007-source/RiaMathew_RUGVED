import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("matches.csv")
x=df.groupby(["season","toss_decision"]).size().unstack()
x.plot(kind="bar")
plt.title("toss decisions")
plt.xlabel("season")
plt.ylabel("decisions")
plt.show()
