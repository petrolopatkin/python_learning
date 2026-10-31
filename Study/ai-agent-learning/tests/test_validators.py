import pytest 

from validators import validate_spending, validate_income

def test_validate_spending_accepts_dict():
    data = {
        "description": "books",
        "amount": 18.4,
        "currency": "USD",
        "category": "books",
        "purchase_date": None
    }

    result = validate_spending(data)

    assert result == data


def test_validate_spending_rejects_list():
    data = [{
        "description": "books",
        "amount": 18.4,
        "currency": "USD",
        "category": "books",
        "purchase_date": None
    }]

    with pytest.raises(ValueError, match="Expected a JSON object"):
        validate_spending(data)


def test_validate_spending_rejects_invald_amount():
    data = {
            "description": "books",
            "amount": "eighteen",
            "currency": "USD",
            "category": "books",
            "purchase_date": None
        }
    
    with pytest.raises(ValueError, match="Invalid amount"):
        validate_spending(data)


def test_validate_seonding_rejects_boolean_amount():
    data = {
                "description": "books",
                "amount": True,
                "currency": "USD",
                "category": "books",
                "purchase_date": None
    }

    with pytest.raises(ValueError, match="Invalid amount"):
        validate_spending(data)


def test_validate_spending_rejects_unknown_amount():
    data = {
                    "description": "books",
                    "amount": None,
                    "currency": "USD",
                    "category": "books",
                    "purchase_date": None
        }

    with pytest.raises(ValueError, match="Invalid amount"):
        validate_spending(data)


def test_validate_spending_rejects_not_string_currency():
    data = {
            "description": "books",
            "amount": 18.4,
            "currency": True,
            "category": "books",
            "purchase_date": None
        }

    with pytest.raises(ValueError, match="Currency must be a string"):
        validate_spending(data)


def test_validate_spending_rejects_not_string_category():
    data = {
                "description": "books",
                "amount": 18.4,
                "currency": "USD",
                "category": True,
                "purchase_date": None
        }

    with pytest.raises(ValueError, match="Category must be a string or be 'None'"):
        validate_spending(data)


def test_validate_spending_accepts_unknown_currency_and_category():
    data = {
                    "description": "books",
                    "amount": 18.4,
                    "currency": "EUR",
                    "category": None,
                    "purchase_date": None
    }

    result = validate_spending(data)

    assert result == data


def test_validate_spending_accepts_valid_purchase_date():
    data = {
                    "description": "books",
                    "amount": 18.4,
                    "currency": "EUR",
                    "category": None,
                    "purchase_date": "2026-10-26"
    }

    result = validate_spending(data)

    assert result == data


def test_validate_spending_accepts_unknown_purchase_date():
    data = {
                        "description": "books",
                        "amount": 18.4,
                        "currency": "EUR",
                        "category": None,
                        "purchase_date": None
        }

    result = validate_spending(data)

    assert result == data


def test_validate_spending_rejects_incorrect_purchase_date():
    data = {
                        "description": "books",
                        "amount": 18.4,
                        "currency": "EUR",
                        "category": None,
                        "purchase_date": "2026-10-40"
        }

    with pytest.raises(ValueError, match="Purchase date must be a valid date in YYYY-MM-DD format"):
        validate_spending(data)


def test_validate_income_accepts_dict():
    data = {
    "description": "Part-time job",
    "amount": 250.0,
    "currency": "EUR",
    "income_date": "2026-10-30"
    }

    result = validate_income(data)

    assert result == data


def test_validate_income_rejects_list():
    data = [
    "Part-time job",
    250.0,
    "EUR",
    "2026-10-30"
    ]

    with pytest.raises(ValueError, match="Expected a JSON object"):
        validate_income(data)


def test_validate_income_reject_missing_field():
    data = {
    "description": "Part-time job",
    "amount": 250.0,
    "currency": "EUR"
    }

    with pytest.raises(ValueError, match=f"Missing required field: income_date"):
        validate_income(data)


def test_validate_income_rejects_empty_description():
    data = {
    "description": "   ",
    "amount": 250.0,
    "currency": "EUR",
    "income_date": "2026-10-30"
    }

    with pytest.raises(ValueError, match="Description cannot be empty"):
        validate_income(data)


def test_validate_income_rejects_incorrect_type_of_amount():
    data = {
    "description": "Part-time job",
    "amount": "250",
    "currency": "EUR",
    "income_date": "2026-10-30"
    }

    with pytest.raises(ValueError, match="Invalid amount"):
        validate_income(data)


def test_validate_income_rejects_boolean_amount():
    data = {
    "description": "Part-time job",
    "amount": True,
    "currency": "EUR",
    "income_date": "2026-10-30"
    }

    with pytest.raises(ValueError, match="Invalid amount"):
        validate_income(data)


def test_validate_income_rejects_amount_equals_zero():
    data = {
    "description": "Part-time job",
    "amount": 0,
    "currency": "EUR",
    "income_date": "2026-10-30"
    }

    with pytest.raises(ValueError, match="Invalid amount"):
        validate_income(data)


def test_validate_income_rejects_negative_amount():
    data = {
    "description": "Part-time job",
    "amount": -50.0,
    "currency": "EUR",
    "income_date": "2026-10-30"
    }

    with pytest.raises(ValueError, match="Invalid amount"):
        validate_income(data)


def test_validate_income_rejects_none_currency():
    data = {
    "description": "Part-time job",
    "amount": 250.0,
    "currency": None,
    "income_date": "2026-10-30"
    }

    with pytest.raises(ValueError, match="Currency must be a string"):
        validate_income(data)


def test_validate_income_rejects_empty_currency():
    data = {
    "description": "Part-time job",
    "amount": 250.0,
    "currency": "   ",
    "income_date": "2026-10-30"
    }

    with pytest.raises(ValueError, match="Currency cannot be empty"):
        validate_income(data)


def test_validate_income_rejects_none_income_date():
    data = {
    "description": "Part-time job",
    "amount": 250.0,
    "currency": "EUR",
    "income_date": None
    }

    with pytest.raises(ValueError, match="Income date must be a string"):
        validate_income(data)


def test_validate_income_rejects_incorrect_date():
    data = {
    "description": "Part-time job",
    "amount": 250.0,
    "currency": "EUR",
    "income_date": "2026-10-40"
    }

    with pytest.raises(ValueError, match="Income date must be a valid date in YYYY-MM-DD format"):
        validate_income(data)


def test_validate_income_accepts_correct_date():
    data = {
    "description": "Part-time job",
    "amount": 250.0,
    "currency": "EUR",
    "income_date": "2026-10-30"
    }

    result = validate_income(data)

    assert result == data