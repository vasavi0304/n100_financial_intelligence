# Dataset Notes

## companies.xlsx

- Location: data/raw/companies.xlsx
- Header row: Row 2, loaded using header=1
- Records loaded: 92
- Primary Key: id
- Purpose: Master company reference table

### Columns
- id
- company_logo
- company_name
- chart_link
- about_company
- website
- nse_profile
- bse_profile
- face_value
- book_value
- roce_percentage
- roe_percentage

### Notes
- The first row contains metadata.
- Actual column headers start from the second row.
- Company id should be normalized using uppercase and stripped whitespace.

## profitandloss.xlsx

- Location: data/raw/profitandloss.xlsx
- Header row: Row 2, loaded using header=1
- Records: 1276
- Primary Key: (company, year)

### Important Columns
- id
- company
- year
- sales
- expenses
- operating_profit
- opm_percentage
- other_income
- interest
- depreciation
- profit_before_tax
- tax_percentage
- net_profit
- eps

### Notes
- Contains yearly profit and loss information.
- Year values include formats such as:
  - Mar 2024
  - Mar 2023
  - Dec 2012
  - TTM

  ## balancesheet.xlsx

- Location: data/raw/balancesheet.xlsx
- Header row: Row 2, loaded using header=1
- Records: 1312
- Primary Key: (company, year)

### Important Columns
- id
- company
- year
- equity_capital
- reserves
- borrowings
- other_liabilities
- total_liabilities
- fixed_assets
- cwip
- investments
- other_assets
- total_assets

### Notes
- Contains yearly balance sheet information.
- Year values include formats such as:
  - Mar 2024
  - Mar 2023
  - Dec 2012
  - Sep 2024
- total_assets should generally match total_liabilities.
- Will be used later for Balance Sheet validation checks.

![alt text](image.png)