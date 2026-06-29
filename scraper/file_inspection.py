import pandas as pd

df = pd.read_excel("data/bronze/hcp_xlsx/data_1_5.xlsx")
print(df.head(15))
print(df.shape)
print(df.columns.tolist())