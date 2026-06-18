import pandas as pd

file_path = "data/raw/companies.xlsx"

df = pd.read_excel(file_path, header=1)

print("Rows:", len(df))
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())