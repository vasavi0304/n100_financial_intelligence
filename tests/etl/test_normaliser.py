from src.etl.normaliser import normalize_ticker
from src.etl.normaliser import normalize_year


def test_ticker_uppercase():
    assert normalize_ticker("abb") == "ABB"


def test_ticker_strip_spaces():
    assert normalize_ticker(" abb ") == "ABB"


def test_ticker_none():
    assert normalize_ticker(None) is None


def test_year_mar():
    assert normalize_year("Mar 2024") == "Mar 2024"


def test_year_dec():
    assert normalize_year("Dec 2012") == "Dec 2012"


def test_year_ttm():
    assert normalize_year("TTM") == "TTM"