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