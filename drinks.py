import pandas as pd

df = pd.read_csv("/data/drinks.csv")

df["營收"] = df["單價"] * df["銷量"]
df["營收狀況"] = df["營收"].apply(lambda x: "超過7000" if x >= 7000 else "未達7000")
df["總營收"] = df["營收"].sum()

df.to_csv("/data/drinks_report.csv", index=False)