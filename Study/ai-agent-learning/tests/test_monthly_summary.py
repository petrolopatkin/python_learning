import pytest
import database
from decimal import Decimal

def test_montly_summary_with_purchases(monkeypatch):
    fake_spendings = [{
        "Description": "Book",
        "Amount": Decimal("18.00"),
        "currency": "EUR",
        "category": "Education",
        "purchase_date": None,
    },
    {
        "Description": "Food",
        "Amount": Decimal("25.00"),
        "currency": "EUR",
        "category": "Food",
        "purchase_date": None,
    },]

    monkeypatch.setattr(
        database, 
        "get_spending_by_month",
        lambda year, month:
        fake_spendings,
    )

    summary = database.get_monthly_summary(2026, 10)

    assert summary["totals_by_currency"] == {
        "EUR": Decimal("43.00")
    }

    assert summary["most_expensive_by_currency"]["EUR"]["Description"] == 'Food'


def test_monthly_summary_with_multiple_currencies(monkeypatch):
    fake_spendings = [
        {
            "Description": "Book",
            "Amount": Decimal("18.00"),
            "currency": "EUR",
            "category": "Education",
            "purchase_date": None,
        },
        {
            "Description": "Lunch",
            "Amount": Decimal("12.00"),
            "currency": "USD",
            "category": "Food",
            "purchase_date": None,
        },
    ]

    monkeypatch.setattr(
        database, 
        "get_spending_by_month",
        lambda year, month :
        fake_spendings,
    )

    summary = database.get_monthly_summary(2026, 10)

    assert summary["totals_by_currency"] == {
        "EUR": Decimal("18.00"),
        "USD": Decimal("12.00"),
    }

    assert summary["most_expensive_by_currency"]["EUR"]['Description'] == 'Book'
    assert summary["most_expensive_by_currency"]["USD"]['Description'] == 'Lunch'


def test_monthly_summary_without_purchases(monkeypatch):
    monkeypatch.setattr(
        database, 
        "get_spending_by_month",
        lambda year, month: 
        [],
    )

    summary = database.get_monthly_summary(2026, 10)

    assert summary["totals_by_currency"] == {}

    assert summary["most_expensive_by_currency"] == {}