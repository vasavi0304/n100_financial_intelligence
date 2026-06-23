import pandas as pd

files = {
    "profitandloss": "data/raw/profitandloss.xlsx",
    "balancesheet": "data/raw/balancesheet.xlsx"
}

for name, path in files.items():
    df = pd.read_excel(path, header=1)

    duplicates = df[df.duplicated(subset=["company_id", "year"], keep=False)]

    print("\n" + "=" * 50)
    print(name)
    print("Duplicate rows:", len(duplicates))
    print(duplicates[["company_id", "year"]].head(20))