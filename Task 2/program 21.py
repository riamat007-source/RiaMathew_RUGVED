import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("matches.csv")
x=df["winner"].value_counts()
x.plot(kind="bar")
plt.title("win distribution")
plt.xlabel("teams")
plt.ylabel("wincount")
plt.show()
