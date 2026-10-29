from decimal import Decimal
import tools
import pytest 
from tools import make_json_safe
from tools import get_monthly_report_for_gemini
from datetime import date as real_date

def test_get_monthly_spending_report(monkeypatch):
    fake_summary = {
        "totals_by_currency": {
            "EUR": Decimal("54.00")
        },
        "most_expensive_by_currency": {
            "EUR": {
                "Description": "test book",
                "Amount": Decimal("18.00"),
                "currency": "EUR",
                "category": "education",
                "purchase_date": None,
            },
        },
    }

    monkeypatch.setattr(
        tools, 
        "get_monthly_summary",
        lambda year, month: fake_summary,
    )

    report = tools.get_monthly_spending_report(2026, 10)

    assert report["year"] == 2026
    assert report["month"] == 10
    assert report["totals_by_currency"] == {
        "EUR": Decimal("54.00")
    }
    assert report["most_expensive_by_currency"]["EUR"]["Description"] == "test book"


def test_make_json_safe_with_decimal():
    result = make_json_safe(Decimal("18.50"))

    assert result == 18.5
    assert isinstance(result, float)


def test_make_json_safe_with_date():
    result = make_json_safe(real_date(2026, 10, 26))

    assert result == "2026-10-26"


def test_make_json_safe_with_unsupported_type():
    with pytest.raises(TypeError):
        make_json_safe(object())


def test_make_json_safe_with_nested_dict():
    data = {
        "purchase": {
            "Amount": Decimal("18.00"),
            "purchase_date": real_date(2026, 10, 26),
        }
    }

    result = make_json_safe(data)

    assert result == {
        "purchase": {
            "Amount": 18.00,
            "purchase_date": "2026-10-26",
        }
    }


def test_get_monthly_report_for_gemini(monkeypatch):
    def fake_report(year, month):
        assert year == 2026
        assert month == 10

        return {
            "year": year,
            "month": month,
            "totals_by_currency": {
                "EUR": Decimal("18.00")
            },
            "most_expensive_by_currency": {
                "EUR": {
                    "Description": "book",
                    "Amount": Decimal("18.00"),
                    "currency": "EUR",
                    "category": "education",
                    "purchase_date": real_date(2026, 10, 26),
                }
            },
        }

    monkeypatch.setattr(
        "tools.get_current_date", 
        lambda: real_date(2026, 10, 26)
    )
    monkeypatch.setattr("tools.get_monthly_spending_report", fake_report,
                        )

    result = get_monthly_report_for_gemini()

    assert result["year"] == 2026
    assert result["month"] == 10
    assert result["totals_by_currency"]["EUR"] == 18.0
    assert(
        result["most_expensive_by_currency"]["EUR"]["purchase_date"] == "2026-10-26"
    ) 