import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("matches.csv")
x=df.groupby("team1").size()
y=df.groupby("team2").size()
totalm=x.add(y,fill_value=0)
winm=df.groupby("winner").size()
winrate=totalm/winm
result=pd.DataFrame({"Total Matches": totalm,"Winning Matches": winm,"Win Rate": winrate})
result.plot(kind="barh")
plt.title("Total Matches vs Winning Matches vs Win Rate")
plt.xlabel("matches")
plt.ylabel("teams")
plt.show()
