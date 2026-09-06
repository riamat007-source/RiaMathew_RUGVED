import pandas as pd
import numpy as np
df=pd.read_csv("matches.csv")
ar=np.array(df["win_by_runs"])
print("mean:",np.mean(ar))
print("median:",np.median(ar))
print("standard deviation:",np.std(ar))
