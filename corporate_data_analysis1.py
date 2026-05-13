import pandas as pd
data={
    "企業":["A社","B社","C社"],
    "PER":[12,25,8]
}
df=pd.DataFrame(data)
print("資料")
print(df.sort_values("企業"))
print("PERが高い順")
print(df.sort_values("PER",ascending=False))
print("平均")
avarage_per=df["PER"].mean()
print(f"平均PER:{avarage_per}")
print(f"{avarage_per}以下の割安企業")
print(df[df["PER"]<avarage_per])