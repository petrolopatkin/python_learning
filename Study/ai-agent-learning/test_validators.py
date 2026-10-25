import pytest 

from validators import validate_spending

def test_validate_spending_accepts_dict():
    data = {
        "description": "books",
        "amount": 18.4,
        "currency": "USD",
        "category": "books",
    }

    result = validate_spending(data)

    assert result == data


def test_validate_spending_rejects_list():
    data = [{
        "description": "books",
        "amount": 18.4,
        "currency": "USD",
        "category": "books",
    }]

    with pytest.raises(ValueError, match="Expected a JSON object"):
        validate_spending(data)


def test_validate_spending_rejects_invald_amount():
    data = {
            "description": "books",
            "amount": "eighteen",
            "currency": "USD",
            "category": "books",
        }
    
    with pytest.raises(ValueError, match="Invalid amount"):
        validate_spending(data)


def test_validate_seonding_rejects_boolean_amount():
    data = {
                "description": "books",
                "amount": True,
                "currency": "USD",
                "category": "books",
    }

    with pytest.raises(ValueError, match="Invalid amount"):
        validate_spending(data)


def test_validate_spending_rejects_unknown_amount():
    data = {
                    "description": "books",
                    "amount": None,
                    "currency": "USD",
                    "category": "books",
        }

    with pytest.raises(ValueError, match="Invalid amount"):
        validate_spending(data)


def test_validate_spending_rejects_not_string_currency():
    data = {
            "description": "books",
            "amount": 18.4,
            "currency": True,
            "category": "books",
        }

    with pytest.raises(ValueError, match="Currency must be a string or be 'None'"):
        validate_spending(data)


def test_validate_spending_rejects_not_string_category():
    data = {
                "description": "books",
                "amount": 18.4,
                "currency": "USD",
                "category": True,
        }

    with pytest.raises(ValueError, match="Category must be a string or be 'None'"):
        validate_spending(data)


def test_validate_spending_accepts_unknown_currency_and_category():
    data = {
                    "description": "books",
                    "amount": 18.4,
                    "currency": None,
                    "category": None,
    }

    result = validate_spending(data)

    assert result == data