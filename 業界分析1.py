import pandas as pd
data={
    "企業":["A社","B社","C社"],
    "PER":[12,25,8]
}
df=pd.DataFrame(data)

#PERが高い順
print(df.sort_values("PER",ascending=False))
#平均
print("平均PER:",df["PER"].mean())
#割安企業
print(df[df["PER"]<15])