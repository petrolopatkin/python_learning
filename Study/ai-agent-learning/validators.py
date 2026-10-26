# There are all validators for my AI Agent studying practice
from datetime import date

def validate_spending(data):
    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object")

    required_fields = ["description", "amount", "currency", "category", "purchase_date"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    if not isinstance(data["description"], str):
        raise ValueError("Description must be a string")
    
    if not isinstance(data["amount"], (int, float)) or isinstance(data["amount"], bool) or data["amount"] <= 0:
        raise ValueError("Invalid amount")

    if not isinstance(data["currency"], str) and data["currency"] is not None:
        raise ValueError("Currency must be a string or be 'None'")

    if not isinstance(data["category"], str) and data["category"] is not None:
        raise ValueError("Category must be a string or be 'None'")

    purchase_date = data["purchase_date"]

    if purchase_date is not None:
        if not isinstance(purchase_date, str):
            raise ValueError("Purchase date must be a string or None")

        try:
            date.fromisoformat(purchase_date)
        except ValueError:
            raise ValueError("Purchase date must be a valid date in YYYY-MM-DD format")

    return data