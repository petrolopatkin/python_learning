# There are all validators for my AI Agent studying practice

def validate_spending(data):
    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object")

    required_fields = ["description", "amount", "currency", "category"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    if not isinstance(data["description"], str):
        raise ValueError("Description must be a string")
    
    if isinstance(data["amount"], (int, float)) and not isinstance(data["amount"], bool) or data["amount"] is None:
        pass
    else:
        raise ValueError("Invalid amount")

    if not isinstance(data["currency"], str) and data["currency"] is not None:
        raise ValueError("Currency must be a string or be 'None'")

    if not isinstance(data["category"], str) and data["category"] is not None:
        raise ValueError("Category must be a string or be 'None'")

    return data