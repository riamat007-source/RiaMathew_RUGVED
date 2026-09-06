import pandas as pd
df=pd.read_csv("matches.csv")
y=df[df["result"]=="tie"]
print("The teams that tied are:")
print(y[["team1","team2"]])
