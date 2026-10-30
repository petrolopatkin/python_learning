import pytest
import database
from decimal import Decimal


def test_monthly_income_summary_with_incomes(monkeypatch):
    fake_incomes = [
    {
        "description": "Part-time job",
        "amount": Decimal("40.00"),
        "currency": "EUR",
        "income_date": None,
    },
    {
        "description": "Freelance",
        "amount": Decimal("65.00"),
        "currency": "EUR",
        "income_date": None,
    },
    ]

    monkeypatch.setattr(
        database,
        "get_income_by_month",
        lambda year, month: fake_incomes
    )

    summary = database.get_monthly_income(2026, 10)

    assert summary["totals_by_currency"] == {
        "EUR": Decimal("105.00")}
    assert summary["most_expensive_by_currency"]["EUR"]["description"] == 'Freelance'


def test_monthly_income_summary_with_multiple_currencies(monkeypatch):
    fake_incomes = [
    {
        "description": "Part-time job",
        "amount": Decimal("40.00"),
        "currency": "USD",
        "income_date": None,
    },
    {
        "description": "Freelance",
        "amount": Decimal("65.00"),
        "currency": "EUR",
        "income_date": None,
    },
    ]

    monkeypatch.setattr(
        database, 
        "get_income_by_month",
        lambda year, month: fake_incomes
    )

    summary = database.get_monthly_income(2026, 10)

    assert summary["totals_by_currency"] == {
        "USD": Decimal("40.00"),
        "EUR": Decimal("65.00"),
    }
    assert summary["most_expensive_by_currency"]["USD"]["description"] == 'Part-time job'
    assert summary["most_expensive_by_currency"]["EUR"]["description"] == 'Freelance'


def test_monthly_incomes_summary_without_earnings(monkeypatch):
    monkeypatch.setattr(
        database,
        "get_income_by_month",
        lambda year, month: []
    )

    summary = database.get_monthly_income(2026, 10)

    assert summary["totals_by_currency"] == {}
    assert summary["most_expensive_by_currency"] == {}