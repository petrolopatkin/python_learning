from database import get_monthly_summary, get_monthly_income
from decimal import Decimal
from datetime import date

def get_monthly_spending_report(year: int, month: int) -> dict:
    """Return the spending totals and
    most expensive purchases for a month"""
    summary = get_monthly_summary(year, month)

    report = {
        "year": year,
        "month": month,
        "totals_by_currency": summary["totals_by_currency"],
        "most_expensive_by_currency": summary["most_expensive_by_currency"],
    }

    return report


def get_monthly_income_report(year: int, month: int) -> dict:
    """Return monthly income totals and 
    the lasrgest incomes by currency"""

    summary = get_monthly_income(year, month)

    report = {
        "year": year,
        "month": month,
        "totals_by_currency": summary["totals_by_currency"],
        "most_expensive_by_currency": summary["most_expensive_by_currency"],
    }

    return report


def get_current_date():
    return date.today()


def get_monthly_report_for_gemini() -> dict:
    """Get the spending report for the current month
    """

    today = get_current_date()

    report = get_monthly_spending_report(today.year, today.month)
    return make_json_safe(report)


def get_monthly_income_report_for_gemini() -> dict:
    """Get the monthly income report for the current month"""

    today = get_current_date()

    report = get_monthly_income_report(today.year, today.month)
    return make_json_safe(report)


def make_json_safe(value):
    if isinstance(value, Decimal):
        return float(value)

    if isinstance(value, date):
        return value.isoformat()

    if isinstance(value, dict):
        return {
            key: make_json_safe(item)
            for key, item in value.items()
        }

    if isinstance(value, list):
        return [make_json_safe(item) for item in value]

    if value is None or isinstance(value, (str, int, float, bool)):
        return value

    raise TypeError(f"Unsupported type: {type(value).__name__}")