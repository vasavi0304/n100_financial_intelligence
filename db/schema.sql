PRAGMA foreign_keys = ON;

CREATE TABLE companies (
    id TEXT PRIMARY KEY,
    company_name TEXT,
    company_logo TEXT,
    chart_link TEXT,
    about_company TEXT,
    website TEXT,
    nse_profile TEXT,
    bse_profile TEXT,
    face_value REAL,
    book_value REAL,
    roce_percentage REAL,
    roe_percentage REAL
);

CREATE TABLE profitandloss (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    sales REAL,
    expenses REAL,
    operating_profit REAL,
    opm_percentage REAL,
    other_income REAL,
    interest REAL,
    depreciation REAL,
    profit_before_tax REAL,
    tax_percentage REAL,
    net_profit REAL,
    eps REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE balancesheet (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    total_assets REAL,
    total_liabilities REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE cashflow (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    operating_activity REAL,
    investing_activity REAL,
    financing_activity REAL,
    net_cash_flow REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE analysis (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    compounded_sales_growth TEXT,
    compounded_profit_growth TEXT,
    stock_price_cagr TEXT,
    roe TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE documents (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    annual_report TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE prosandcons (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    pros TEXT,
    cons TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE sectors (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    broad_sector TEXT,
    sub_sector TEXT,
    index_weight REAL,
    market_cap_category TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE stock_prices (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    date TEXT,
    open_price REAL,
    high_price REAL,
    low_price REAL,
    close_price REAL,
    volume REAL,
    adjusted_close REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE financial_ratios (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE peer_groups (
    id INTEGER PRIMARY KEY,
    peer_group TEXT,
    company_id TEXT,
    is_benchmark TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE market_cap (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    market_cap REAL,
    enterprise_value REAL,
    pe_ratio REAL,
    pb_ratio REAL,
    ev_ebitda REAL,
    dividend_yield_pct REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);