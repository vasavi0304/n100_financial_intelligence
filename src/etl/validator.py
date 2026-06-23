import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path("output/validation_failures.csv")


def add_failure(failures, rule_id, severity, dataset, column, message):
    failures.append({
        "rule_id": rule_id,
        "severity": severity,
        "dataset": dataset,
        "column": column,
        "message": message
    })


def validate_companies(failures):
    df = pd.read_excel("data/raw/companies.xlsx", header=1)
    dataset = "companies.xlsx"

    if df["id"].isnull().sum() > 0:
        add_failure(failures, "DQ-01", "CRITICAL", dataset, "id", "Missing company IDs found")

    if df["id"].duplicated().sum() > 0:
        add_failure(failures, "DQ-01", "CRITICAL", dataset, "id", "Duplicate company IDs found")

    if df["company_name"].isnull().sum() > 0:
        add_failure(failures, "DQ-06", "WARNING", dataset, "company_name", "Missing company names found")


def validate_profitandloss(failures):
    df = pd.read_excel("data/raw/profitandloss.xlsx", header=1)
    dataset = "profitandloss.xlsx"

    if df[["company_id", "year"]].duplicated().sum() > 0:
        add_failure(failures, "DQ-02", "WARNING", dataset, "company_id, year", "Duplicate company-year records found")

    if df["company_id"].isnull().sum() > 0:
        add_failure(failures, "DQ-03", "CRITICAL", dataset, "company_id", "Missing company IDs found")

    if (df["sales"] <= 0).sum() > 0:
        add_failure(failures, "DQ-06", "WARNING", dataset, "sales", "Sales should be positive")


def validate_balancesheet(failures):
    df = pd.read_excel("data/raw/balancesheet.xlsx", header=1)
    dataset = "balancesheet.xlsx"

    if df[["company_id", "year"]].duplicated().sum() > 0:
        add_failure(failures, "DQ-02", "WARNING", dataset, "company_id, year", "Duplicate company-year records found")

    diff = (df["total_assets"] - df["total_liabilities"]).abs()
    tolerance = df["total_assets"].abs() * 0.01

    if (diff > tolerance).sum() > 0:
        add_failure(
            failures,
            "DQ-04",
            "WARNING",
            dataset,
            "total_assets,total_liabilities",
            "Balance sheet mismatch greater than 1%"
        )


def validate_cashflow(failures):
    df = pd.read_excel("data/raw/cashflow.xlsx", header=1)
    dataset = "cashflow.xlsx"

    calc_net_cash = (
        df["operating_activity"]
        + df["investing_activity"]
        + df["financing_activity"]
    )

    diff = (df["net_cash_flow"] - calc_net_cash).abs()

    if (diff > 10).sum() > 0:
        add_failure(
            failures,
            "DQ-07",
            "WARNING",
            dataset,
            "net_cash_flow",
            "Net cash flow mismatch greater than 10 crore"
        )


def run_validation():
    failures = []

    validate_companies(failures)
    validate_profitandloss(failures)
    validate_balancesheet(failures)
    validate_cashflow(failures)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    failures_df = pd.DataFrame(failures)
    failures_df.to_csv(OUTPUT_PATH, index=False)

    print("Validation complete")
    print(f"Failures found: {len(failures_df)}")
    print(f"Saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    run_validation()