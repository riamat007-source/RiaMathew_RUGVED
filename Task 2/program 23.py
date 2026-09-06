import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("matches.csv")
x=df.groupby("winner").size()
x.sort_values(ascending=False).head(5).plot(kind="barh")
plt.title("top five teams")
plt.xlabel("times won")
plt.ylabel("team")
plt.show()
